# Copyright (c) 2022 Cohere Inc. and its affiliates.
#
# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
#
# You may obtain a copy of the License in the LICENSE file at the top
# level of this repository.

from concurrent.futures import ThreadPoolExecutor
import getpass
import logging

import cohere
import numpy as np

from .cluster_namers import ClusterNamer
from .prompts.prompts import generic_cluster_naming_prompt


class Topically(object):

    def __init__(self, api_key: str = None, mockAPI: bool = False):
        if mockAPI:
            self.co = MockCohereAPI()
        else:
            if api_key is None:
                api_key = getpass.getpass('Enter your Cohere API Key')

            self.co = cohere.Client(api_key)

    def name_clusters(self, X, prompt: str = '', num_generations=1, num_sample_texts=10):
        """
        Name clusters using the default prompt. For each cluster, calls the Cohere generate end-point to assign a name to the cluster.
        Example: If we have ten samples clustered into two clusters (0,1), this makes two generation API calls. That results in two cluster names. We return n_samples,

        Parameters
        ----------
            X: array-like of shape (n_samples, 2)
              A tuple of two arrays. One is the texts (str), the second is their cluster assignments (int).

        Returns
        -------
            assigned_cluster_names: array-like of length n_samples
               The cluster name assigned to each text

        """

        # Get the texts and their cluster assignments
        texts, cluster_assignments = X

        if isinstance(cluster_assignments, list):
            cluster_assignments = np.array(cluster_assignments)

        if isinstance(texts, list):
            texts = np.array(texts)

        if prompt == '':
            prompt = generic_cluster_naming_prompt

        # Instantiate ClusterNamer
        cluster_namer = ClusterNamer(self.co, prompt, num_generations=num_generations)

        # Get the unique cluster assignments
        unique_cluster_assignments = np.unique(cluster_assignments)

        # Create a dictionary to store the cluster names for each cluster
        cluster_names = {}

        extracted = []
        cluster_names = {}

        def name_cluster(cluster_number):
            # Get the texts in this cluster, sample from them
            cluster_texts = texts[cluster_assignments == cluster_number]
            # sample_texts_from_cluster = cluster_texts.sample(num_sample_texts)
            if len(cluster_texts) > num_sample_texts:
                sample_texts_from_cluster = np.random.choice(cluster_texts, num_sample_texts, replace=False)
            else:
                sample_texts_from_cluster = cluster_texts

            cluster_name = cluster_namer.predict(sample_texts_from_cluster)

            logging.info(f'naming cluster {cluster_number}: {cluster_name}')

            return cluster_number, cluster_name

        # Name all clusters in parallel
        with ThreadPoolExecutor(max_workers=8) as executor:
            for (cluster_number, cluster_name) in executor.map(name_cluster, unique_cluster_assignments):
                cluster_names[cluster_number] = cluster_name


        # Create a list to store the cluster assignments per sample
        assigned_cluster_names = [cluster_names[cluster_number] for cluster_number in cluster_assignments]

        return assigned_cluster_names

    def name_cluster(self, cluster_texts, temperature=0.6, num_generations=1):
        """
        Name a cluster using the default prompt. Calls the Cohere generate end-point to assign a name to the cluster.

        Parameters
        ----------
            cluster_texts: array-like of shape (n_samples,)
              The texts in the cluster to be named.

        Returns
        -------
            cluster_name: str
               The cluster name assigned to the cluster

        """

        # Create the prompt, starting with the global task description
        prompt = 'The following texts are from the same cluster. Please name the cluster.'

        # Add the data of the current cluster we want to label
        prompt += self.construct_example_for_prompt(cluster_texts)

        # Generate the cluster name
        cluster_name = self.generate(prompt, temperature=temperature, num_generations=num_generations)[0]

        return cluster_name


class MockCohereAPI:
    """Mock Cohere API for testing."""

    def __init__(self):
        pass

    def generate(self, **kwargs):
        mock_gens_list = [
            cohere.generation.Generation(text='two', likelihood=-10, token_likelihoods=None),
            cohere.generation.Generation(text='one', likelihood=-5, token_likelihoods=None)
        ]
        mock_gens = cohere.generation.Generations(generations=mock_gens_list, return_likelihoods=None)

        return mock_gens
