"""
This file provided feature manipulation methods.
For now, only encode_string_label is available.
"""

from sklearn.preprocessing import LabelEncoder


def encode_string_label(data, label):
    """
    Encode string labels into numbers.
    Args:
        data: pandas.DataFrame, dataset
        label: str, name of the column want to encode

    Returns: pandas.DataFrame, dataset

    """
    lb = LabelEncoder()
    data[label] = lb.fit_transform(data[label])
    return data
