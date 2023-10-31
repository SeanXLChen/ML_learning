'''
Data Preparation page. When user select EDA->Understand Data, will call understand_data_main()
'''
import streamlit as st
import pandas as pd
from streamlit_extras.add_vertical_space import add_vertical_space

def understand_data_main(column):
    with column:
        st.title("Understand Data")

        context_container = st.container()

        with context_container:
            st.header("How to quickly understand the data?")
            st.text("1. head and tail")
            st.text("2. shape and info")
            st.text("3. describe")

        st.divider()
        button_col, display_col = st.columns([1, 3])

        with button_col:
            head_and_tail_button = st.button("Head & Tail")
            add_vertical_space(2)
            shape_and_info_button = st.button("Shape & Info")
            add_vertical_space(2)
            describe_button = st.button("Describe")
        
        with display_col:
            if "head_and_tail_button" not in st.session_state:
                st.session_state['head_and_tail_button'] = 0
            
            if head_and_tail_button:
                st.session_state['head_and_tail_button'] +=1
                if st.session_state['head_and_tail_button'] %2 != 0:
                    data = st.session_state['dataset']
                    st.write("The following is the head of this data")
                    st.code("data.head()")
                    st.write(data.head())
                    st.divider()
                    st.write("The following is the tail of the data")
                    st.code("data.tail()")
                    st.write(data.tail())
            
            if "shape_and_info_button" not in st.session_state:
                st.session_state['shape_and_info_button'] = 0
            
            if shape_and_info_button:
                st.session_state['shape_and_info_button'] +=1
                if st.session_state['shape_and_info_button'] %2 != 0:
                    data = st.session_state['dataset']
                    st.write("The following is the shape of this data")
                    st.code("data.shape()")
                    st.write(data.shape)
                    st.divider()
                    st.write("The following is the info of this data")
                    st.code("data.info()")
                    st.write(data.info())
            
            if "describe_button" not in st.session_state:
                st.session_state['describe_button'] = 0
            
            if describe_button:
                st.session_state['describe_button'] += 1
                if st.session_state['describe_button'] %2 != 0:
                    data = st.session_state['dataset']
                    st.write("The following describe the summary of this data")
                    st.code("data.describe()")
                    st.write(data.describe())
        
                
        
