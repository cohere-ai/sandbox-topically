import umap.umap_ as umap
import numpy as np
import pandas as pd
from sklearn.manifold import TSNE


def umap_reduce(table_df,embeds):
    """
    this will reduce the embeddings to a manageable dimension for plotting

    param embeds: embedding array of the sentences
    param n_neighbors: This parameter controls how UMAP balances local versus global structure in the data

    returns: dataframe of reduced dimensions
    """
    labels = table_df['topic_name']
    sentences = table_df['Utterance']
    X_embedded = TSNE(random_state=0, n_components=1).fit_transform(embeds)
    df_embeddings = pd.DataFrame(X_embedded)
    df_embeddings = df_embeddings.rename(columns={0:'x',1:'y'})
    df_embeddings = df_embeddings.assign(label=table_df['topic_name'].values)
    df_embeddings = df_embeddings.assign(text=table_df['Utterance'].values)
    return df_embeddings





