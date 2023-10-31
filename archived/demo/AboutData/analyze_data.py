'''
Data Preparation page. When user select EDA->Analyze Data, will call analyze_data_main()
'''
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_extras.add_vertical_space import add_vertical_space

def analyze_data_main(column):
    with column:
        st.title("Analyze Data")
        context_container = st.container()

        with context_container:
            st.header("Final Data Analysis")

            variable_names = st.session_state['feature_names']
            final_feature_option = st.multiselect("Select the Feature to analyze", variable_names, key='final_feature_option')
            add_vertical_space(2)
            data = st.session_state['dataset']
            feature_col = data[st.session_state['final_feature_option']]
            stat_col, plot_col = st.columns(2)
            
            with stat_col:
                if final_feature_option:
                    st.write(feature_col.describe())
            
            with plot_col:
                if final_feature_option:
                    fig, ax = plt.subplots()
                    ax.boxplot(feature_col)

                    ax.set_ylabel('Values')
                    ax.set_title('Box Plot')

                    st.pyplot(fig)
        
        st.divider()
        button_col, display_col = st.columns([1, 3])

        with button_col:
            add_button = st.button("Add")
            add_vertical_space(2)
            drop_button = st.button("Drop")
            add_vertical_space(2)
            scale_button = st.button("Scale")
            add_vertical_space(2)
            encode_button = st.button("Encode")
        
        with display_col:
            if add_button:
                st.write("Need more development")
            
            if drop_button:
                st.write("Need more development")
            
            if scale_button:
                st.write("Need more development")

            if encode_button:
                st.write("Need more development")

