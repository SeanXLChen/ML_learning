"""
All python files in the tests folder are for testing only. They are safe to delete and modified without
affecting the backend server integrity.
This test file is for plotly jsonify figures and generate figure in json format testing.
"""

import plotly.graph_objects as go
import json

# Read and parse the histogram data
with open("json_data/train_svm.json", 'r') as f:
    data = f.read()
    data_parsed = json.loads(data)

result = data_parsed[0]

# Extract stats
accuracy = result['accuracy']
f1_score = result['f1_score']
precision = result['precision']
recall = result['recall']

print(f"Accuracy: {accuracy}")
print(f"F1 Score: {f1_score}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")

# Parse the JSON strings into Python dicts and create the Plotly figures
confusion_matrix_figure_dict = json.loads(result['confusion_matrix_plot_json'])
roc_curve_figure_dict = json.loads(result['roc_curve_plot_json'])

confusion_matrix_figure = go.Figure(confusion_matrix_figure_dict)
roc_curve_figure = go.Figure(roc_curve_figure_dict)

# Display the figures
confusion_matrix_figure.show()
roc_curve_figure.show()
