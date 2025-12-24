"""Model evaluation utilities for the lung cancer ML project.

This module provides helper functions to evaluate trained models using
accuracy, precision, and recall, and to aggregate results into a summary
table suitable for reporting.
"""

from typing import Dict, Tuple

import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
)


def evaluate_models(
    models: Dict[str, object], X_test: np.ndarray, y_test: np.ndarray
) -> pd.DataFrame:
    """Evaluate multiple models on a test set.

    For each model, this function computes accuracy, precision, and recall.

    Parameters
    ----------
    models : dict
        Dictionary mapping model names to trained model instances.
    X_test : np.ndarray
        Test feature matrix.
    y_test : np.ndarray
        True labels for the test set.

    Returns
    -------
    pd.DataFrame
        Data frame with one row per model and columns:
        ["Model", "Accuracy", "Precision", "Recall"].
    """
    records = []
    for name, model in models.items():
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, zero_division=0)
        rec = recall_score(y_test, y_pred, zero_division=0)
        records.append(
            {
                "Model": name,
                "Accuracy": acc,
                "Precision": prec,
                "Recall": rec,
            }
        )

    results = pd.DataFrame.from_records(records)
    results = results.sort_values(by="Accuracy", ascending=False).reset_index(drop=True)
    return results


def confusion_matrix_for_model(
    model: object, X_test: np.ndarray, y_test: np.ndarray
) -> Tuple[np.ndarray, np.ndarray]:
    """Compute a confusion matrix for a single trained model.

    Parameters
    ----------
    model : object
        Trained classifier with a predict method.
    X_test : np.ndarray
        Test feature matrix.
    y_test : np.ndarray
        True labels for the test set.

    Returns
    -------
    cm : np.ndarray
        Confusion matrix with shape (2, 2) for binary classification.
    y_pred : np.ndarray
        Predicted labels for the test set.
    """
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    return cm, y_pred





