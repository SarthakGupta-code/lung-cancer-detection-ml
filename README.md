# Early Detection of Lung Cancer among Indian Patients using Machine Learning Algorithms

This repository is a student-led, reproducible implementation of the published study:

> Gupta, S. (2024). *Early Detection of Lung Cancer among Indian Patients using Machine Learning Algorithms*. *Journal of Student Research*. Study based on primary clinical data from **Neera Hospital, Lucknow, India**. [`file://2383-Article Text-11106-1-10-20240729 (8).pdf`]

All code and notebooks mirror the methodology, models, and key findings using a **synthetic dataset** that matches the structure of the original clinical data.

## Project Overview
- Lung cancer drives a major share of global cancer deaths; fewer than ~16% of cases are detected early.
- In India, cases exceeded ~70,000 in 2022 and may surpass ~80,000 by 2025; five-year survival is ~5% due to late diagnosis.
- Objective: compare multiple ML models for **early detection** using clinical and symptom data from Indian patients to flag high-risk individuals and highlight influential symptoms.

## Dataset Summary
- **Original study data**: 2,512 Indian patients, primary clinical records from **Neera Hospital, Lucknow**.
- **Features (17 total)**: Gender, Age, Smoking, Family History of Cancer, Dyspnea, Chest Pain, Weight Loss, Coughing, Previous Lung Disease, Occupational Hazards, Pollution Level in Residence City, Allergy, Coughing Blood, Immediate Family Smokers, Fatigue, Hoarseness of Voice, Lung Cancer (label).
- **Missing values (original study)**: rows with missing values in key clinical/symptom fields (family history, dyspnea, chest pain, weight loss, previous lung disease, occupational hazards, allergy, immediate family smokers, hoarseness of voice) were dropped.
- **Synthetic dataset here**: `data/synthetic_lung_cancer_data.csv` (~230 rows) mirrors columns and qualitative distributions.

### Data Disclaimer
The dataset included in this repository (`synthetic_lung_cancer_data.csv`) is a synthetic sample, created solely for demonstration and reproducibility.

The actual research study was conducted using primary clinical data from Neera Hospital, Lucknow, covering 2,512 Indian patients, as described in the published paper.

Due to patient privacy, ethics requirements, and data-protection policies, the original clinical dataset cannot be publicly released.

All analyses in this repository replicate the methodology of the published study using synthetic data.

## Methodology
- **Missing values**: drop rows with missing values in the specified clinical/symptom columns (as in the study).
- **Encoding**:
  - Ordinal/label encoding for ordered features: Dyspnea, Chest Pain, Weight Loss, Occupational Hazards, Pollution Level, Hoarseness of Voice.
  - One-hot encoding for nominal features: Gender, Smoking, Family History, Coughing, Previous Lung Disease, Allergy, Coughing Blood, Immediate Family Smokers, Fatigue. Target `Lung Cancer` is mapped to 0/1.
- **Train/test split**: 80/20 stratified split (consistent across models).
- **Models evaluated**: Logistic Regression (LR), Decision Tree (DT), K-Nearest Neighbours (KNN), Random Forest (RF), XGBoost (XGB), Gradient Boosting Classifier (GBC), CatBoost, AdaBoost.
- **Metrics**: Accuracy, Precision, Recall on the held-out test set.

## Results from the Published Study
(Values approximated from the paper [`file://2383-Article Text-11106-1-10-20240729 (8).pdf`])

| Model                    | Accuracy (%) | Precision (%) | Recall (%) |
|--------------------------|--------------|---------------|------------|
| Logistic Regression (LR) | 89.6         | 88.2          | 90.4       |
| Decision Tree (DT)       | 90.1         | 89.5          | 90.8       |
| KNN                      | 91.2         | 90.3          | 92.0       |
| Random Forest (RF)       | 93.3         | 92.5          | 93.9       |
| XGBoost (XGB)            | 95.0         | 94.1          | 95.7       |
| Gradient Boosting (GBC)  | 96.1         | 95.7          | 96.4       |
| **CatBoost**             | **97.2**     | **97.0**      | **97.4**   |
| AdaBoost                 | 95.5         | 95.0          | 95.8       |

- Ensemble methods outperformed non-ensemble baselines.
- CatBoost delivered the best accuracy, precision, and recall.

## Symptoms & Feature Analysis (qualitative highlights)
- **Age**: positive coefficient; older patients at higher risk.
- **Dyspnea**, **Coughing (Yes)**, **Coughing Blood (Yes)**: strong positive signals.
- **Immediate Family Smokers (Yes)**: elevates risk, reflecting second-hand smoke.
- **Smoking (Never Smoker)**: negative coefficient versus current/former smokers.
- **Family History of Cancer (Yes)**: higher probability of lung cancer (~80% higher in study).
- Absence categories (e.g., no chest pain, no weight loss) can appear as negative coefficients.

## Repository Structure
- `data/` – synthetic dataset.
- `notebooks/` – EDA, preprocessing, modelling, and feature-importance analysis (run 01 → 04). Plots are saved to `diagrams/`.
- `src/` – reusable preprocessing, model training, evaluation, and plotting helpers.
- `docs/` – background, dataset description, models explained, symptoms analysis, results summary, limitations/future work, methodology diagram.
- `diagrams/` – Mermaid workflow (`workflow.mmd`) and generated PNGs (model comparison, CatBoost confusion matrix, feature importance).

## How to Run
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
Run notebooks in order (`01` → `04`) to reproduce the workflow. Figures will be written to `diagrams/`.

## Citation
If you use this repository, please cite the original paper:

> Gupta, S. (2024). *Early Detection of Lung Cancer among Indian Patients using Machine Learning Algorithms*. *Journal of Student Research*. Study based on primary clinical data from Neera Hospital, Lucknow. [`file://2383-Article Text-11106-1-10-20240729 (8).pdf`]

This repository provides a synthetic-data replication of the methodology for learning and teaching purposes.
