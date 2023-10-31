"""
This file provided methods that involves dataset processing.
Before loading the dataset, this file provided some preprocessing methods.
"""

import os
import pandas as pd
from sklearn.model_selection import train_test_split, KFold
from sklearn.impute import SimpleImputer

from utils.feature_manipulation import encode_string_label


def load_dataset(dataset_name, feature_status=None):
    """
      Load a dataset from a CSV file. only select the features marked True in feature_status

      Args:
          dataset_name (str): Name of the dataset.
          feature_status (dict): Dictionary indicating whether each feature is selected or not

      Returns:
          pandas.DataFrame: Loaded dataset.
      """
    script_dir = os.path.dirname(__file__)
    file_name = dataset_name.replace(' ', '_') + '.csv'
    file_path = os.path.join(script_dir, '..', 'datasets', file_name)

    data = pd.read_csv(file_path)
    if dataset_name == 'breast cancer wisconsin':
        data = process_breast_cancer_wisconsin(dataset_name, data)
    elif dataset_name == 'penguins size':
        data = process_penguins(dataset_name, data)
    elif dataset_name == 'ionosphere':
        data = process_ionosphere(dataset_name, data)
    elif dataset_name == 'titanic':
        data = process_titanic(dataset_name, data)

    if feature_status is None:
        return data

    for feature_name in feature_status:
        if feature_status[feature_name] is False:
            data = remove_col(data, feature_name)

    return data


def process_breast_cancer_wisconsin(dataset_name, data):
    """
    Process the Breast Cancer Wisconsin dataset by removing unnecessary columns and 
    encoding the target column.

    Parameters:
    ----------
    dataset_name : str
        Name of the dataset (not used in this function).
    data : pandas.DataFrame
        The original dataset.

    Returns:
    -------
    pandas.DataFrame
        Processed DataFrame with unnecessary columns removed and the target column encoded.
    """
    data = remove_col(data, "id")
    target_column = get_target_column(dataset_name)
    data = encode_string_label(data, target_column)
    return data


def process_penguins(dataset_name, data):
    """
    Process the penguins dataset by cleaning rows and encoding categorical columns.

    Parameters:
    ----------
    dataset_name : str
        Name of the dataset (not used in this function).
    data : pandas.DataFrame
        The original dataset.

    Returns:
    -------
    pandas.DataFrame
        Processed DataFrame with cleaned rows and encoded categorical columns.
    """
    data = clean_rows(data)
    target_column = get_target_column(dataset_name)
    data = encode_string_label(data, target_column)
    data = encode_string_label(data, "island")
    data = encode_string_label(data, 'sex')
    return data


def process_ionosphere(dataset_name, data):
    target_column = get_target_column(dataset_name)
    data = encode_string_label(data, target_column)
    return data


def process_titanic(dataset_name, data):
    """
    Process the Titanic dataset by encoding categorical columns and performing data cleaning.

    Parameters:
    ----------
    dataset_name : str
        Name of the dataset (not used in this function).
    data : pandas.DataFrame
        The original dataset.

    Returns:
    -------
    pandas.DataFrame
        Processed DataFrame with encoded categorical columns and data cleaning applied.
    """
    target_column = get_target_column(dataset_name)
    data = encode_string_label(data, target_column)
    
    # Fill missing values in 'Embarked' with "S"
    data['Embarked'].fillna("S", inplace=True)
    
    # Fill missing values in 'Age' with the median age
    age_median = data['Age'].median()
    data["Age"].fillna(age_median, inplace=True) 

    data = encode_string_label(data, 'Sex')
    data = encode_string_label(data, 'Embarked')
    
    # Drop the 'Cabin', 'Name' and 'Ticket' columns
    data.drop(columns=['PassengerId', 'Cabin', 'Name', 'Ticket'], inplace=True)

    return data


def get_target_column(dataset_name):
    """
    This function takes a dataset name as input and returns the corresponding target column.
    
    Parameters:
    dataset_name (str): Name of the dataset

    Returns:
    target_column (str): Name of the target column for the given dataset. 
                         If the dataset is not recognized, it returns an empty string.
    """
    if dataset_name == 'breast cancer wisconsin':
        target_column = 'diagnosis'
    elif dataset_name == 'ionosphere':
        target_column = 'class'
    elif dataset_name == 'penguins size':
        target_column = 'species'
    elif dataset_name == 'titanic':
        target_column = 'Survived'
    else:
        target_column = ''
    return target_column


def remove_col(data, column_name):
    """
    Remove a specified column from the given DataFrame.

    Parameters:
    ----------
    data : pandas.DataFrame
        The DataFrame from which the column should be removed.
    column_name : str
        The name of the column to be removed.

    Returns:
    -------
    pandas.DataFrame
        A new DataFrame with the specified column removed.
    """
    return data.drop(column_name, axis=1)


def clean_rows(data, threshold=3):
    """
    Delete the whole row is this row has more than threshold number of NaN data
    Args:
        data: pd.dataframe, dataset read from csv file
        threshold: int, the threshold number

    Returns:
        the dataset after clean rows
    """
    filtered_data = data[data.isnull().sum(axis=1) < threshold]
    filled_data = impute_category_data(filtered_data)
    return filled_data


def impute_category_data(data):
    """
      Use SimpleImputer to do data imputation
      For simpleImputer, refer to https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html
      for more details.
      Args:
          data: pd.dataframe, dataset read from csv file

      Returns:
          pd.dataframe, the dataset after data imputation
      """
    cols = list(data.columns.values)
    imp = SimpleImputer(strategy='most_frequent')
    data = pd.DataFrame(imp.fit_transform(data))
    imp = SimpleImputer(missing_values='.', strategy='most_frequent')
    data = pd.DataFrame(imp.fit_transform(data), columns=cols)
    return data


def split_data(data, target_column, train_size=None, k_folds=None):
    """
    Split the data into train and test sets, optionally performing k-fold cross-validation.

    Parameters:
    ----------
    data : pandas.DataFrame
        The original dataset containing both features and target.
    target_column : str
        The name of the target column.
    train_size : float, optional
        The proportion of data to be used for training. Only used when k_folds is not specified.
    k_folds : int, optional
        The number of folds for k-fold cross-validation. If provided, k-fold splits will be used instead of
        train-test split.

    Returns:
    -------
    list of tuples
        A list of tuples containing train and test data for each fold if k_folds is specified,
        or a list containing a single tuple of train and test data if k_folds is not specified.
        Each tuple contains X_train, X_test, y_train, y_test data splits.
    """
    X = data.drop(target_column, axis=1)
    y = data[target_column]
    if k_folds is not None:
        kf = KFold(n_splits=k_folds)
        return [(X.iloc[train_index], X.iloc[test_index], y.iloc[train_index],
                 y.iloc[test_index]) for train_index, test_index in kf.split(X)]
    else:
        X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                            train_size=train_size,
                                                            random_state=42)
        return [(X_train, X_test, y_train, y_test)]
