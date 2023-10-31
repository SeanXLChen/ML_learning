'''
Data Preparation page. When user select EDA->Clean Data, will call clean_data_main()
'''
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

def clean_data_main(column):
    with column:
        st.title("Clean Data")
        context_container = st.container()

        with context_container:
            st.header("How to handle the missing value?")
            st.text("Steps:")
            st.text("1. Identify and understand missing data")
            st.text("2. Develop a plan for handing missing data")
            st.text("3. Decide on the most appropriate method")
        
        st.divider()
        button_col, display_col = st.columns([1, 3])

        with button_col:
            check_na_button = st.button("Check Missing Value")
            add_vertical_space(2)
            fill_median_button = st.button("Fill By Median")
            add_vertical_space(2)
            fill_mode_button = st.button("Fill By Mode")

        with display_col:
            if "check_na_button" not in st.session_state:
                st.session_state['check_na_button'] = 0
            
            if check_na_button:
                st.session_state['check_na_button'] +=1
                if st.session_state['check_na_button'] %2 != 0:
                    data = st.session_state['dataset']
                    st.write("The following code checks missing value")
                    st.code("data.isna().sum()")
                    st.write(data.isna().sum())
            
            if "fill_median_button" not in st.session_state:
                st.session_state['fill_median_button'] = 0
            
            if fill_median_button:
                st.session_state['fill_median_button'] +=1
                if st.session_state['fill_median_button'] %2 != 0:
                    data = st.session_state['dataset']
                    st.write("The following code fill the missing value by median")
                    st.code("data['feature'].fillna(data['feature'].median(), inplace = True)")
                    st.write("Needs further development")

            if "fill_mode_button" not in st.session_state:
                st.session_state['fill_mode_button'] = 0
            
            if fill_mode_button:
                st.session_state['fill_mode_button'] +=1
                if st.session_state['fill_mode_button'] %2 != 0:
                    data = st.session_state['dataset']
                    st.write("The following code fill the missing value by mode")
                    st.code("data['feature'].fillna(data['feature'].mode(), inplace = True)")
                    st.write("Needs further development")