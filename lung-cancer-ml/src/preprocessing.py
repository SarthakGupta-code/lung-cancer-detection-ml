"""Preprocessing utilities for the lung cancer ML project.

This module provides helper functions for loading the synthetic dataset,
handling missing values, encoding categorical variables, and creating
train/test splits suitable for classical machine learning models.
"""

from typing import List, Tuple

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder


ORDINAL_COLUMNS = [
    "Dyspnea",
    "Chest Pain",
    "Weight Loss",
    "Occupational Hazards",
    "Pollution Level in Residence City",
    "Hoarseness of Voice",
]

ORDINAL_ORDER = {
    "Dyspnea": ["None", "Mild", "Moderate", "Severe"],
    "Chest Pain": ["None", "Mild", "Moderate", "Severe"],
    "Weight Loss": ["None", "Mild", "Marked"],
    "Occupational Hazards": ["None", "Low", "Moderate", "High"],
    "Pollution Level in Residence City": ["Low", "Moderate", "High"],
    "Hoarseness of Voice": ["None", "Mild", "Moderate", "Severe"],
}

MISSING_VALUE_COLUMNS = [
    "Family History of Cancer",
    "Dyspnea",
    "Chest Pain",
    "Weight Loss",
    "Previous Lung Disease",
    "Occupational Hazards",
    "Allergy",
    "Immediate Family Smokers",
    "Hoarseness of Voice",
]

ONE_HOT_COLUMNS = [
    "Gender",
    "Smoking",
    "Family History of Cancer",
    "Coughing",
    "Previous Lung Disease",
    "Allergy",
    "Coughing Blood",
    "Immediate Family Smokers",
    "Fatigue",
]

TARGET_COLUMN = "Lung Cancer"


def load_data(path: str) -> pd.DataFrame:
    """Load the lung cancer CSV dataset from disk.

    Parameters
    ----------
    path : str
        Path to the CSV file containing the dataset.

    Returns
    -------
    pd.DataFrame
        Data frame with all raw columns as loaded from the CSV file.
    """
    df = pd.read_csv(path, keep_default_na=False)
    return df


def _encode_ordinal_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Apply simple ordinal encoding to symptom severity columns.

    The mapping is defined in ORDINAL_ORDER and is applied column by column.
    Any unexpected category is treated as missing (NaN).
    """
    df_encoded = df.copy()
    for col in ORDINAL_COLUMNS:
        if col not in df_encoded.columns:
            continue
        order = ORDINAL_ORDER[col]
        mapping = {name: idx for idx, name in enumerate(order)}
        df_encoded[col] = df_encoded[col].map(mapping)
    return df_encoded


def preprocess_data(
    df: pd.DataFrame,
) -> Tuple[pd.DataFrame, pd.Series, OneHotEncoder, List[str]]:
    """Preprocess the raw data into numeric features and target labels.

    Steps:
    - Drop rows with missing values in clinically important columns.
    - Ordinal-encode ordered symptom and exposure columns.
    - One-hot encode nominal categorical variables.
    - Extract the binary target label (Lung Cancer) as 0/1.

    Parameters
    ----------
    df : pd.DataFrame
        Raw data frame with all original columns.

    Returns
    -------
    X : pd.DataFrame
        Preprocessed feature matrix with numeric columns only.
    y : pd.Series
        Binary target labels (1 for Lung Cancer = Yes, 0 for No).
    encoder : OneHotEncoder
        Fitted OneHotEncoder instance used for nominal columns.
    one_hot_feature_names : list of str
        Names of the one-hot encoded feature columns.
    """
    # Drop rows with missing values in key columns, following the original study.
    df_clean = df.dropna(subset=MISSING_VALUE_COLUMNS).copy()

    # Ensure target is binary 0/1 for modelling, leaving original labels intact in df_clean.
    y = df_clean[TARGET_COLUMN].map({"No": 0, "Yes": 1})

    # Separate features from the target.
    X = df_clean.drop(columns=[TARGET_COLUMN])

    # Ordinal encode severity-style columns.
    X = _encode_ordinal_columns(X)

    # One-hot encode nominal categorical columns.
    # scikit-learn >=1.4 uses sparse_output instead of sparse.
    ohe = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
    nominal_data = ohe.fit_transform(X[ONE_HOT_COLUMNS])
    nominal_feature_names = ohe.get_feature_names_out(ONE_HOT_COLUMNS)
    nominal_df = pd.DataFrame(nominal_data, columns=nominal_feature_names, index=X.index)

    # Keep any remaining numeric columns (including ordinal-encoded ones).
    numeric_cols = [c for c in X.columns if c not in ONE_HOT_COLUMNS]
    X_numeric = X[numeric_cols].reset_index(drop=True)
    nominal_df = nominal_df.reset_index(drop=True)

    X_final = pd.concat([X_numeric, nominal_df], axis=1)

    # Basic sanity check: ensure no remaining object dtypes.
    if X_final.select_dtypes(include=["object"]).shape[1] > 0:
        raise ValueError("Preprocessed feature matrix still has non-numeric columns.")

    return X_final, y.reset_index(drop=True), ohe, list(nominal_feature_names)


def train_test_split_wrapped(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = 0.2,
    random_state: int = 42,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Split the dataset into training and testing sets with stratification.

    Parameters
    ----------
    X : pd.DataFrame
        Feature matrix after preprocessing.
    y : pd.Series
        Binary target labels.
    test_size : float, optional
        Proportion of the data to use as the test set (default is 0.2).
    random_state : int, optional
        Random seed for reproducibility (default is 42).

    Returns
    -------
    X_train : np.ndarray
        Training features.
    X_test : np.ndarray
        Testing features.
    y_train : np.ndarray
        Training labels.
    y_test : np.ndarray
        Testing labels.
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X.values,
        y.values,
        test_size=test_size,
        stratify=y.values,
        random_state=random_state,
    )
    return X_train, X_test, y_train, y_test


