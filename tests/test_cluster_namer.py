# Copyright (c) 2022 Cohere Inc. and its affiliates.
#
# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
#
# You may obtain a copy of the License in the LICENSE file at the top
# level of this repository.

import cohere
import numpy as np

from topically import cluster_namers
from topically import Topically
from topically.app import MockCohereAPI
from topically.cluster_namers import ClusterNamer


def test_cluster_namer():
    assert True


def test_reranker():
    """ Test that reranker properly orders generations by likelihood."""

    api = MockCohereAPI()
    mock_gens_list = api.generate().generations

    ranked_generations = cluster_namers.rerank_by_likelihood(mock_gens_list)
    assert list(ranked_generations) == ['one', 'two']


def test_cluster_namer():
    """ Test that test_cluster_namer() returns n_samples names."""

    app = Topically('', mockAPI=True)

    cluster_names = app.name_clusters(([0, 0, 0], [1, 1, 1]), num_generations=5)

    print(cluster_names)
    assert cluster_names == ['one', 'one', 'one']
