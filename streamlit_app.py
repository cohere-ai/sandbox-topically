import streamlit as st
import numpy as np
from collections import OrderedDict
import pandas as pd
from streamlit_option_menu import option_menu
from clustering.model import Clustering
import topically
from topic_visualization import umap_reduce
import plotly.express as px

APP_NAME = "Cohere Topic Modelling co:topic 🚀"


###### HELPER METHOD ######

def display_clustering(selected2, sentences, parameter):
    technique = Clustering(
        selected2, 'api_key')
    df,embeddings = technique.get_clusters(sentences, parameter)
    return df,embeddings

####### STREAMLIT COMPONENTS FOR CONTROLLING PARAMETERS ########

######### CREATE SCATTER PLOT OF VISUALIZING TOPICS #########

def create_scatter(table_df,embeddings):
    reduced_df = umap_reduce(table_df,embeddings)
   
    scatter = px.scatter(reduced_df, x='x',y='label',color='label',labels={'color':'label'},
                            hover_data=['text'],title='Topic Visualization')

    st.plotly_chart(scatter)


##########################
# UI
##########################
if __name__ == '__main__':
    st.set_page_config(
        page_title=APP_NAME,
        page_icon=":bar_chart:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    # title and image
    sentences = []
    h1, h2 = st.columns([1, 10])
    h1.image('./assets/profile-white-logo.png', width=90)
    h2.title('Topic Modelling with Cohere')
    with st.empty():
        st.write('\n#\n')
    with st.form('Utterances'):
        uploaded_file = st.file_uploader(
            "Add lines of text for Topic modelling(.txt file)",type=["txt"])
        selected2 = option_menu(None, ["Agglomerative", "K-Means", "DBSCAN"],
                                icons=['tree', 'collection', 'upc-scan'],
                                menu_icon="cast", orientation="horizontal")
        if selected2 == 'Agglomerative':
            parameter = st.sidebar.slider(
                "distance_threshold", min_value=1.4, max_value=2.0, value=1.4, step=0.05
            )
        elif selected2 == 'K-Means':
            parameter = st.sidebar.slider(
                "Value of K", min_value=2, max_value=10, value=2, step=1
            )
        option = st.selectbox(
            'Choose a Topic Modelling Approach', ('KeyBert + Prompt', 'BERTopic', 'Latent Dirichlet Allocation'))
        submitted = st.form_submit_button('Submit')

    if submitted:
        print(selected2)
        if uploaded_file:
            for line in uploaded_file:
                sentences.append(line.decode("utf-8").replace('\n', ''))
            print(sentences)
            with st.spinner(text='Clustering in progress'):
                df,embeddings = display_clustering(selected2, sentences, parameter)
            print(embeddings)
            app = topically.Topically(option,'api_key')
            df['topic_name'], topic_names = app.name_topics((df['Utterance'],df['Cluster_name']))
            table_df = df.drop('Cluster_name',axis=1)
            
            st.table(table_df)
            with st.container():
                with st.empty():
                    st.write('\n#\n#\n')
                with st.expander('Topic Visualization'):
                    create_scatter(table_df,embeddings)
        
        else:
            st.write('Please check the input file 💥')
