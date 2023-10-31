"""
All python files in the tests folder are for testing only. They are safe to delete and modified without
affecting the backend server integrity.
This test file is for plotly library testing.
"""

import plotly.graph_objects as go
import json

# Read and parse the histogram data
with open("json_data/plot_hist.json", 'r') as f:
    data_str_hist = f.read()
    data_str_hist_parsed = json.loads(data_str_hist)  # first parse
    hist_data = json.loads(data_str_hist_parsed['data'])

# Create a Plotly figure from the histogram dictionary
fig_hist = go.Figure(hist_data)

# Display the histogram figure
fig_hist.show()

# Read and parse the line plot data
with open("json_data/plot_line.json", 'r') as f:
    data_str_line = f.read()
    data_str_line_parsed = json.loads(data_str_line)  # first parse
    line_data = json.loads(data_str_line_parsed['data'])

# Create a Plotly figure from the line plot dictionary
fig_line = go.Figure(line_data)

# Display the line plot figure
fig_line.show()

# Read and parse the scatter plot data
with open("json_data/plot_scatter.json", 'r') as f:
    data_str_scatter = f.read()
    data_str_scatter_parsed = json.loads(data_str_scatter)  # first parse
    scatter_data = json.loads(data_str_scatter_parsed['data'])

# Create a Plotly figure from the scatter plot dictionary
fig_scatter = go.Figure(scatter_data)

# Display the scatter plot figure
fig_scatter.show()

# Read and parse the pie plot data
with open("json_data/plot_pie.json", 'r') as f:
    data_str_pie = f.read()
    data_str_pie_parsed = json.loads(data_str_pie)  # first parse
    pie_data = json.loads(data_str_pie_parsed['data'])

# Create a Plotly figure from the pie plot dictionary
fig_pie = go.Figure(pie_data)

# Display the pie plot figure
fig_pie.show()

# Read and parse the bar plot data
with open("json_data/plot_bar.json", 'r') as f:
    data_str_bar = f.read()
    data_str_bar_parsed = json.loads(data_str_bar)  # first parse
    bar_data = json.loads(data_str_bar_parsed['data'])

# Create a Plotly figure from the bar plot dictionary
fig_bar = go.Figure(bar_data)

# Display the bar plot figure
fig_bar.show()

# Read and parse the box plot data
with open("json_data/plot_box.json", 'r') as f:
    data_str_box = f.read()
    data_str_box_parsed = json.loads(data_str_box)  # first parse
    box_data = json.loads(data_str_box_parsed['data'])

# Create a Plotly figure from the box plot dictionary
fig_box = go.Figure(box_data)

# Display the box plot figure
fig_box.show()
