"""
All python files in the tests folder are for testing only. They are safe to delete and modified without
affecting the backend server integrity.
This test file is for breast cancer dataset testing.
"""

# Import the necessary libraries
from models.svm_model import SVMModel
from utils.process_dataset import load_dataset, split_data

# Load the dataset
cancer = load_dataset("breast cancer wisconsin")

# Baseline Model
# Step 1: Split the dataset into training set and test set
splits_base = split_data(data=cancer, target_column="diagnosis", train_size=0.7)
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

# Optimal Model
# Step 1: Apply feature manipulation to get the optimal model results
correlation_matrix = cancer.corr()
correlations = correlation_matrix["diagnosis"]
features = correlations[correlations > 0.2].index
cancer_op = cancer[features]

# Step 2: Split the dataset into training set and test set
splits_op = split_data(data=cancer_op, target_column="diagnosis", train_size=0.7)
X_train_op, X_test_op, y_train_op, y_test_op = splits_op[0]

# Step 3: Train the model using the training sets
op_model = SVMModel({"kernel": "linear"})
op_model.train(X_train_op, y_train_op)

# Step 4: Predict the response for test dataset
y_pred_op = op_model.predict(X_test_op)

# Step 5: Evaluate the model results
classification_stats_op, confusion_mat_op = op_model.evaluate(X_test_op, y_test_op)
print("Optimal Model Evaluation Stats")
print("Accuracy: ", classification_stats_op['accuracy'])
print("Recall: ", classification_stats_op['macro avg']['recall'])
print("Precision: ", classification_stats_op['macro avg']['precision'])
print("F1-Score: ", classification_stats_op['macro avg']['f1-score'])
print("Confusion Matrx: \n", confusion_mat_op)

op_model.plot_roc_curve(X_test_op, y_test_op).show()
op_model.plot_precision_recall_curve(X_test_op, y_test_op).show()
op_model.plot_decision_boundary(X_train_op, y_train_op, X_test_op, y_test_op).show()
