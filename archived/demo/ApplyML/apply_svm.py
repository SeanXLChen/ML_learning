import streamlit as st
from streamlit_antd_components import menu
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_option_menu import option_menu
from ApplyML.apply_svm_stage import train_model
from ApplyML.apply_svm_stage import test_model
from ApplyML.apply_svm_stage import feature_importance
from ApplyML.apply_svm_stage import feature_engineering



def apply_svm(menu_column, main_column):

    # Store the selected dataset in session state
    if "dataset_chosen" not in st.session_state:
        st.session_state["dataset_chosen"] = "None"

    # left column
    with menu_column:
        st.divider()
        st.write("Dataset you selected: ")
        st.write(st.session_state["dataset_chosen"])

        st.divider()
        # download button
        text_contents = '''This is some text'''
        st.download_button('Download model config', text_contents)

    # right main column
    with main_column:
        if st.session_state.get('train_button', False):
            st.session_state['algo_menu_option'] = 1
            stage = st.session_state['algo_menu_option']
        else:
            stage = None
        algo_action_selection = option_menu(None, ["Train Model", "Test Model", "Feature Importance", "Feature Engineering"], 
                                            default_index=0,
                                            orientation="horizontal",
                                            manual_select=stage)
        st.session_state["algo_action_selection"] = algo_action_selection
        
        if algo_action_selection == "Train Model":
            train_model()
        elif algo_action_selection == "Test Model":
            test_model()
        elif algo_action_selection == "Feature Importance":
            feature_importance()
        elif algo_action_selection == "Feature Engineering":
            feature_engineering()
