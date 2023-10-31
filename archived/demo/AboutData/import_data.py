'''
Dataset Settings page. When user select EDA->Import Data, will call import_data_main()
'''
import os
import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris, load_wine, load_breast_cancer
from streamlit_extras.add_vertical_space import add_vertical_space


def select_data():
    """
    Selects a dataset from the selectbox.

    Parameters:
        No parameters are required.

    Returns:
        str: The name of the selected dataset.
    """
    dataset_name = st.selectbox("Dataset", ("Iris", "Wine", "Breast Cancer"))
    return dataset_name


def convert_to_pandasdataframe(dataset):
    """
    Convert a dataset to a Pandas DataFrame object.

    Parameters:
        dataset (sklearn.utils.Bunch): A dataset object from the Sklearn.datasets.

    Returns:
        pandas.DataFrame: A Pandas DataFrame object of the dataset.
    """
    dataframe = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
    return dataframe


@st.cache_data(persist=True)
def load_dataset(dataset_name):
    """
    Function --- load_dataset
        Loads the selected dataset.
    
    Parameters:
        dataset_name (str): The name of the dataset.
    
    Returns
        pandas.DataFrame: The loaded dataset as a Pandas DataFrame.
    """
    if dataset_name == "Iris":
        dataset = load_iris()
    elif dataset_name == "Wine":
        dataset = load_wine()
    elif dataset_name == "Breast Cancer":
        dataset = load_breast_cancer()
    
    dataframe = convert_to_pandasdataframe(dataset)

    return dataframe

def load_feature_names(dataset_name):
    if dataset_name == "Iris":
        dataset = load_iris()
    elif dataset_name == "Wine":
        dataset = load_wine()
    elif dataset_name == "Breast Cancer":
        dataset = load_breast_cancer()
    
    feature_names = dataset.feature_names
    return feature_names

def display_description(dataset_name):
    """
    Function --- display_description
        Displays tje description of a dataset.
    
    Parameters:
        dataset_name (str): The name of the dataset.
    
    Returns:
        str: The description of the dataset.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    description_folder = os.path.join(current_dir, "description")

    description_file = os.path.join(description_folder, f"{dataset_name}_description.txt")

    with open(description_file, "r") as file:
        description = file.read()
    return description

def import_data_main(column):
    with column:
        st.title("Import Data")

        
        col1, col2, col3 = st.columns(3, gap="large")

        # This column gives the user a selectbox to choose the dataset
        with col1:
            dataset_name = select_data()
        
        # This column has a button to display dataset description
        with col2:
            description_button = st.button("Dataset Description")
            

        # This column has a button to preview all features in the dataset
        with col3:
            feature_button = st.button("Feature Preview")

        st.divider()

        # After the user selects a dataset
        if 'dataset_name' not in st.session_state:
            st.session_state['dataset_name'] = None

        if dataset_name != st.session_state.get('dataset_name'):
            st.session_state['dataset_name'] = dataset_name
            st.session_state['description_button'] = 0
        
        dataset = load_dataset(dataset_name)
        feature_names = load_feature_names(dataset_name)
        if 'dataset' not in st.session_state:
            st.session_state['dataset'] = dataset
        st.write(dataset)
        
        if 'feature_names' not in st.session_state:
            st.session_state['feature_names'] = feature_names

        # If the "Dataset Description" Button is clicked
        if 'description_button' not in st.session_state:
            st.session_state['description_button'] = 0
        
        if 'preview_button' not in st.session_state:
            st.session_state['preview_button'] = 0
        
        if description_button:
            st.session_state['description_button'] +=1

            if st.session_state['description_button'] % 2 != 0:
                st.write(display_description(dataset_name))
        
        # The feature button has not worked yet
        if feature_button:
            st.write("Display Feature Preview")