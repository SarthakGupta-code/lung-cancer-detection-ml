## Methodology and Workflow

This document describes the overall methodology used in the lung cancer prediction study and provides a visual summary using a **Mermaid workflow diagram**.

### Textual Workflow Description

1. **Raw Patient Data Collection**  
   - Clinical and symptom data are collected from patients at **Neera Hospital, Lucknow**, including demographics, smoking history, family history, respiratory symptoms, and other risk factors.  
   - The original study used primary clinical data from **2,512 Indian patients**.

2. **Preprocessing and Cleaning**  
   - Data are loaded from the hospital’s records into a structured tabular format.  
   - Records with missing values in key variables (family history, dyspnea, chest pain, weight loss, previous lung disease, occupational hazards, allergy, immediate family smokers) are **dropped**.  
   - Categorical variables are inspected and harmonised (e.g., consistent labels for smoking status or symptom levels).

3. **Encoding of Features**  
   - **Ordinal (label) encoding** is applied to variables with a natural order, such as Dyspnea, Chest Pain, Weight Loss, Occupational Hazards, Pollution Level in Residence City, and Hoarseness of Voice.  
   - **One‑hot encoding** is applied to nominal categorical variables like Gender, Smoking, Family History of Cancer, Coughing, Previous Lung Disease, Allergy, Coughing Blood, Immediate Family Smokers, Fatigue, and (for some models) the Lung Cancer label.

4. **Train/Test Split**  
   - The processed dataset is split into **training** and **testing** subsets (e.g., 80% train, 20% test), typically using a **stratified** split to preserve the proportion of Lung Cancer = Yes/No cases.  
   - The training data are used to fit the models; the test data are held out for unbiased evaluation.

5. **Model Training**  
   - Multiple machine learning algorithms are trained on the training set, including:  
     - Logistic Regression (LR)  
     - Decision Tree (DT)  
     - K‑Nearest Neighbours (KNN)  
     - Random Forest (RF)  
     - XGBoost (XGB)  
     - Gradient Boosting Classifier (GBC)  
     - CatBoost  
     - AdaBoost  
   - Hyperparameters are chosen to reflect standard, robust configurations rather than heavily tuned competition settings.

6. **Model Evaluation**  
   - On the test set, each model is evaluated using:  
     - **Accuracy** – overall fraction of correctly classified patients.  
     - **Precision** – fraction of predicted positive cases that are truly positive.  
     - **Recall** – fraction of true positive cases that are correctly identified.  
   - A comparison table is created, and performance is visualised (e.g., bar charts, confusion matrices).

7. **Symptom and Feature Analysis**  
   - Logistic Regression coefficients are examined to understand how each feature (e.g., age, dyspnea, smoking status, family history) affects the modelled odds of lung cancer.  
   - Feature importance scores from ensemble models (e.g., Random Forest, XGBoost, CatBoost) are used to identify which variables contribute most to predictive performance.

8. **Insights and Conclusions**  
   - The best‑performing models (particularly **ensemble methods**, with **CatBoost** as a top performer) are highlighted.  
   - Key risk factors and symptoms (e.g., smoking, second-hand smoke, coughing blood, dyspnea, age, family history) are summarised.  
   - Limitations of the single-centre dataset and the need for multi-centre, multi‑modal validation studies are discussed.

### Mermaid Workflow Diagram

The following Mermaid diagram (stored as `diagrams/workflow.mmd`) visualises the workflow described above.

```mermaid
flowchart TD

    A[Raw Patient Data<br/>Neera Hospital (Primary Clinical Data)] --> B[Preprocessing<br/>Missing Value Removal<br/>Encoding]

    B --> C[Train/Test Split]

    C --> D[Model Training<br/>LR, DT, KNN, RF, XGB, GBC, CatBoost, AdaBoost]

    D --> E[Model Evaluation<br/>Accuracy, Precision, Recall]

    E --> F[Symptom & Feature Analysis<br/>Regression Coefficients<br/>Feature Importances]

    F --> G[Insights & Conclusions<br/>Support Earlier Diagnosis]
```

This diagram is also available in the `diagrams/` folder as a standalone `.mmd` file that can be rendered by tools supporting Mermaid.





