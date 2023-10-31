'''
This is the landing page for learn ml algorithms.
'''
import streamlit as st
from LearnML.learn_svm import learn_svm
from streamlit_option_menu import option_menu

def learn_ml_algorithms_main():

    if "svm_button" not in st.session_state:
        st.session_state["svm_button"] = False
    
    def svm_callback():
        st.session_state["svm_button"] = True

    def back_learn_ml_main():
        st.session_state["svm_button"] = False

    if st.session_state["svm_button"]:
        menu_col, main_col = st.columns([1, 4])
        menu_col.button(label="Go back",
                    on_click=back_learn_ml_main,
                    key="return")
        algorithm_selection = menu_col.selectbox("Select algorithm:", ['Support Vector Machine', 'Random Forest', 'Decision Trees'])
        if algorithm_selection == 'Support Vector Machine':
            learn_svm(menu_col, main_col)

    else:
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

        local_css("css/learn.css")

        col1, col2, col3 = st.columns([0.15, 0.7, 0.15])
        with col2:
            st.title("Learn Algorithms")
            st.image("res/learn_algo_placeholder.jpg", use_column_width=True)
            subcol = st.columns([0.02, 0.35, 0.02, 0.35, 0.02, 0.35, 0.02])

            with subcol[1]:
                # st.markdown(format_heading("Support Vector Machine"), unsafe_allow_html=True)
                # st.markdown(format_text("Support Vector Machines (SVM) is a powerful machine learning algorithm used for classification and regression tasks. It finds a boundary, called a hyperplane, that separates different classes by maximizing the margin between them. SVM is known for its ability to handle complex datasets, generalize well to unseen data, and has applications in diverse fields like image recognition and text classification."), unsafe_allow_html=True)
                # This mark down for buttons do no work. Need to find a way to make it work
                # st.markdown("""<div style="display: flex; justify-content: flex-end; align-items: center; alignt-content: flex-end margin: 5px">""", unsafe_allow_html=True)
                st.button(
                    label="# SUPPORT VECTOR MACHINE \n Support Vector Machines (SVM) is a powerful machine learning algorithm used for classification and regression tasks. It finds a boundary, called a hyperplane, that separates different classes by maximizing the margin between them. SVM is known for its ability to handle complex datasets, generalize well to unseen data, and has applications in diverse fields like image recognition and text classification.",
                    on_click=svm_callback,
                    key="svm",
                    )
                st.markdown("""</div>""", unsafe_allow_html=True)
            with subcol[3]:
                # st.markdown(format_heading("Random Forest"), unsafe_allow_html=True)
                # st.markdown("Random Forest is a machine learning algorithm that combines multiple decision trees to make predictions. It works by constructing a multitude of trees and aggregating their predictions to arrive at a final result. Random Forest is known for its versatility, accuracy, and ability to handle large and complex datasets, making it a popular choice for tasks like classification and regression in various domains.", unsafe_allow_html=True)
                st.button(
                    label="# RANDOM FOREST \n Random Forest is a machine learning algorithm that combines multiple decision trees to make predictions. It works by constructing a multitude of trees and aggregating their predictions to arrive at a final result. Random Forest is known for its versatility, accuracy, and ability to handle large and complex datasets, making it a popular choice for tasks like classification and regression in various domains.",
                    on_click=None,
                    key="random_forest",
                    )
            with subcol[5]:
                # st.markdown(format_heading("Decision Trees"), unsafe_allow_html=True)
                # st.markdown(format_text("Decision trees is a machine learning algorithm used for both classification and regression tasks. The tree consists of nodes that represent specific features and branches that represent the possible outcomes or decisions. By repeatedly splitting the data based on different features, decision trees can make predictions or classify new instances. Decision trees are known for their interpretability and ease of understanding."), unsafe_allow_html=True)
                st.button(
                    label="# DECISION TREES \n Decision trees is a machine learning algorithm used for both classification and regression tasks. The tree consists of nodes that represent specific features and branches that represent the possible outcomes or decisions. By repeatedly splitting the data based on different features, decision trees can make predictions or classify new instances. Decision trees are known for their interpretability and ease of understanding.",
                    on_click=None,
                    key="decision_tree",
                    )
            
    
            
def format_heading(heading):
    return f"""<div style="text-align: center; margin: 5px"><h3>{heading}</h3></div>"""


def format_text(text):
    return f"""<div style="text-align: justify; margin: 5px">{text}</div>"""
