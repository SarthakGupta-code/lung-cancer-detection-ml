"""Model definition and training utilities for the lung cancer ML project.

This module provides functions to construct standard machine learning models
and train them on preprocessed feature matrices.
"""

from typing import Dict

import numpy as np
from catboost import CatBoostClassifier
from sklearn.ensemble import (
    AdaBoostClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier,
)
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier


def get_models(random_state: int = 42) -> Dict[str, object]:
    """Create a dictionary of model instances keyed by model name.

    Parameters
    ----------
    random_state : int, optional
        Seed used for reproducible models where applicable (default is 42).

    Returns
    -------
    dict
        Dictionary mapping model name strings to untrained model instances.
    """
    models = {
        "Logistic Regression": LogisticRegression(
            max_iter=200, solver="lbfgs"
        ),
        "Decision Tree": DecisionTreeClassifier(
            random_state=random_state,
            max_depth=None,
        ),
        "KNN": KNeighborsClassifier(n_neighbors=5),
        "Random Forest": RandomForestClassifier(
            n_estimators=200,
            random_state=random_state,
        ),
        "XGBoost": XGBClassifier(
            n_estimators=200,
            learning_rate=0.05,
            max_depth=4,
            subsample=0.9,
            colsample_bytree=0.9,
            objective="binary:logistic",
            eval_metric="logloss",
            use_label_encoder=False,
            random_state=random_state,
        ),
        "Gradient Boosting": GradientBoostingClassifier(
            n_estimators=200,
            learning_rate=0.05,
            max_depth=3,
            random_state=random_state,
        ),
        "CatBoost": CatBoostClassifier(
            depth=4,
            learning_rate=0.05,
            loss_function="Logloss",
            verbose=False,
            random_seed=random_state,
        ),
        "AdaBoost": AdaBoostClassifier(
            n_estimators=200,
            learning_rate=0.05,
            random_state=random_state,
        ),
    }
    return models


def train_all_models(
    models: Dict[str, object], X_train: np.ndarray, y_train: np.ndarray
) -> Dict[str, object]:
    """Train all models on the provided training data.

    Parameters
    ----------
    models : dict
        Dictionary mapping model names to untrained model instances.
    X_train : np.ndarray
        Training feature matrix.
    y_train : np.ndarray
        Training labels (binary 0/1).

    Returns
    -------
    dict
        Dictionary mapping model names to trained model instances.
    """
    trained = {}
    for name, model in models.items():
        # For CatBoost and some others, passing numpy arrays is fine.
        model.fit(X_train, y_train)
        trained[name] = model
    return trained





