## Results Summary

This document summarises the comparative performance of different machine learning models for predicting lung cancer using structured clinical and symptom data. The values below are the **approximate metrics** reported in the original study; the synthetic implementation in this repository will produce similar but not identical numbers.

### Comparative Performance of Models

The original study evaluated eight models using **Accuracy**, **Precision**, and **Recall** as the main metrics:

| Model        | Accuracy | Precision | Recall |
|-------------|----------|-----------|--------|
| Logistic Regression (LR) | 0.9277 | 0.8955 | 0.9090 |
| Decision Tree (DT)       | 0.8111 | 0.7285 | 0.7727 |
| K‑Nearest Neighbours (KNN) | 0.8277 | 0.7777 | 0.7424 |
| Random Forest (RF)       | 0.9389 | 0.9365 | 0.8939 |
| XGBoost (XGB)            | 0.9333 | 0.9218 | 0.8939 |
| Gradient Boosting (GBC)  | 0.9611 | 0.9836 | 0.9090 |
| CatBoost                 | **0.9722** | **0.9692** | **0.9545** |
| AdaBoost                 | 0.9555 | 0.9393 | 0.9393 |

These results show a **clear performance hierarchy**:

- Classical, non-ensemble models (Logistic Regression, Decision Tree, KNN) achieve **reasonable** performance, with Logistic Regression doing particularly well among them.  
- **Ensemble models** (Random Forest, XGBoost, Gradient Boosting, CatBoost, AdaBoost) consistently outperform the simpler models.  
- **CatBoost** achieved the **best overall performance**, with accuracy around 97.2% and strong precision and recall, indicating both low false-positive and low false-negative rates.

### Key Findings

- **Ensemble methods excel**:  
  - Random Forest, XGBoost, Gradient Boosting, CatBoost, and AdaBoost all achieved accuracies above 0.93.  
  - They were especially strong on **precision and recall**, which are critical in medical diagnostic settings where both false positives and false negatives matter.

- **CatBoost as top performer**:  
  - CatBoost achieved the highest accuracy (~0.9722) and very strong precision (~0.9692) and recall (~0.9545).  
  - Its ability to handle categorical variables effectively and model complex interactions likely contributed to its superior performance on this structured dataset.

- **Logistic Regression remains competitive**:  
  - Despite its simplicity, Logistic Regression achieved accuracy above 0.92, making it a strong baseline.  
  - Its interpretability and directly interpretable coefficients make it valuable for understanding **which symptoms and risk factors drive predictions**.

- **Decision Tree and KNN are less robust**:  
  - The single Decision Tree model had lower accuracy and precision, likely due to overfitting and instability.  
  - KNN performance was moderate and sensitive to the choice of K and feature scaling.

### Synthetic Implementation in this Repository

In this repository:

- We train the same eight models on a **synthetic dataset** that mirrors the structure and qualitative relationships of the original clinical data.  
- The exact metrics obtained on synthetic data will differ but are set up so that:
  - **Ensemble models still outperform** Logistic Regression, Decision Tree, and KNN on average.  
  - **CatBoost** remains among the **top-performing models**.

The notebook `03_model_training_and_evaluation.ipynb`:

- Trains all models on the processed synthetic data.  
- Computes and displays accuracy, precision, and recall for each model.  
- Produces:
  - A comparison table analogous to the one above.  
  - A bar chart of model accuracies.  
  - A confusion matrix for the best-performing model (usually CatBoost in this setup).

### Clinical Interpretation

From a clinical standpoint, the results suggest that:

- Modern ensemble techniques, particularly **gradient-boosted trees** and **CatBoost**, can achieve high diagnostic performance on structured clinical and symptom data.  
- Such models could be used to **flag high-risk patients** during routine visits, prompting clinicians to consider early imaging or specialist referral.  
- At the same time, **simpler models** like Logistic Regression still provide **useful, interpretable baselines** and can help validate that the ML findings align with established medical knowledge.

Any real-world deployment would require:

- Further validation on **larger, multi-centre datasets**.  
- Careful evaluation of calibration, fairness, and generalisability.  
- Integration into clinical workflows in a way that supports, rather than replaces, clinician decision-making.





