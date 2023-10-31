import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.toggle_switch import st_toggle_switch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, KFold
from sklearn import svm
from sklearn.feature_selection import SelectPercentile, f_classif

from utils.svm_train_model import svm_train_main

def select_data():
    """
    Selects a dataset from the selectbox.

    Returns:
        str: The name of the selected dataset.
    """
    if 'dataset_name' not in st.session_state:
        st.session_state['dataset_name'] = None

    dataset_name = st.selectbox(
                        "Select the dataset", 
                        ["---", "Iris", "Wine", "Breast Cancer"]
                    )
    
    if dataset_name != st.session_state.dataset_name:
        st.session_state.dataset_name = dataset_name
    
    return dataset_name

def select_kernel():
    """
    Presents a selectbox to the user for kernel selection for machine learning algorithms.

    Returns:
        str: The name of the selected kernel. Options are "Linear", "Polynomial",
             or "Gaussian Radial Basis Function (RBF)".
    """
    if 'kernel_type' not in st.session_state:
        st.session_state['kernel_type'] = None

    dataset_name = st.session_state.dataset_name

    if dataset_name is None or dataset_name == "---":
        kernel_disability = True
    else:
        kernel_disability = False
    
    kernel_helper = """A kernel is a function that defines the similarity between pairs of 
    data points in a higher-dimensional space."""

    kernel_type = st.selectbox(
                        "Select the kernel type", 
                        ["---", "linear", "poly", "rbf"], 
                        help = kernel_helper,
                        disabled = kernel_disability
                    )
    
    if kernel_type != st.session_state.kernel_type:
        st.session_state.kernel_type = kernel_type
    return kernel_type


def set_margin():
    """
    Adjusts the margin parameter C based on the selected kernel.

    Returns:
        float: The adjusted margin parameter value.
    """
    if 'margin_value' not in st.session_state:
        st.session_state['margin_value'] = None

    dataset_name = st.session_state.dataset_name
    kernel_type = st.session_state.kernel_type    
    
    margin_helper = """The margin parameter (C) determines the trade-off between maximizing 
    the margin (distance) between the decision boundary and the training samples and minimizing 
    the training errors."""
    
    if (dataset_name is None or dataset_name == "---" or 
        kernel_type is None  or kernel_type == "---"):
        margin_disability = True
    else:
        margin_disability = False
    
    margin_value = st.number_input(
                    "Set the margin parameter (C)",
                    value=1.0,
                    min_value = 0.1,
                    max_value = 10000.0, 
                    step = 0.1,
                    help = margin_helper,
                    disabled = margin_disability
                    )
    
    if margin_value != st.session_state.margin_value:
        st.session_state.margin_value = margin_value
    
    return margin_value


def set_gamma():
    """
    Adjusts the gamma value based on the selected kernel.

    Returns:
        float: The adjusted gamma value.
    """
    if 'gamma_value' not in st.session_state:
        st.session_state['gamma_value'] = None

    kernel_type = st.session_state.kernel_type  
    
    gamma_helper = """The gamma parameter (γ) determines the model's influence and can significantly impact 
    the decision boundary's flexibility."""

    if (kernel_type is None  or kernel_type == "---" or kernel_type == "linear"):
        gamma_disability = True
    else:
        gamma_disability = False

    gamma_value = st.number_input(
                        "Set the Gamma (γ)", 
                        value=1.0,
                        min_value = 0.0, 
                        max_value = 10.0, 
                        step = 0.1, 
                        help = gamma_helper,
                        disabled = gamma_disability
                    )
    
    if gamma_value != st.session_state.gamma_value:
        st.session_state.gamma_value = gamma_value
    return gamma_value


def set_coefficient():
    """
    Adjusts the coefficient value based on the selected kernel.

    Returns:
        float: The adjusted coefficient value.
    """
    if 'coefficient_value' not in st.session_state:
        st.session_state['coefficient_value'] = None

    kernel_type = st.session_state.kernel_type    
    
    if (kernel_type is None or kernel_type == "---" or kernel_type == "linear"):
        coefficient_disability = True
    else:
        coefficient_disability = False

    coefficient_helper = """The coefficient parameter (r) refers to an additional constant term in 
    the polynomial kernel function used to transform the input data."""

    coefficient_value = st.number_input(
                            "Set the coefficient (r)", 
                            value=0.0,
                            min_value = -1.0,
                            max_value = 1.0,
                            step = 0.01, 
                            help = coefficient_helper,
                            disabled = coefficient_disability,
                        )
    
    if coefficient_value != st.session_state.coefficient_value:
        st.session_state.coefficient_value = coefficient_value
    return coefficient_value


def set_degree():
    """
    Adjusts the degree value based on the selected kernel.

    Returns:
        int: The adjusted degree value.
    """
    if "degree_value" not in st.session_state:
        st.session_state['degree_value'] = None
    
    kernel_type = st.session_state.kernel_type
    if kernel_type == "poly":
        degree_disability = False
    else:
        degree_disability = True
    
    degree_helper = """The degree parameter (d) in the polynomial kernel function controls the 
    nonlinearity of the polynomial transformation applied to the data. """

    degree_value = st.number_input(
                        "Set the degree (d)",
                        value=3,
                        min_value = 1,
                        max_value = 10,
                        step = 1,
                        help = degree_helper,
                        disabled = degree_disability 
                    )
    if degree_value != st.session_state.degree_value:
        st.session_state.degree_value = degree_value
    return degree_value


def split_train_and_test():
    """
    Split the dataset into train and test sets based on the selected split method.

    Returns:
        str: The selected split method ("K-Fold Cross-Validation" or "Repeated Sub-Sampling").
    """
    if 'split_method' not in st.session_state:
        st.session_state['split_method'] = None
    if 'k_value' not in st.session_state:
        st.session_state['k_value'] = 5
    if 'train_percentage' not in st.session_state:
        st.session_state['train_percentage'] = 70.0
    
    dataset_name = st.session_state.dataset_name
    kernel_type = st.session_state.kernel_type

    if (dataset_name is None or dataset_name == "---" or 
        kernel_type is None or kernel_type == "---"):
        split_method_disability = True
    else:
        split_method_disability = False
    
    split_method = st.radio(
                    "Train / Test Techniques", 
                    ("K-Fold Cross-Validation",
                     "Repeated Sub-Sampling"),
                     disabled = split_method_disability, 
                    label_visibility = 'hidden'
                    )
    if split_method == "Repeated Sub-Sampling":
            train_percentage = st.number_input(
                                    "Enter the percentage of train",
                                    min_value = 0.0,
                                    max_value = 100.0,
                                    value = 70.0,
                                    disabled = split_method_disability  
                                )
            st.session_state.train_percentage = train_percentage
            st.session_state.k_value = None

    elif split_method == "K-Fold Cross-Validation":
        k_value = st.number_input(
                                "Enter the number of K", 
                                min_value = 2,
                                max_value = 10, 
                                value = 5, 
                                disabled = split_method_disability
                            )
        st.session_state.train_percentage = None
        st.session_state.k_value = k_value
    
    if split_method != st.session_state.split_method:
        st.session_state.split_method = split_method
    
    return split_method


def interactive_helper():
    with st.expander("Interactive Helper"):
        st.write("""
                1. Click the dataset from the exploratory data analysis (EDA) or select one from the dropdown menu.
                2. Select the sample size, noise level, and threshold values to customize your training setup.
                3. Choose the kernel function for your model and adjust the settings for cost, degree, and gamma.
                You can also enable or disable shrinking based on your preference.
                4. Once you have configured the desired parameters, click the train button to initiate the training process.
        """)

def switch_interactive_helper():
    interactive_helper_switch = st_toggle_switch(
                                    label = "Needs some helps?",
                                    default_value= False,
                                    inactive_color="#D3D3D3",  # optional
                                    active_color="#11567f",  # optional
                                    track_color="#29B5E8",  # optional
                                    )
    
    if interactive_helper_switch:
        st.write("""
                1. Click the dataset from the exploratory data analysis (EDA) or select one from the dropdown menu.
                2. Select the sample size, noise level, and threshold values to customize your training setup.
                3. Choose the kernel function for your model and adjust the settings for cost, degree, and gamma.
                You can also enable or disable shrinking based on your preference.
                4. Once you have configured the desired parameters, click the train button to initiate the training process.
        """)  

def algo_train():
    algo_train_col1, algo_train_col2 = st.columns([1, 2])

    with algo_train_col1:
        st.subheader("Data Setting")
        dataset_name = select_data()
        algo_train_col1.divider()

        st.subheader("Parameters Tunning")
        kernel_type = select_kernel()
        margin_value  = set_margin()

        gamma_value = set_gamma()
        coefficient_value = set_coefficient()
        degree_value = set_degree()
        algo_train_col1.divider()

        st.subheader("Train / Test Techniques")
        split_method = split_train_and_test()
        
        button_train = algo_train_col1.button(
                                            "Train", 
                                            key="train_button"
                                        )

    with algo_train_col2:
        interactive_helper()
        switch_interactive_helper()
        st.write(st.session_state)

def algo_test():
    # To avoid unstable button callback, simply check the session_state for the "train_button"
    # If its true, run the click_train_button()
    if st.session_state.get('train_button', False):
        svm_train_main()
    st.write(st.session_state)
    return


def algo_feature_manipulation():
    col1, col2, col3 = st.columns([3, 1, 3])

    col1.subheader("Available Features")

    features_list = ["Utque erectos", "Secrevit ponderib...", "Capacius"]

    features_list_unadded = features_list
    available_feature = col1.selectbox(
        "Available Features", features_list_unadded)
    available_df = pd.DataFrame({"Feature": features_list_unadded})
    col1.dataframe(available_df)

    col3.subheader("Selected Features")
    features_list_added = filter(
        lambda x: x != features_list_unadded, features_list)
    selected_feature = col3.selectbox("Selected Features", {})
    features_list_df = pd.DataFrame({"Feature": {}})
    col3.dataframe(features_list_df)

    with col2:
        add_vertical_space(10)
    add_feature = col2.button(
        "Add Feature", features_list_unadded.remove(available_feature))
    remove_feature = col2.button("Remove Feature")


def algo_action_main():
    if st.session_state.get('train_button', False):
        st.session_state['algo_menu_option'] = 1
        manual_select = st.session_state['algo_menu_option']
    else:
        manual_select = None
    algo_action_selection = option_menu(None, ["Train Model", "Test Model", "Feature Manipulation"],
                                        default_index=0,
                                        orientation="horizontal",
                                        manual_select=manual_select)
    st.session_state["algo_action_selection"] = algo_action_selection
    if algo_action_selection == "Train Model":
        ## The following line which are commented out are for showing different arrangement of the interactive helper
        # interactive_helper()
        algo_train()
        # interactive_helper()

    elif algo_action_selection == "Test Model":
        algo_test()
    elif algo_action_selection == "Feature Manipulation":
        algo_feature_manipulation()

