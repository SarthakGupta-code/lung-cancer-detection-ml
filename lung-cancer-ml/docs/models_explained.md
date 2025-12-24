## Models Explained

This project compares a range of classical machine learning algorithms for early detection of lung cancer using structured clinical and symptom data. All models are implemented using standard libraries such as scikit-learn, XGBoost, and CatBoost.

### Logistic Regression (LR)

Logistic Regression is a **linear classifier** that models the log-odds of the positive class as a linear combination of the input features. It uses the **sigmoid (logistic) function** to convert this linear combination into a probability between 0 and 1.

- Well suited for binary classification problems like “lung cancer vs. no lung cancer”.  
- Coefficients are easy to interpret: positive values indicate increased risk, negative values indicate decreased risk.  
- Assumes a mostly linear relationship between features and the log-odds of the outcome.

In this study, Logistic Regression is particularly useful for **symptom coefficient analysis** and interpretability.

### Decision Tree (DT)

A Decision Tree classifier splits the data into segments by asking a series of **yes/no questions** about the features (e.g., “Is age > 60?”, “Is smoking status = Current?”). At each node:

- The algorithm chooses a split that best separates the classes using criteria like **Gini impurity** or **entropy**.  
- Leaves of the tree correspond to final predictions (Lung Cancer = Yes/No).

Decision Trees are:

- Easy to visualise and interpret.  
- Able to capture non‑linear relationships and interactions.

However, single trees can be **unstable** and prone to **overfitting**, especially when grown deep.

### K‑Nearest Neighbours (KNN)

K‑Nearest Neighbours is an **instance-based** (or “lazy”) learning method:

- To classify a new patient, it finds the **K most similar patients** in the training data, based on a distance metric (usually Euclidean distance on the feature space).  
- The predicted class is determined by the majority label among these K neighbours.

Properties:

- Simple to understand and implement.  
- No explicit training phase (aside from storing the data).

Limitations:

- Performance depends heavily on the choice of K and feature scaling.  
- Can be slower at prediction time for large datasets.  
- Not as interpretable as linear models or trees in terms of specific feature effects.

### Random Forest (RF)

Random Forest is an **ensemble** of Decision Trees trained with **bagging** (bootstrap aggregating):

- Each tree is trained on a random bootstrap sample of the training data.  
- At each split, only a random subset of features is considered.  
- Final predictions are made by **majority vote** across all trees.

Advantages:

- Reduces overfitting compared to a single tree.  
- Handles non-linearities and interactions well.  
- Provides **feature importance** measures based on how much each feature reduces impurity across the forest.

Random Forest often provides **strong baseline performance** with relatively little tuning.

### Gradient Boosting Classifier (GBC)

Gradient Boosting builds an ensemble of **weak learners** (usually shallow decision trees) in a **stage-wise** manner:

- Each new tree is trained to correct the **errors (residuals)** of the previous ensemble.  
- By combining many small improvements, the overall model becomes very powerful.

Key characteristics:

- Often achieves high accuracy on structured/tabular data.  
- More sensitive to hyperparameters (learning rate, number of estimators, tree depth).

In this study, GBC is one of the high-performing ensemble methods on the lung cancer prediction task.

### AdaBoost

AdaBoost (Adaptive Boosting) is another boosting-based ensemble method:

- Starts with a simple base learner (often a shallow decision tree, called a **decision stump**).  
- Iteratively focuses on **previously misclassified** examples by increasing their weights.  
- Aggregates the weak learners using a weighted majority vote.

Properties:

- Often performs well on moderately complex problems.  
- Sensitive to noisy data and outliers because misclassified points receive higher weights.

AdaBoost is included here to compare a classic boosting approach with Gradient Boosting, XGBoost, and CatBoost.

### XGBoost (XGB)

XGBoost (Extreme Gradient Boosting) is a popular, high-performance implementation of gradient boosting for decision trees:

- Optimised for speed and performance, using techniques like **tree pruning**, **regularisation**, and **parallelisation**.  
- Includes **L1/L2 regularisation** and robust handling of missing values.  
- Provides useful diagnostics and feature importance scores.

On many tabular datasets, XGBoost is among the top-performing models. In the original lung cancer study, XGBoost achieved high accuracy, precision, and recall, though it was slightly outperformed by CatBoost.

### CatBoost

CatBoost is a gradient boosting library that is particularly strong on **datasets with many categorical features**. It uses:

- Special techniques for encoding categorical variables (based on ordered target statistics) that reduce overfitting.  
- Symmetric (oblivious) trees that can improve generalisation and inference speed.

Advantages for this study:

- Handles a mix of **categorical and numeric** features naturally.  
- Often requires **less manual preprocessing** of categorical variables compared to other boosting methods.

In the original study, **CatBoost achieved the best overall performance**, with accuracy around **97.2%** and strong precision and recall. This aligns with the general observation that CatBoost works very well on structured clinical data with many categorical variables.

---

Together, these models provide a spectrum from simple, interpretable baselines (Logistic Regression, Decision Tree) to powerful ensembles (Random Forest, Gradient Boosting, XGBoost, CatBoost, AdaBoost). Comparing their performance helps highlight the **benefit of ensemble learning** for early detection of lung cancer using clinical and symptom data.





