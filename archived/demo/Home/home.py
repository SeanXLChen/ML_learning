# Landing page. The first page when user enter the website. will call home_main()

import streamlit as st
from Home.principles import principles
from streamlit_option_menu import option_menu
from LearnML.learn_ml_main import learn_ml_algorithms_main


st.session_state["principle_button"] = False

def home_main():
    def principle_callback():
        st.session_state["principle_button"] = not st.session_state["principle_button"]

    def learn_algorithms_callback():
        st.session_state['learn_algo_button'] = True

    def apply_algorithms_callback():
        st.session_state['apply_algo_button'] = True

    # nav to the princple page
    if st.session_state["principle_button"]:
        principles()
    else:
        col1, col2, col3 = st.columns([0.15, 0.7, 0.15])
        with col2:
            st.title("Machine Learning Dashboard")
            st.image("res/home_background_placeholder.jpg",
                     use_column_width=True)
            subcol = st.columns([0.02, 0.28, 0.05, 0.28, 0.05, 0.28, 0.02])

            def local_css(file_name):
                with open(file_name) as f:
                    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

            local_css("css/home.css")

            with subcol[1]:
                # st.markdown(format_heading("Machine Learning Basics"), unsafe_allow_html=True)
                # st.markdown(format_text("New to machine learning? No worries! This section will walk you through the basics. Discover what machine learning is, how it works, and get a clear picture of its workflow."), unsafe_allow_html=True)

                # This mark down for buttons do no work. Need to find a way to make it work
                # st.markdown("""<div style="display: flex; justify-content: flex-end; align-items: center; alignt-content: flex-end margin: 5px">""", unsafe_allow_html=True)
                st.button(
                    label="# MACHINE LEARNING BASICS \n New to machine learning? No worries! This section will walk you through the basics. Discover what machine learning is, how it works, and get a clear picture of its workflow.",
                    on_click=principle_callback,
                )
                st.markdown("""</div>""", unsafe_allow_html=True)
            with subcol[3]:
                # st.markdown(format_heading("Learn Algorithms"), unsafe_allow_html=True)
                # st.markdown("Let's dive deeper into the different types of machine learning algorithms. We'll also discuss the pros and cons of each algorithm, and walk through an example on how to apply them.", unsafe_allow_html=True)
                st.button(
                    label="# LEARN ALGORITHMS \n Let's dive deeper into the different types of machine learning algorithms. We'll also discuss the pros and cons of each algorithm, and walk through an example on how to apply them.",
                    on_click=learn_algorithms_callback,
                )
            with subcol[5]:
                # st.markdown(format_heading("Apply Algorithms"), unsafe_allow_html=True)
                # st.markdown(format_text("Apply the algorithms you have learned to real-world data. Experiment with your own datasets with different algorithms in this open playground."), unsafe_allow_html=True)
                st.button(
                    label="# APPLY ALGORITHMS \n Apply the algorithms you have learned to real-world data. Experiment with your own datasets with different algorithms in this open playground.",
                    on_click=apply_algorithms_callback,
                )


def format_heading(heading):
    return f"""<div style="text-align: center; margin: 5px"><h3>{heading}</h3></div>"""


def format_text(text):
    return f"""<div style="text-align: justify; margin: 5px">{text}</div>"""
