# This should be the page that appears after clicking on "ML Basics" on the homepage.

import streamlit as st
# from Globals.globals import globals_dict


def learn_algorithms_callback():
    st.session_state['learn_algo_button'] = True
    return_callback()


def apply_algorithms_callback():
    st.session_state['apply_algo_button'] = True
    return_callback()


def eda_callback():
    st.session_state['eda_button'] = True
    return_callback()

def return_callback():
    st.session_state["principle_button"] = not st.session_state["principle_button"]

def principles():



    col1, col2, col3 = st.columns([1, 8, 1])
    with col2:
        st.button(label="Go back",
                  on_click=return_callback,
                  key="return")
        st.title("Machine Learning Principles")
        st.subheader("What is Machine Learning")
        st.markdown("The term machine learning was first coined in the 1950s when Artificial Intelligence pioneer Arthur Samuel built the first self-learning system for playing checkers. He noticed that the more the system played, the better it performed."
                    "Fueled by advances in statistics and computer science, as well as better datasets and the growth of neural networks, machine learning has truly taken off in recent years."
                    "Today, whether you realize it or not, machine learning is everywhere ‒ automated translation, image recognition, voice search technology, self-driving cars, and beyond.")
        st.markdown("Machine learning is a subset of artificial intelligence (AI) that focuses on developing algorithms and models that enable computers to learn and make predictions or decisions without being explicitly programmed. It involves the use of statistical techniques and data to train algorithms, allowing them to improve their performance over time through experience."
                    "In traditional programming, humans write explicit instructions that tell computers how to perform specific tasks. However, in machine learning, computers learn from patterns and examples found in data, and then use this learned knowledge to make predictions or decisions on new, unseen data.")
        st.text("")
        st.subheader("Machine Learning Pipeline")
        st.markdown("Machine learning follows an iterative workflow or pipeline"
                    "that includes stages such as data collection, preprocessing,"
                    "feature engineering, model selection, training, evaluation, and deployment:")

        button1, button2, button3, margin = st.columns([1, 1, 1, .7])
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

        local_css("css/principles.css")


        with button1:
            st.button(
                label="# All About Data",
                on_click=eda_callback,
            )
        with button2:
            st.button(label="# Learn Algorithms",
                      on_click=learn_algorithms_callback)
        with button3:
            st.button(label="# Apply Algorithms",
                      on_click=apply_algorithms_callback)

        st.image("res/ml_pipeline.jpg", use_column_width=True)

        st.text("")
        st.subheader("Data Exploration and Preprocessing")
        st.markdown("This combined step involves both Exploratory Data Analysis (EDA) and Data Preprocessing tasks."
                    "Initially, the data is explored through EDA techniques, such as visualizations, statistical"
                    "summaries, and correlation analysis, to gain insights into the dataset's structure, patterns,"
                    "and relationships between variables. During this process, missing values, outliers, and other"
                    "data quality issues can be identified. Subsequently, the data is preprocessed by handling missing"
                    "values, addressing outliers, performing feature scaling or normalization, encoding categorical"
                    "variables, and splitting the data into training and testing sets.")

        st.text("")
        st.subheader("Model Build")
        st.markdown("Once the data has been explored and preprocessed, the next step is to select an appropriate machine learning algorithm based on the problem and the available data. Various algorithms can be considered, such as linear regression, decision trees, random forests, support vector machines (SVM), or neural networks.")

        st.text("")
        st.subheader("Model Evaluation and Training")
        st.markdown("The selected algorithm is then trained using the preprocessed training data, involving the optimization of algorithm parameters to minimize the difference between predicted and actual outputs.After training the model, it is evaluated to assess its performance and generalization abilities. Evaluation metrics, such as accuracy, precision, recall, and F1 score, are used to measure how well the model performs on unseen data. The model is tested on the preprocessed testing data to evaluate its effectiveness.")
