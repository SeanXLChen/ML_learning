"""
This is the main entrance for the backend server. Before you do "npm start" in the frontend folder,
please run this python file first to start the backend server first.
"""

from flask import Flask, request, jsonify, session
from utils.process_dataset import load_dataset, get_target_column, split_data
import visualizations.visualizations as visualize
from models.svm_model import SVMModel
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 's3cr3t_k3y'
model = None

GLOBAL_DATA = {}
ALLOWED_DATASET_NAMES = ['breast cancer wisconsin', 'ionosphere', 'penguins size']
ALLOWED_PLOT_TYPES = ['histogram', 'line', 'scatter', 'box', 'bar', 'pie']

CORS(app)


@app.route('/load_data', methods=['POST'])
def load_data():
    """
    Load the dataset and store its name, target column, and feature columns into session.
    Return both target column and feature columns.

    Request JSON example:
    {
        "dataset_name": "breast cancer wisconsin",  
        # Name of the dataset, string, range in ['breast cancer wisconsin', 'ionosphere', 'penguins size']
    }

    Returns: JSON response: { # baseline default config, will lead to the baseline result. "baseline_config": {
    "SVM_parameters": { "C": 10, "coef0": 0.0, "degree": 3, "gamma": 0.0001, "kernel": "linear" },
    "feature_selection": {...} }, "error": null, "feature_columns": [...],               # List of dataset column
    names "message": "Import data successfully.",  # Message indicating successful import, string, range in [null,
    "Import data successfully."] # optimal default config, will lead to the best accuracy result. "optimal_config": {
    "SVM_parameters": { "C": 10, "coef0": 0.0, "degree": 3, "gamma": 0.1, "kernel": "rbf" }, "feature_selection": {
    ...} }, "target_column": "class"             # Target column for the given dataset }

    Raises:
    400 Bad Request: If dataset name is not provided in the request, or the dataset name is not 
    in the range of ['breast cancer wisconsin', 'ionosphere', 'penguins size']
    """
    json_data = request.get_json()
    dataset_name = json_data.get('dataset_name')

    if not dataset_name:
        return jsonify({
            "message": None,
            "error": 'Dataset name not provided.',
            "feature_columns": None,
            "target_column": None
        }), 400

    if dataset_name not in ALLOWED_DATASET_NAMES:
        return jsonify({
            "message": None,
            "error": 'Dataset name not recognized.',
            "feature_columns": None,
            "target_column": None
        }), 400

    # Load the dataset and store it in the global data dict
    GLOBAL_DATA[dataset_name] = load_dataset(dataset_name)
    # Get the target column
    target_column = get_target_column(dataset_name)
    # Get the rest feature columns
    feature_columns = [col for col in GLOBAL_DATA[dataset_name].columns.tolist() if col != target_column]
    optimal_feature_status = {}
    if dataset_name == 'breast cancer wisconsin':
        for feature in feature_columns:
            optimal_feature_status[feature] = True
        optimal_feature_status["fractal_dimension_mean"] = False
        optimal_feature_status["fractal_dimension_se"] = False
        optimal_feature_status["smoothness_se"] = False
        optimal_feature_status["symmetry_se"] = False
        optimal_feature_status["texture_se"] = False
    elif dataset_name == 'ionosphere':
        for feature in feature_columns:
            optimal_feature_status[feature] = False
        optimal_feature_status["attribute1"] = True
        optimal_feature_status["attribute3"] = True
        optimal_feature_status["attribute5"] = True
        optimal_feature_status["attribute7"] = True
        optimal_feature_status["attribute8"] = True
        optimal_feature_status["attribute9"] = True
        optimal_feature_status["attribute15"] = True
        optimal_feature_status["attribute21"] = True
        optimal_feature_status["attribute23"] = True
        optimal_feature_status["attribute29"] = True
        optimal_feature_status["attribute31"] = True
        optimal_feature_status["attribute33"] = True
    else:
        for feature in feature_columns:
            optimal_feature_status[feature] = True
        optimal_feature_status = {"culmen_depth_mm": False, "island": False, "sex": False}
    baseline_feature_status = {}
    for feature in feature_columns:
        baseline_feature_status[feature] = True
    optimal_svm_parameters = {}
    if dataset_name == 'breast cancer wisconsin':
        optimal_svm_parameters["kernel"] = "linear"
        optimal_svm_parameters["C"] = 10
        optimal_svm_parameters["gamma"] = 0.1
        optimal_svm_parameters["coef0"] = 0.0
        optimal_svm_parameters["degree"] = 3
    elif dataset_name == 'ionosphere':
        optimal_svm_parameters["kernel"] = "rbf"
        optimal_svm_parameters["C"] = 10
        optimal_svm_parameters["gamma"] = 0.1
        optimal_svm_parameters["coef0"] = 0.0
        optimal_svm_parameters["degree"] = 3
    else:
        optimal_svm_parameters["kernel"] = "linear"
        optimal_svm_parameters["C"] = 10
        optimal_svm_parameters["gamma"] = 0.1
        optimal_svm_parameters["coef0"] = 0.0
        optimal_svm_parameters["degree"] = 3

    return jsonify({
        "message": 'Import data successfully.',
        "error": None,
        "feature_columns": feature_columns,
        "target_column": target_column,
        "optimal_config": {
            "feature_selection": optimal_feature_status,
            "SVM_parameters": optimal_svm_parameters
        },
        "baseline_config": {
            "feature_selection": baseline_feature_status,
            "SVM_parameters": {
                "kernel": "linear",
                "C": 10,
                "gamma": 0.0001,
                "coef0": 0.0,
                "degree": 3
            }
        }
    }), 200


@app.route('/plot', methods=['POST'])
def plot():
    """
    Select features, plot type, and generate a chart using data stored in the session.

    Request JSON example:
    {
        "feature_x": "radius_mean",  # Name of the first feature to select
        "feature_y": "texture_mean",  # Name of the second feature to select (optional)
        "plot_type": "scatter"  # Type of the plot to select ("histogram" or "line")
    }

    Returns:
    JSON response:
    {
        "message": "Plot generated successfully.",
        "error": None
        "data": [{"x":[1,2,3], "y":[1,2,3], "mode":"scatter"}],  # JSON representation of the plot,
    }

    Raises:
    400 Bad Request: If feature names, plot type, or data are not provided or not supported.
    """
    json_data = request.get_json()
    feature_x = json_data.get('feature_x')
    feature_y = json_data.get('feature_y')
    plot_type = json_data.get('plot_type')

    if plot_type is None:
        return jsonify({
            "message": None,
            "error": 'No plot type provided.',
            "data": None}), 400
    if plot_type not in ALLOWED_PLOT_TYPES:
        return jsonify({
            "message": None,
            "error": f'Plot type not supported. Supported types are {ALLOWED_PLOT_TYPES}.',
            "data": None}), 400
    if feature_x is None:
        return jsonify({
            "message": None,
            "error": 'No feature_x provided.',
            "data": None}), 400

    dataset_name = session.get('dataset_name')
    if dataset_name not in GLOBAL_DATA:
        return jsonify({
            "message": None,
            "error": f'Data for dataset {dataset_name} not found. Please load the data first.',
            "data": None}), 400

    data = GLOBAL_DATA[dataset_name]

    if feature_x not in data.columns:
        return jsonify({
            "message": None,
            "error": f'Feature {feature_x} does not exist in the dataset.',
            "data": None}), 400

    if feature_y and feature_y not in data.columns:
        return jsonify({
            "message": None,
            "error": f'Feature {feature_y} does not exist in the dataset.',
            "data": None}), 400

    session['feature_x'] = feature_x
    session['feature_y'] = feature_y
    session['plot_type'] = plot_type

    plot_json = visualize.plot_data(plot_type, data, feature_x, feature_y)

    if plot_json is not None:
        return jsonify({
            "message": 'Plot generated successfully.',
            "error": None,
            "data": plot_json}), 200
    else:
        return jsonify({
            "message": None,
            "error": 'Failed to generate plot.',
            "data": None}), 400


@app.route('/train_svm', methods=['POST'])
def train_svm():
    """
    Train an SVM model using the specified dataset and parameters.

    Request JSON example:
    {
    "dataset_name": "breast cancer wisconsin",  # Name of the dataset, string, range in
                                            ['breast cancer wisconsin', 'ionosphere', 'penguins size']
    "svm_params": {},                           # SVM parameters
                        https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
    "train_size": 0.7,                          # train set size, double, range 0.0 - 1.0
    "k_folds": null                             # number of folds for cross-validation, int, range 2 - 100
                                    # if both train_size and k_folds is not null, will use k_folds
    "selected_features":            # a dictionary of all feature_column_names: true/false (been selected)
        {
            "radius_mean": true,
            "texture_mean": false,
            "perimeter_mean": false,
            "area_mean": true,
            ...
        }
    }

    Returns:
    JSON response:
    {
    "avg_accuracy": 0.9296693060083838,
    "highest_accuracy_result": {
        "accuracy": 0.9649122807017544,
        "confusion_matrix_plot_json": "xxx",
        "f1_score": 0.9526578073089701,
        "precision": 0.9642401021711366,
        "recall": 0.9423935091277891,
        "roc_curve_plot_json": "xxx"
        }
    }
    """
    dataset_name = request.json['dataset_name']
    target_column = get_target_column(dataset_name)
    svm_params = request.json.get('svm_params', {})
    train_size = request.json.get('train_size')
    k_folds = request.json.get('k_folds')
    feature_status = request.json.get('selected_features')
    GLOBAL_DATA['current_dataset'] = load_dataset(dataset_name, feature_status)
    data = GLOBAL_DATA['current_dataset']
    feature_columns = [col for col in GLOBAL_DATA['current_dataset'].columns.tolist() if col != target_column]

    session['dataset_name'] = dataset_name
    session['target_column'] = target_column
    session['feature_columns'] = feature_columns
    session['feature_status'] = feature_status

    data_splits = split_data(data, target_column, train_size=train_size, k_folds=k_folds)

    global model
    all_results = []
    for X_train, X_test, y_train, y_test in data_splits:
        model = SVMModel(svm_params)
        model.train(X_train, y_train)

        classification_stats, confusion_mat = model.evaluate(X_test, y_test)
        accuracy = classification_stats['accuracy']
        recall = classification_stats['macro avg']['recall']
        precision = classification_stats['macro avg']['precision']
        f1_score = classification_stats['macro avg']['f1-score']

        # confusion_matrix_plot_json = model.plot_confusion_matrix(confusion_mat).to_json()
        roc_curve_plot_json = model.plot_roc_curve(X_test, y_test).to_json()
        precision_recall_curve_plot_json = model.plot_precision_recall_curve(X_test, y_test).to_json()
        
        all_results.append({
            'accuracy': accuracy,
            'recall': recall,
            'precision': precision,
            'f1_score': f1_score,
            'confusion_matrix': confusion_mat,
            'roc_curve_plot_json': roc_curve_plot_json,
            'precision_recall_curve_plot_json': precision_recall_curve_plot_json
        })
    avg_accuracy = 0.0
    max_accuracy = -1.0
    highest_accuracy_result = {}
    for i in range(len(all_results)):
        curr_accuracy = all_results[i]['accuracy']
        if curr_accuracy > max_accuracy:
            max_accuracy = curr_accuracy
            highest_accuracy_result = all_results[i]
        avg_accuracy += curr_accuracy
    avg_accuracy = avg_accuracy / len(all_results)

    return jsonify({
        'avg_accuracy': avg_accuracy,
        'highest_accuracy_result': highest_accuracy_result
    }), 200


@app.route('/features', methods=['GET'])
def get_features_status():
    """
        Returns a dictionary with all features status, true or false indicating certain feature is selected or not.
        All features' default status will be selected when the dataset is first loaded.

        Returns:
        JSON response:
        {
            "radius_mean": true
            "texture_mean": true
            "perimeter_mean": true
            ...
        }
    """
    return jsonify(session['feature_status']), 400


@app.route('/session', methods=['POST'])
def get_session():
    """
    Debug function, get all key-value pairs in the Flask session.
    """
    return jsonify(session)


@app.route('/global', methods=['POST'])
def get_global():
    """
    Debug function, get all key-value pairs in the GLOBAL_DATA.
    """
    return jsonify(GLOBAL_DATA)


if __name__ == '__main__':
    app.run(debug=True)
