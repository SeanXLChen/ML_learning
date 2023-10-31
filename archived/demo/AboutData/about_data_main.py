'''
EDA page. When user select EDA->EDA Introduction, will call eda_main()
'''
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_antd_components import menu

# Importing necessary modules for exploratory data analysis (EDA)
from AboutData.import_data import import_data_main
from AboutData.understand_data import understand_data_main
from AboutData.clean_data import clean_data_main
from AboutData.visualize_data import visualize_data_main
from AboutData.analyze_data import analyze_data_main
from utils.generate_menu import generate_menu


def select_eda_menu(menu_strings):
    """
    Selects an option from the EDA menu and displays the corresponding content.

    Parameters:
        menu_strings (list): A list of strings representing the EDA menu options.

    Returns:
        None
    """

    # Split the layout into two columns: menu_col and main_col
    menu_col, main_col = st.columns([1, 4])

    with menu_col:
        add_vertical_space(5)

        # Generate menu options based on the provided menu_strings
        menu_options = generate_menu(menu_strings)
        eda_menu_selection = menu(menu_options, format_func='title', open_all=True)
        
        # Store the selected menu option in session state
        st.session_state['eda_menu_selection'] = eda_menu_selection

        # Check the selected menu option and display the corresponding content in main_col
        if eda_menu_selection == menu_strings[0]:
            display_eda_background(main_col)
        elif eda_menu_selection == menu_strings[1]:
            import_data_main(main_col)
        elif eda_menu_selection == menu_strings[2]:
            understand_data_main(main_col)
        elif eda_menu_selection == menu_strings[3]:
            clean_data_main(main_col)
        elif eda_menu_selection == menu_strings[4]:
            visualize_data_main(main_col)
        elif eda_menu_selection == menu_strings[5]:
            analyze_data_main(main_col)


def display_eda_background(column):
    """
    Displays the background information about Exploratory Data Analysis (EDA) in the specified column.

    Parameters:
        column: The Streamlit column to display the content in.

    Returns:
        None
    """
    with column:
        st.title("Exploratory Data Analysis")
        st.divider()

        # Background information about EDA
        EDA_text = """
        Exploratory Data Analysis (EDA) is a technique used in data science and machine
        learning to gain insights into the structure and nature of the data before building a
        model. It involves a series of techniques and tools for exploring, visualizing, and
        summarizing the data to identify patterns, relationships, and potential problems.


        The main goal of EDA is to get a sense of the data, including its distribution, central
        tendency, and variability, as well as any relationships or correlations between variables.
        EDA helps to identify outliers, missing values, and other anomalies that can affect the
        quality of the analysis and model performance.
        """

        st.text(EDA_text)
        st.divider()


def eda_main():
    eda_menu_strings = ['Intro to EDA', 'Import Data', 'Understand Data', 
                        'Clean Data', 'Visualize Data', 'Analyze Data']
    
    select_eda_menu(eda_menu_strings)
        
        