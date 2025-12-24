## Limitations and Future Work

This section summarises the main limitations of the original lung cancer study and outlines potential directions for future research and model development.

### Limitations

#### 1. Single-Hospital Dataset

- The original clinical data were collected from a **single centre**: Neera Hospital, Lucknow, India.  
- While this provides a detailed view of patients from that hospital’s catchment area, it may not fully represent:
  - Other regions of India with different environmental exposures or healthcare access.  
  - Rural versus urban populations.  
  - Populations treated in tertiary cancer centres versus general hospitals.

As a result, the trained models may have **limited generalisability** when applied directly to other hospitals or regions without further validation.

#### 2. Structured Clinical Data Only (No Imaging)

- The study relied on **structured clinical and symptom data** (e.g., demographics, smoking status, dyspnea, chest pain, weight loss, coughing blood).  
- Important diagnostic information from **imaging modalities** such as chest X‑rays and CT scans was not directly integrated into the models.

This means:

- The models do not capture structural lung changes visible only on imaging.  
- Predictions are based solely on **pre‑imaging information**, which is useful for triage but not a complete diagnostic solution.

#### 3. Limited Sample Size for Complex Models

- Although 2,512 patients is a respectable sample size, it is still **modest** for training very flexible models, especially if there are many categories and interactions.  
- Some patient subgroups (e.g., very young non-smokers or specific occupational exposures) may have **small numbers**, leading to uncertainty in model estimates for those groups.

#### 4. Retrospective Study Design

- The study used **retrospective clinical data**, meaning it looked back at existing records rather than following patients prospectively.  
- Retrospective data can contain:
  - Incomplete records.  
  - Coding differences over time.  
  - Biases in which patients were investigated for lung cancer in the first place.

Such factors can influence model performance and limit **causal interpretation**.

### Future Work

#### 1. Multi-Centre Data Collection

To improve generalisability, future studies should:

- Collect data from **multiple hospitals** across different regions of India (urban and rural).  
- Include both public and private health facilities, and possibly tertiary cancer centres.

This would:

- Provide a more diverse and representative patient cohort.  
- Allow better assessment of how well models transfer across settings.  
- Enable stratified analyses by region, socio-economic status, or hospital type.

#### 2. Integration of Imaging Data

Combining **clinical/symptom data** with **imaging features** has strong potential:

- Imaging modalities such as **chest X‑ray** and **CT scans** can provide detailed information about tumour size, location, and spread.  
- Deep learning or radiomics approaches could extract **quantitative imaging biomarkers**.

Future work could:

- Build **multi‑modal models** that integrate:
  - Demographics and risk factors.  
  - Symptoms and clinical history.  
  - Imaging-derived features.

This may lead to more accurate and robust early detection tools.

#### 3. Exploration of Genetic and Familial Risk

- The study suggests that **family history of cancer** and **immediate family smokers** are important predictors.  
- However, more detailed work on **genetic factors** and specific familial risk patterns is still needed.

Future directions:

- Incorporate **genetic or genomic data** (where feasible and ethically approved).  
- Study interactions between **genetic predisposition**, **smoking behaviour**, and **environmental exposures**.

#### 4. Prospective Validation and Clinical Integration

Before any model can be used in clinical practice, it should undergo:

- **Prospective validation** in real-world clinical workflows.  
- Evaluation of metrics such as:
  - Calibration (do predicted probabilities match observed outcomes?).  
  - Impact on referral patterns and diagnostic delays.  
  - Acceptability to clinicians and patients.

In practical use, models should:

- Be integrated as **decision-support tools** that:
  - Flag high-risk patients for earlier investigation.  
  - Provide transparent explanations of key risk factors.  
- Never be used as a **replacement for clinician judgement** or as the sole basis for diagnosis or treatment decisions.

### Summary

The current work demonstrates that machine learning models, especially ensemble methods like CatBoost, can achieve strong diagnostic performance using routine clinical and symptom data. However, to move from research to practice, further steps are needed:

- Multi-centre, larger-scale data collection.  
- Integration of imaging and potentially genetic information.  
- Rigorous prospective validation and careful clinical deployment.

The synthetic implementation in this repository provides a reproducible foundation for exploring these ideas and developing more advanced early detection tools in the future.





