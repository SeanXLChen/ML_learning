'''
Data Preparation page. When user select EDA->Visualize Data, will call visualize_data_main()
'''
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_extras.add_vertical_space import add_vertical_space

def visualize_data_main(column):
    with column:
        st.title("Visualize Data")
        context_container = st.container()

        with context_container:
            st.header("How to visualize our features?")
            st.text("Types of Visualization:")
            st.text("1. Histogram")
            st.text("2. Bar Chart")
            st.text("3. Pie Chart")
            st.text("4. Scatter Plot")
            st.text("5. Correlation Matrix")
            select_x_col, select_y_col = st.columns(2)
            with select_x_col:
                variable_names = st.session_state['feature_names']
                select_x_options = st.multiselect("Select the X Feature", variable_names, key='variable_names')
                
            with select_y_col:
                target_names = st.session_state['feature_names']
                select_y_options = st.multiselect("Select the Y Feature", target_names, key = 'target_names')
        
        st.divider()
        button_col, display_col = st.columns([1, 3])

        with button_col:
            histogram_button = st.button("Plot Histrogram")
            add_vertical_space(2)
            bar_chart_button = st.button("Plot Bar Chart")
            add_vertical_space(2)
            pie_chart_button = st.button("Plot Pie Chart")
            add_vertical_space(2)
            scatter_plot_button = st.button("Plot Scatter Plot")
            add_vertical_space(2)
            correlation_button = st.button("Plot Correlation Matrix")
        
        with display_col:
            if "histogram_button" not in st.session_state:
                st.session_state['histogram_button'] = 0
            
            if histogram_button:
                st.session_state['histogram_button'] +=1
                if st.session_state['histogram_button'] %2 != 0:
                    data = st.session_state['dataset']
                    selected_data = data[st.session_state['variable_names']]
                    fig, ax = plt.subplots()
                    ax.hist(selected_data, bins = 10)
                    st.pyplot(fig)

            if "bar_chart_button" not in st.session_state:
                st.session_state['bar_chart_button'] = 0
            
            if bar_chart_button:
                st.write("Need further development")
            
            if "pie_chart_button":
                st.session_state['pie_chart_button'] = 0
            
            if pie_chart_button:
                st.write("Need further development")

            if "scatter_plot_button" not in st.session_state:
                st.session_state['scatter_plot_button'] = 0
            
            if scatter_plot_button:
                st.session_state['scatter_plot_button'] += 1
                if st.session_state['scatter_plot_button'] %2 != 0:
                    data = st.session_state['dataset']
                    x_data = data[st.session_state['variable_names']]
                    y_data = data[st.session_state['target_names']]
                    fig, ax = plt.subplots()
                    ax.scatter(x_data, y_data)
                    ax.set_xlabel("X")
                    ax.set_ylabel("Y")
                    ax.set_title("Scatter Chart")
                    st.pyplot(fig)
            
            if "correlation_button" not in st.session_state:
                st.session_state['correlation_button'] = 0

            if correlation_button:
                st.session_state['correlation_button'] += 1
                if st.session_state['correlation_button'] %2 != 0:
                    data = st.session_state['dataset']
                    correlation_matrix = np.corrcoef(data, rowvar=False)
                    fig, ax = plt.subplots()
                    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)
                    ax.set_title('Correlation Matrix')
                    st.pyplot(fig)

        
        
