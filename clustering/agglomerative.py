from os import truncate
from sklearn.cluster import AgglomerativeClustering
import numpy as np
from keybert import KeyBERT
import pandas as pd


class Agglomerative:
    def __init__(self, sentences, parameter, cohere_client):
        self.sentences = sentences
        self.parameter = parameter
        self.cohere_client = cohere_client

    def find_cluster_name(self, sentences, embedding_model):
        """_Get the cluster name_
        Args:
            value (_List_): _List of utterances_
        Returns:
            _str_: _cluster name_
        """

        #### KEY BERT ######
        kw_model = KeyBERT(model=embedding_model)
        s = ','.join((str(n) for n in sentences))
        keywords = kw_model.extract_keywords(s, keyphrase_ngram_range=(
            1, 3), stop_words='english', use_mmr=True, diversity=0.7)
        cluster_name = keywords[0][0]
        return cluster_name

    def get_clusters(self):
        """_Return clusters of sentences_

        Returns:
            _dataframe_: _Clustername,Utterance_
        """
        corpus_embeddings_model = self.cohere_client.embed(
            texts=self.sentences, model='large', truncate='LEFT')
        corpus_embeddings_embed = corpus_embeddings_model.embeddings
        # Normalize the embeddings to unit length
        corpus_embeddings_embed = corpus_embeddings_embed / \
            np.linalg.norm(corpus_embeddings_embed, axis=1, keepdims=True)
        clustering_model = AgglomerativeClustering(
            n_clusters=None, distance_threshold=self.parameter)
        clustering_model.fit(corpus_embeddings_embed)
        cluster_assignment = clustering_model.labels_

        clustered_sentences = {}
        for sentence_id, cluster_id in enumerate(cluster_assignment):
            if cluster_id not in clustered_sentences:
                clustered_sentences[cluster_id] = []
            clustered_sentences[cluster_id].append(self.sentences[sentence_id])

        final_clustered = {}

        for i, cluster in clustered_sentences.items():
            print(f'Cluster: {i+1}')
            print(cluster)
            print("")
            final_clustered.update({i+1: cluster})

        final_clustered_names = []

        for key, value in final_clustered.items():
            cluster_name = self.find_cluster_name(
                value, corpus_embeddings_model)
            for utterance in value:
                final_clustered_names.append([cluster_name, utterance])

        df = pd.DataFrame(final_clustered_names, columns=[
                          'Cluster_name', 'Utterance'])
        return df,corpus_embeddings_embed
