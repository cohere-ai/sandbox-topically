from topically import Topically, cluster_namers
from topically.app import MockCohereAPI
from topically.cluster_namers import ClusterNamer
import cohere
import numpy as np


def test_cluster_namer():
    assert True


def test_reranker():
    """ Test that reranker properly orders generations by likelihood """
    api = MockCohereAPI()
    mock_gens_list = api.generate().generations

    # mock_gens_list = [cohere.generation.Generation(text='two', likelihood=-10, token_likelihoods=None),
    #                   cohere.generation.Generation(text='one', likelihood=-5, token_likelihoods=None)]
    # mock_gens = cohere.generation.Generations(generations=mock_gens_list, return_likelihoods=None)

    ranked_generations = cluster_namers.rerank_by_likelihood(mock_gens_list)
    assert list(ranked_generations) == ['one', 'two']


def test_cluster_namer():
    """ Test that test_cluster_namer() returns n_samples names """
    app = Topically('', mockAPI=True)

    cluster_names = app.name_clusters(([0, 0, 0], [1, 1, 1]),
                                      num_generations=5)

    print(cluster_names)
    assert cluster_names == ['one', 'one', 'one']
