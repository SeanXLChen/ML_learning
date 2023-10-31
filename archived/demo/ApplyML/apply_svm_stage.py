import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_antd_components import menu
from streamlit_extras.add_vertical_space import add_vertical_space

def train_model():
    # monitor if user uploads dataset already
    if st.session_state.get('dataset_chosen', False):
        st.session_state['dataset_chosen'] = st.session_state.get('dataset_chosen', "None")
    else:
        st.session_state['dataset_chosen'] = "None"

    if st.session_state["dataset_chosen"] == "None":
        st.write("How do you like to upload dataset?")
        add_vertical_space(2)
        st.write("Choose from available datasets:")
        st.selectbox("Choose dataset", ["None", "Iris", "Breast Cancer", "Wine"], key="dataset_chosen")
        add_vertical_space(2)
        st.write("Upload your own dataset:")
        st.file_uploader("Upload dataset", type=["csv", "txt"], key="dataset_upload")
        add_vertical_space(2)
        st.write("Upload dataset from URL:")
        st.text_input("Enter URL", key="dataset_url")
        st.button("Load", key="dataset_url_load")
        add_vertical_space(2)
        st.button("Submit", key="dataset_submit")
    else: 
        train1, train2 = st.columns([1, 2])
        st.button("Train Model", key="train_button")
    

def test_model():
    pass

def feature_importance():
    st.write("Feature Importance")

def feature_engineering():
    st.write("Feature Engineering")