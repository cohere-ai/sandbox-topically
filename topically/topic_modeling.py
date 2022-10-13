# Copyright (c) 2022 Cohere Inc. and its affiliates.
#
# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
#
# You may obtain a copy of the License in the LICENSE file at the top
# level of this repository.

from ctfidf import ClassTFIDF
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer


def cluster_kmeans(embeds, n_clusters):
    kmeans_model = KMeans(n_clusters=n_clusters, random_state=0)
    classes = kmeans_model.fit_predict(embeds)

    return classes


def extract_keywords(df, classes, max_df=0.6):
    documents = df['title']
    documents = pd.DataFrame({"Document": documents, "ID": range(len(documents)), "Topic": None})
    documents['Topic'] = classes
    documents_per_topic = documents.groupby(['Topic'], as_index=False).agg({'Document': ' '.join})

    count_vectorizer = CountVectorizer(ngram_range=(1, 3), max_df=max_df,
                                       stop_words="english").fit(documents_per_topic.Document)
    count = count_vectorizer.transform(documents_per_topic.Document)
    words = count_vectorizer.get_feature_names()

    ctfidf = ClassTFIDF().fit_transform(count).toarray()

    words_per_class = {
        label: [words[index] for index in ctfidf[label].argsort()[-10:]] for label in documents_per_topic.Topic
    }
    df['cluster'] = classes
    df['keywords'] = df['cluster'].map(lambda topic_num: ", ".join(np.array(words_per_class[topic_num])[:]))

    # def convert_dict_to_dataframe(dict):
    keywords_list = []
    for k, v in words_per_class.items():
        keywords = ", ".join(v)
        keywords_list.append(keywords)

    return df, keywords_list, words_per_class
