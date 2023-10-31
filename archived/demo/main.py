'''
Main entrance for Educative ML Dashboard, which contains sidebar menu logic
calling each page's main function.
'''
import streamlit as st
from streamlit_option_menu import option_menu

from Home.home import home_main
from AboutData.about_data_main import eda_main
from LearnML.learn_ml_main import learn_ml_algorithms_main
from ApplyML.apply_ml_techniques import apply_techniques_main

def set_page_config():
    """
    Configures the page settings for the Streamlit application.

    Parameters:
        None

    Returns:
        None
    """
    st.set_page_config(page_title="Educative Machine Learning Dashboard",
                       page_icon="book",
                       layout="wide",
                       initial_sidebar_state="collapsed")


def on_change(key):
    """
    Retrieves the value of a session state variable based on the provided key.

    Parameters:
        key (str): The key of the session state variable.

    Returns:
        Any: The value of the session state variable.
    """
    selection = st.session_state[key]


def dashboard_controller():
    if st.session_state.get('learn_algo_button', False):
        st.session_state['main_menu_option'] = 2
        st.session_state['learn_algo_button'] = False
        main_manual_select = st.session_state['main_menu_option']
    elif st.session_state.get('apply_algo_button', False):
        st.session_state['main_menu_option'] = 3
        st.session_state['apply_algo_button'] = False
        main_manual_select = st.session_state['main_menu_option']
    elif st.session_state.get('eda_button', False):
        st.session_state['main_menu_option'] = 1
        st.session_state['eda_button'] = False
        main_manual_select = st.session_state['main_menu_option']
    else:
        main_manual_select = None
    main_menu_selection = option_menu(None, ['Home', 'All About Data', 'Learn Algorithms', 'Apply Algorithms'],
                            icons = ['house', 'bar-chart-fill', 'card-checklist', 'tools'],
                            menu_icon="cast", default_index=0, orientation="horizontal",
                            on_change=on_change, key='main_menu', manual_select = main_manual_select,
                            styles={
                                "container": {"padding": "0!important", "background-color": "black"},
                                "icon": {"color": "orange", "font-size": "25px"}, 
                                "nav-link": {"font-size": "20px", "text-align": "center", "margin":"0px", "--hover-color": "#333333"},
                                "nav-link-selected": {"background-color": "#128bb5", "font-size": "20px", "text-align": "center", "margin":"0px", "--hover-color": "darkgray"},
                                }
                            )

    if main_menu_selection == 'Home':
        home_main()
    elif main_menu_selection == 'All About Data':
        eda_main()
    elif main_menu_selection == 'Learn Algorithms':
        learn_ml_algorithms_main()
    elif main_menu_selection == 'Apply Algorithms':
        apply_techniques_main()


def main():
    set_page_config()
    dashboard_controller()


if __name__ == "__main__":
    main()
