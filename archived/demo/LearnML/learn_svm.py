import streamlit as st
from streamlit_option_menu import option_menu
import LearnML.svm_background as svmb
from LearnML.svm_algo_action import algo_action_main
import pandas as pd


def svm_background_main():
    manual_select = None
    svm_background_selection = option_menu(None,
                                           ["What it is", "Use Cases",
                                            "Pros & Cons", "What is Kernel", "How hyperplane works"],
                                           default_index=0,
                                           orientation="horizontal",
                                           manual_select=manual_select)
    st.session_state['svm_background_selection'] = svm_background_selection

    if svm_background_selection == "What it is":
        svmb.svm_background_what_it_is()
    elif svm_background_selection == "Use Cases":
        svmb.svm_background_use_cases()
    elif svm_background_selection == "Pros & Cons":
        svmb.svm_background_pros_and_cons()
    elif svm_background_selection == "What is Kernel":
        svmb.svm_background_what_is_kernel()
    elif svm_background_selection == "How hyperplane works":
        svmb.svm_background_how_hyperplane_works()


def use_cases_main():
    st.write("Note: this section can reuse functionality from RJ's EDA")
    dataset_selection = st.selectbox(
        "Select dataset", ["Dataset from EDA", "Iris", "Wine", "Breast Cancer"])

    st.write("## Case Story")
    titanic_story = """The sinking of the Titanic is one of the most infamous shipwrecks in history. On April 15, 1912, 
    during her maiden voyage, the widely considered “unsinkable” RMS Titanic sank after colliding with an iceberg. 
    Unfortunately, there weren’t enough lifeboats for everyone onboard, resulting in the death of 1502 out of 2224 passengers and crew. 
    While there was some element of luck involved in surviving, it seems some groups of people were more likely to survive than others.
    In this project, the task is to build a predictive model that answers the question: 
    “what sorts of people were more likely to survive?” using passenger data (ie name, age, gender,
    socio-economic class, etc).')
    """

    train_data = pd.read_csv("datasets/train.csv")
    st.write(titanic_story)

    st.write("## Data Details")

    st.write("### Description")
    st.write(train_data.describe())

    st.write("### Head")
    st.write(train_data.head())

    st.write("### Tail")
    st.write(train_data.tail())

    st.write("## Data Visualization")
    st.bar_chart(train_data, x="Age", y="Survived")


def learn_svm(menu_column, main_column):
    with menu_column:
        learn_svm_selection = option_menu(None, ["Background", "Cases & Data Understanding", "Algorithm in Action"],
                                          default_index=0)
    with main_column:
        if learn_svm_selection == "Background":
            svm_background_main()
        elif learn_svm_selection == "Cases & Data Understanding":
            use_cases_main()
        elif learn_svm_selection == "Algorithm in Action":
            algo_action_main()
