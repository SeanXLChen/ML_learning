"""
All python files in the tests folder are for testing only. They are safe to delete and modified without
affecting the backend server integrity.
This test file is for penguins dataset testing.
NOTICE: penguins dataset are not used at the end of the phase1 version.
"""

# Import the necessary libraries
from models.svm_model import SVMModel
from utils.process_dataset import load_dataset, split_data

# Load the dataset
penguins = load_dataset("penguins size")

# Baseline Model
# Step 1: Split the dataset into training set and test set
splits_base = split_data(data=penguins, target_column="species", train_size=0.7)
X_train_base, X_test_base, y_train_base, y_test_base = splits_base[0]

# Step 2: Train the model using the training sets
base_model = SVMModel({"kernel": "linear"})
base_model.train(X_train_base, y_train_base)

# Step 3: Train the model using the training sets
y_pred_base = base_model.predict(X_test_base)

# Step 4: Evaluate the model results
classification_stats_base, confusion_mat_base = base_model.evaluate(X_test_base, y_test_base)
print("Baseline Model Evaluation Stats")
print("Accuracy: ", classification_stats_base['accuracy'])
print("Recall: ", classification_stats_base['macro avg']['recall'])
print("Precision: ", classification_stats_base['macro avg']['precision'])
print("F1-Score: ", classification_stats_base['macro avg']['f1-score'])
print("Confusion Matrx: \n", confusion_mat_base)

base_model.plot_decision_boundary(X_train_base, y_train_base, X_test_base, y_test_base).show()
