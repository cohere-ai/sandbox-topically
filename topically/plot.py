# Copyright (c) 2022 Cohere Inc. and its affiliates.
#
# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
#
# You may obtain a copy of the License in the LICENSE file at the top
# level of this repository.

from typing import List

import altair as alt
import pandas as pd


def interactive_scatterplot(df: pd.DataFrame, fields_in_tooltip: List[str] = None, title: str = ''):
    """
    Create interactive scatterplot. Basic plot showing point details on hover. Single color for all the points.

    Parameters
    ----------
        df: pandas dataframe
          Must contain columns:
          x: x-coordinate of point. Usually UMAP dimension transformed from embeddings
          y: y-coordinate of point. Usually UMAP dimension transformed from embeddings

        fields_in_tooltip: List of strings
        The names of the other columns to show in the tooltip that appears when hovering over a point.

        title: str
        The title of the plot.


    Returns
    -------
        chart: altair chart
           The interactive altair chart. Can be the displayed or saved.

    """
    if fields_in_tooltip is None:
        fields_in_tooltip = ['']
    chart = alt.Chart(df).mark_circle(size=20).encode(
        x=alt.X('x', scale=alt.Scale(zero=False), axis=alt.Axis(labels=False, ticks=False, domain=False)),
        y=alt.Y('y', scale=alt.Scale(zero=False), axis=alt.Axis(labels=False, ticks=False, domain=False)),
        tooltip=fields_in_tooltip).configure(background="#f6f6f6").properties(width=700, height=400, title=title)

    return chart


def interactive_clusters_scatterplot(df: pd.DataFrame,
                                     fields_in_tooltip: List[str] = None,
                                     title: str = '',
                                     title_column: str = 'keywords'):
    """
     Create interactive scatterplot for clusters. Shows point details on hover. Each cluster is assigned its own color. Sidebar shows the names of the clusters.

     Parameters
     ----------
         df: pandas dataframe
           Must contain columns:
           x: x-coordinate of point. Usually UMAP dimension transformed from embeddings
           y: y-coordinate of point. Usually UMAP dimension transformed from embeddings

         fields_in_tooltip: List of strings
         The names of the other columns to show in the tooltip that appears when hovering over a point.

         title: str
         The title of the plot.

         title_column:
            The column in df holding the name of the cluster. Used to display cluster names in sidebar.

     Returns
     -------
         chart: altair chart
            The interactive altair chart. Can be the displayed or saved.

     """
    if fields_in_tooltip is None:
        fields_in_tooltip = ['']

    selection = alt.selection_multi(fields=[title_column], bind='legend')

    chart = alt.Chart(df).transform_calculate(
        # url='https://news.ycombinator.com/item?id=' + alt.datum.id
    ).mark_circle(size=20, stroke='#666', strokeWidth=1, opacity=0.1).encode(
        x=  # 'x',
        alt.X('x', scale=alt.Scale(zero=False), axis=alt.Axis(labels=False, ticks=False, domain=False)),
        y=alt.Y('y', scale=alt.Scale(zero=False), axis=alt.Axis(labels=False, ticks=False, domain=False)),
        # href='url:N',
        color=alt.Color(
            f'{title_column}:N',
            legend=alt.Legend(
                columns=2,
                symbolLimit=0,
                orient='right',
                # legendX=130, legendY=-40,
                labelFontSize=12)),
        opacity=alt.condition(selection, alt.value(1), alt.value(0.2)),
        tooltip=fields_in_tooltip).properties(
            width=1000,
            height=700).add_selection(selection).configure_legend(labelLimit=0).configure_view(strokeWidth=0).configure(
                background="#F6f6f6").properties(title=title).configure_range(category={'scheme': 'category20'})

    return chart
