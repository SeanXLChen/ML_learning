"""
This file provided the EDA page in Streamlit framework, which is not included in the current requirements.txt file.
If you want to run this file, please install the Streamlit framework first.
"""

import streamlit as st
from utils.process_dataset import load_dataset, get_target_column
import visualizations.visualizations as visualize
import json


def main():
    st.title("EDA Dashboard")

    # Sidebar controls
    dataset_name = st.sidebar.selectbox("Select Dataset", ['breast cancer wisconsin', 'penguins size', 'ionosphere'])
    plot_type = st.sidebar.selectbox("Select Plot Type", ["histogram", "line", "scatter", "bar", "box", "pie"])

    # Load dataset and show preview
    data = load_dataset(dataset_name)
    target_column = get_target_column(dataset_name)
    st.write("### Dataset Preview")
    st.write(data.head())

    # User selects features
    features = st.multiselect("Select features for plotting", data.columns.tolist(), [target_column])

    # Plot the data
    if len(features) >= 1:
        if plot_type in ["histogram", "box", "pie"]:
            plot_feature = st.selectbox("Select a feature for the plot", features)
            plot_json = visualize.plot_data(plot_type, data, plot_feature)
        else:
            x_feature = st.selectbox("Select feature for X-axis", features)
            y_feature = st.selectbox("Select feature for Y-axis", features)
            plot_json = visualize.plot_data(plot_type, data, x_feature, y_feature)

        if plot_json is not None:
            st.write("### Visualization")
            st.plotly_chart(json.loads(plot_json))


if __name__ == "__main__":
    main()
