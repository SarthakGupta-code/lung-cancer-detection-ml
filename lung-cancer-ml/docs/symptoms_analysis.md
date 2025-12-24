## Symptoms and Risk Factor Analysis

This document summarises how key symptoms and risk factors relate to lung cancer risk in the original study, primarily based on **logistic regression coefficients** and **feature importance** from ensemble models. The analysis is reproduced qualitatively using synthetic data in this repository.

### Approximate Logistic Regression Coefficients

In the original analysis, a logistic regression model was fitted after appropriate encoding of features. The following coefficients (approximate values) were reported for some key predictors:

- **Age**: +0.13  
- **Dyspnea**: +0.69  
- **Chest Pain (None)**: –1.13  
- **Coughing (Yes)**: +1.44  
- **Immediate Family Smokers (Yes)**: +1.71  
- **Hoarseness of Voice (None)**: –0.64  
- **Hoarseness of Voice (Moderate)**: +0.83  
- **Family History of Cancer (Yes)**: +0.86  
- **Weight Loss (No)**: –1.07  
- **Coughing Blood (Yes)**: +1.78  
- **Smoking (Never Smoker)**: –1.31

Positive coefficients indicate that higher values (or presence of the category) are associated with **increased odds of lung cancer**, while negative coefficients indicate **decreased odds** relative to the reference.

### Interpretation of Key Predictors

#### Age

- **Coefficient: +0.13**  
- Interpretation: As **age increases**, the modelled probability of lung cancer **increases**.  
- Clinical context: Lung cancer is more common in older adults, reflecting cumulative exposure to risk factors such as smoking and pollution over time.

#### Dyspnea (Shortness of Breath)

- **Coefficient: +0.69** (for higher levels of dyspnea).  
- Interpretation: Patients with **more severe dyspnea** are more likely to have lung cancer compared to those without dyspnea.  
- Clinical context: Dyspnea is a common symptom of advanced or centrally located lung tumours, but can also be caused by many non-cancerous respiratory conditions. In combination with other risk factors (e.g., smoking), it becomes more concerning.

#### Chest Pain

- **Coefficient for Chest Pain (None): –1.13**.  
- Interpretation: Patients **without chest pain** are less likely to have lung cancer compared to certain reference categories with pain.  
- Clinical context: While chest pain can be a symptom of lung cancer, many patients may present primarily with cough, dyspnea, or weight loss. The negative coefficient for “None” suggests that **absence of chest pain** is associated with a lower predicted risk in the model.

#### Coughing

- **Coefficient for Coughing (Yes): +1.44**.  
- Interpretation: Presence of a **persistent cough** substantially increases the odds of lung cancer relative to those without cough.  
- Clinical context: Chronic cough is one of the classic presenting symptoms of lung cancer, especially in smokers or patients with other respiratory risk factors.

#### Coughing Blood (Hemoptysis)

- **Coefficient for Coughing Blood (Yes): +1.78**.  
- Interpretation: **Coughing up blood** is one of the strongest positive predictors in the model.  
- Clinical context: Hemoptysis is a serious symptom that often prompts urgent evaluation. While not specific to lung cancer, its presence in an at-risk individual significantly raises suspicion.

#### Weight Loss

- **Coefficient for Weight Loss (No): –1.07**.  
- Interpretation: Patients **without weight loss** have a lower predicted risk of lung cancer compared to those with weight loss.  
- Clinical context: Unintentional weight loss is a well-known “red flag” symptom in many cancers, including lung cancer. Its absence can modestly lower suspicion, although not completely rule out disease.

#### Hoarseness of Voice

- **Coefficient for Hoarseness of Voice (None): –0.64**  
- **Coefficient for Hoarseness of Voice (Moderate): +0.83**  
- Interpretation:  
  - **No hoarseness** is associated with a lower risk of lung cancer.  
  - **Moderate hoarseness** increases the modelled risk, possibly reflecting involvement of structures near the vocal cords or recurrent laryngeal nerve.

#### Smoking and Second-Hand Smoke

- **Smoking (Never Smoker): –1.31**  
  - Interpretation: Being a **never-smoker** is associated with **lower risk** relative to smokers (current or former).  
  - Clinical context: This aligns with the established role of active tobacco smoking as the primary risk factor for lung cancer.

- **Immediate Family Smokers (Yes): +1.71**  
  - Interpretation: Having immediate family members who smoke was associated with **higher odds** of lung cancer (roughly 1.7× higher in the original analysis).  
  - Clinical context: This likely reflects **second-hand smoke exposure** and shared environmental or lifestyle factors within families.

#### Family History of Cancer

- **Coefficient for Family History of Cancer (Yes): +0.86**  
- Interpretation: Patients with a **family history of cancer** have substantially higher predicted risk (roughly 80% higher odds) of lung cancer in the model.  
- Clinical context: This may capture genetic predisposition and shared environmental factors, although it is not specific to lung cancer alone.

### Summary of Patterns

Overall, the symptom and risk factor analysis confirms several well-known associations:

- **Older age**, **active smoking**, and **second-hand smoke exposure** (immediate family smokers) are key risk factors.  
- Respiratory symptoms such as **cough**, **dyspnea**, **hoarseness of voice**, and especially **coughing blood** are strong positive signals once present.  
- **Family history of cancer** adds to the risk profile.  
- The **absence** of some critical symptoms (e.g., **no chest pain**, **no weight loss**) and being a **never‑smoker** are associated with **lower risk**.

### Relation to Feature Importance from Ensemble Models

In the notebooks, ensemble models such as Random Forest, XGBoost, and CatBoost provide **feature importance scores**. While these scores are not directly comparable to logistic regression coefficients, the high-importance features typically include:

- **Smoking status**  
- **Immediate Family Smokers**  
- **Family History of Cancer**  
- **Dyspnea** and **Coughing**  
- **Coughing Blood**  
- **Age**

This agreement between regression coefficients and feature importance plots increases confidence that the models are capturing meaningful, **clinically plausible** patterns in the data.

### Clinical Perspective

From a clinical standpoint, these results support using ML-based tools to:

- Highlight patients with high-risk combinations (e.g., **older age + current smoker + chronic cough + dyspnea + family smokers**).  
- Encourage **earlier imaging and specialist referral** for such patients.  
- Provide transparent explanations (via coefficients or feature importance) that clinicians can relate to established medical knowledge.

However, ML outputs should always be interpreted **alongside clinical judgement**, not in isolation, and any automated risk scores should be validated prospectively before being used in routine care.





