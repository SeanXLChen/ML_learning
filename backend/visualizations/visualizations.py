"""
This file provided method involves graphing and visualizations.
"""

import plotly.graph_objects as go


def plot_data(plot_type, data, x_feature, y_feature=None):
    plot_functions = {
        'histogram': plot_histogram,
        'line': plot_line,
        'scatter': plot_scatter,
        'bar': plot_bar,
        'box': plot_box,
        'pie': plot_pie
    }

    if plot_type in ['histogram', 'box', 'pie']:
        return plot_functions[plot_type](data, x_feature)
    elif plot_type in ['line', 'scatter', 'bar']:
        return plot_functions[plot_type](data, x_feature, y_feature)
    else:
        return None


def plot_histogram(data, feature_name):
    """
    Create a histogram for the given feature.

    Args:
        data (pandas.DataFrame): The dataset.
            A DataFrame containing the data to be plotted.

        feature_name (str): The name of the feature.
            The name of the column in the DataFrame to plot the histogram for.

    Returns:
        str or None: JSON representation of the histogram plot, if successful.
            If the feature_name is not found in the DataFrame columns, returns None.
    """
    if feature_name in data.columns:
        fig = go.Figure(data=[go.Histogram(x=data[feature_name])])
        fig.layout.template = None

        return fig.to_json()
    else:
        return None


def plot_line(data, x_feature, y_feature):
    """
    Create a line plot for the given features.

    Args:
        data (pandas.DataFrame): The dataset.
            A DataFrame containing the data to be plotted.

        x_feature (str): The name of the feature for the x-axis.
            The name of the column in the DataFrame for the x-axis.

        y_feature (str): The name of the feature for the y-axis.
            The name of the column in the DataFrame for the y-axis.

    Returns:
        str or None: JSON representation of the line plot, if successful.
            If the x_feature or y_feature is not found in the DataFrame columns, returns None.
    """
    if x_feature in data.columns and y_feature in data.columns:
        fig = go.Figure(data=go.Scatter(x=data[x_feature], y=data[y_feature], mode='lines'))
        fig.layout.template = None

        return fig.to_json()
    else:
        return None


def plot_scatter(data, x_feature, y_feature):
    """
    Create a scatter plot for the given features.

    Args:
        data (pandas.DataFrame): The dataset.
            A DataFrame containing the data to be plotted.

        x_feature (str): The name of the feature for the x-axis.
            The name of the column in the DataFrame for the x-axis.

        y_feature (str): The name of the feature for the y-axis.
            The name of the column in the DataFrame for the y-axis.

    Returns:
        str or None: JSON representation of the scatter plot, if successful.
            If the x_feature or y_feature is not found in the DataFrame columns, returns None.
    """
    if x_feature in data.columns and y_feature in data.columns:
        fig = go.Figure(data=go.Scatter(x=data[x_feature], y=data[y_feature], mode='markers'))
        fig.layout.template = None

        return fig.to_json()
    else:
        return None


def plot_bar(data, x_feature, y_feature):
    """
    Create a bar plot for the given features.

    Args:
        data (pandas.DataFrame): The dataset.
            A DataFrame containing the data to be plotted.

        x_feature (str): The name of the feature for the x-axis.
            The name of the column in the DataFrame for the x-axis.

        y_feature (str): The name of the feature for the y-axis.
            The name of the column in the DataFrame for the y-axis.

    Returns:
        str or None: JSON representation of the bar plot, if successful.
            If the x_feature or y_feature is not found in the DataFrame columns, returns None.
    """
    if x_feature in data.columns and y_feature in data.columns:
        fig = go.Figure(data=go.Bar(x=data[x_feature], y=data[y_feature]))
        fig.layout.template = None

        return fig.to_json()
    else:
        return None


def plot_box(data, feature_name):
    """
    Create a box plot for the given feature.

    Args:
        data (pandas.DataFrame): The dataset.
            A DataFrame containing the data to be plotted.

        feature_name (str): The name of the feature.
            The name of the column in the DataFrame to plot the box plot for.

    Returns:
        str or None: JSON representation of the box plot, if successful.
            If the feature_name is not found in the DataFrame columns, returns None.
    """
    if feature_name in data.columns:
        fig = go.Figure(data=go.Box(y=data[feature_name]))
        fig.layout.template = None

        return fig.to_json()
    else:
        return None


def plot_pie(data, feature_name):
    """
    Create a pie chart for the given feature.

    Args:
        data (pandas.DataFrame): The dataset.
            A DataFrame containing the data to be plotted.

        feature_name (str): The name of the feature.
            The name of the column in the DataFrame to plot the pie chart for.

    Returns:
        str or None: JSON representation of the pie chart, if successful.
            If the feature_name is not found in the DataFrame columns, returns None.
    """
    if feature_name in data.columns:
        fig = go.Figure(data=go.Pie(labels=data[feature_name].unique(),
                                    values=data[feature_name].value_counts()))
        fig.layout.template = None

        return fig.to_json()
    else:
        return None
