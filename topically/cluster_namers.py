# Copyright (c) 2022 Cohere Inc. and its affiliates.
#
# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
#
# You may obtain a copy of the License in the LICENSE file at the top
# level of this repository.

import cohere.generation
import numpy as np
from sklearn.base import BaseEstimator


class ClusterNamer(BaseEstimator):
    """ Assign names to clusters of text based on their content using managed Language Models from Cohere."""
    def __init__(self, co, prompt: str = '', num_generations: int = 1, temperature=0.6):
        """
        Name a cluster using the default prompt. Calls the Cohere generate end-point to assign a name to the cluster.

        Parameters
        ----------
            co: Python cohere SDK object
            prompt: str
                The text prompt the generative model uses to name a cluster
            num_generations: int
                The number of candidate generations to get for each cluster. Multiple generations can enhance the quality of cluster names.
            temperature: float
                Typically between 0-1, the temperature value used to control the randomness of the generation model. Lower values lead to more predictable, less "creative" names.

        """
        self.co = co
        self.prompt = prompt
        self.num_generations = num_generations
        self.temperature = temperature

    def make_prompt(self, cluster_example_texts):
        """
        Prepare the naming prompt by adding examples from a single cluster to the prompt.

        Parameters
        ----------
            cluster_example_texts: array-like of strings
                A collection of texts belonging to a single cluster/topic. They are added to the naming prompt

        Returns
        -------
            prompt: str
               The naming prompt including the examples from this cluster

        """
        # Add the data of the current cluster we want to label
        return self.prompt + construct_example_for_prompt(cluster_example_texts)

    def generate(self, cluster_example_texts):
        """
        Generate suggest topic name(s)

        Parameters
        ----------
            cluster_example_texts: array-like of strings
                A collection of texts belonging to a single cluster/topic. They are added to the naming prompt

        Returns
        -------
            generations: list of Cohere Generation objects.
               The cluster names suggest by the generative model

        """
        # Add the data of the current cluster we want to label
        prompt = self.make_prompt(cluster_example_texts)

        # Generate using the language model
        request = self.co.generate(model='xlarge',
                                   prompt=prompt,
                                   max_tokens=50,
                                   num_generations=self.num_generations,
                                   return_likelihoods='GENERATION',
                                   stop_sequences=["\n"])

        return request.generations

    def predict(self, texts):
        """
        Generate a name for a single topic

        Parameters
        ----------
            texts: array-like of strings
                A collection of texts belonging to a single cluster/topic. They are used to help the model suggest a name for the clsuter.

        Returns
        -------
            topic_name: str
               The suggest name for the topic/cluster.

        """
        gens = self.generate(texts)

        if self.num_generations > 1:
            gens = rerank_by_likelihood(gens)
            return gens[0]

        return gens[0].text.strip()


def rerank_by_likelihood(generations: cohere.generation.Generations):
    """
    Get a list of generations from Cohere's Generate endpoint, order them by highest likelihood score.

    Parameters
    ----------
        generations: cohere.generation.Generations object
          Contains a list of generations (length: n_samples) from Cohere's Generate endpoint containing generated texts and token likelihoods.

    Returns
    -------
        ordered_generations: array-like of length n_samples
           The same list of generations, except ordered by highest likelihoods

    """

    # Sort by most likely, most likely generations first
    likelihoods = np.array([gen.likelihood for gen in generations])
    texts = np.array([gen.text.strip() for gen in generations])
    sorted_indexes = likelihoods.argsort()[::-1]
    new_indices = likelihoods[sorted_indexes]
    ordered_generations = texts[sorted_indexes]
    print(ordered_generations)

    return ordered_generations


def construct_example_for_prompt(cluster_example_texts):
    """
    Prepare a single portion of the prompt by stitching the texts as an example

    Parameters
    ----------
        cluster_example_texts: array-like of strings
            A collection of texts belonging to a single cluster/topic. They are used to help the model suggest a name for the clsuter.

    Returns
    -------
        example_prompt_text: str
           A portion of a naming prompt

    """
    example_prompt_text = f'\nCluster:\nSample texts from this cluster:\n'
    for text in cluster_example_texts:
        example_prompt_text += f'- {text}\n'

    example_prompt_text += f'Cluster name:'

    return example_prompt_text
