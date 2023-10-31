'''
This is the landing page for apply machine learning techniques.
'''
import streamlit as st
from streamlit_antd_components import menu
from streamlit_extras.add_vertical_space import add_vertical_space
from ApplyML.apply_svm import apply_svm
import pandas as pd

# this is the main function for Apply page
def apply_techniques_main():
    # Create a container for the top section of the page
    top_container = st.container()

    # Create a container for the bottom section of the page
    bottom_container = st.container()

    # Split the bottom container into two columns: menu_col and main_col
    menu_col, main_col = bottom_container.columns([1, 4])

    algorithm_selection = menu_col.selectbox("Select algorithm:", ['Support Vector Machine', 'Random Forest', 'Decision Trees'], label_visibility="visible")

    if algorithm_selection == 'Support Vector Machine':
        apply_svm(menu_col, main_col)
