"""Utility functions for plotting and shared configuration.

This module contains helper functions for visualising confusion matrices
and feature importances, as well as small utilities that are reused across
the notebooks and scripts.
"""

from typing import List, Optional

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import ConfusionMatrixDisplay


def plot_confusion_matrix(
    cm: np.ndarray,
    class_names: Optional[List[str]] = None,
    title: str = "Confusion Matrix",
    cmap: str = "Blues",
) -> None:
    """Plot a confusion matrix using matplotlib.

    Parameters
    ----------
    cm : np.ndarray
        Confusion matrix of shape (2, 2) or (n_classes, n_classes).
    class_names : list of str, optional
        Names of the classes in the same order as in the confusion matrix.
        If None, numeric labels are used.
    title : str, optional
        Title for the plot (default is "Confusion Matrix").
    cmap : str, optional
        Matplotlib colormap name (default is "Blues").
    """
    if class_names is None:
        class_names = [str(i) for i in range(cm.shape[0])]

    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
    fig, ax = plt.subplots(figsize=(4, 4))
    disp.plot(ax=ax, cmap=cmap, colorbar=False)
    ax.set_title(title)
    plt.tight_layout()


def plot_feature_importances(
    feature_names: List[str],
    importances: np.ndarray,
    top_n: int = 15,
    title: str = "Feature Importances",
    figsize: tuple = (6, 4),
) -> None:
    """Plot the top-n feature importances as a horizontal bar chart.

    Parameters
    ----------
    feature_names : list of str
        Names of the features corresponding to the importances.
    importances : np.ndarray
        Feature importance values (e.g., from tree-based models).
    top_n : int, optional
        Number of top features to display (default is 15).
    title : str, optional
        Title of the plot (default is "Feature Importances").
    figsize : tuple, optional
        Figure size for the matplotlib plot (default is (6, 4)).
    """
    importances = np.asarray(importances)
    if importances.ndim != 1:
        raise ValueError("importances should be a 1D array.")

    data = pd.DataFrame(
        {"feature": feature_names, "importance": importances}
    ).sort_values("importance", ascending=False)

    data_top = data.head(top_n).iloc[::-1]  # reverse for nicer bar order

    plt.figure(figsize=figsize)
    plt.barh(data_top["feature"], data_top["importance"], color="steelblue")
    plt.xlabel("Importance")
    plt.title(title)
    plt.tight_layout()





