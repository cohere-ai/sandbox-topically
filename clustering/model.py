

from mimetypes import init
from concurrent.futures import ThreadPoolExecutor
import getpass
import logging

import cohere
import numpy as np
from clustering.agglomerative import Agglomerative


class Clustering:
    def __init__(self, technique: str = 'Agglomerative', api_key: str = None, mockAPI: bool = False):
        self.technique = technique
        if mockAPI:
            self.co = MockCohereAPI()
        else:
            if api_key is None:
                api_key = getpass.getpass('Enter your Cohere API Key')

            self.co = cohere.Client(api_key)

    def get_clusters(self, sentences, parameter):
        if self.technique == 'Agglomerative':
            agglomerative = Agglomerative(sentences, parameter, self.co)
            cluster_assignments, embeddings = agglomerative.get_clusters()
            return cluster_assignments, embeddings


class MockCohereAPI:
    """Mock Cohere API for testing."""

    def __init__(self):
        pass

    def generate(self, **kwargs):
        mock_gens_list = [
            cohere.generation.Generation(
                text='two', likelihood=-10, token_likelihoods=None),
            cohere.generation.Generation(
                text='one', likelihood=-5, token_likelihoods=None)
        ]
        mock_gens = cohere.generation.Generations(
            generations=mock_gens_list, return_likelihoods=None)

        return mock_gens
