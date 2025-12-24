## Dataset Description

This repository reproduces, using **synthetic data**, the structure and methodology of a clinical study conducted at **Neera Hospital, Lucknow, India**.

### Original Clinical Dataset (Study Data)

- **Source**: Neera Hospital, Lucknow, India.  
- **Population**: **2,512 Indian patients** evaluated for possible lung cancer.  
- **Data type**: Structured tabular data (no images), including demographics, clinical history, and presenting symptoms.  
- **Target label**: Whether the patient was diagnosed with **lung cancer** (Yes/No).

The main goal of the original dataset was to support early detection of lung cancer by learning patterns in routine clinical and symptom data.

### Features Collected

The original study used 17 features. The synthetic dataset in `data/synthetic_lung_cancer_data.csv` follows the same naming and approximate semantics.

1. **Gender**  
   - Sex of the patient, typically recorded as **Male** or **Female**.

2. **Age**  
   - Age of the patient in years (integer).  
   - In the underlying population, lung cancer cases were more common among older adults.

3. **Smoking**  
   - Smoking status with categories such as:
     - **Never Smoker**
     - **Former Smoker**
     - **Current Smoker**
   - Smoking is one of the strongest known risk factors for lung cancer.

4. **Family History of Cancer**  
   - Whether any **close family members** (e.g., parents, siblings) have had cancer.  
   - Coded as **Yes** or **No**.

5. **Dyspnea**  
   - Shortness of breath, recorded with an **ordered severity scale**, for example:
     - None  
     - Mild  
     - Moderate  
     - Severe

6. **Chest Pain**  
   - Presence and, if present, severity of chest pain:
     - None  
     - Mild  
     - Moderate  
     - Severe

7. **Weight Loss**  
   - Recent unintentional weight loss:
     - None  
     - Mild  
     - Marked

8. **Coughing**  
   - Presence of cough at presentation, coded as **Yes** or **No**.

9. **Previous Lung Disease**  
   - History of prior lung diseases such as **COPD, tuberculosis (TB)**, or other chronic respiratory conditions.  
   - Encoded as **Yes** or **No**.

10. **Occupational Hazards**  
    - Occupational exposure relevant to lung cancer risk, such as dust, fumes, or chemicals.  
    - Represented using levels that can be ordered (e.g., None, Low, Moderate, High).

11. **Pollution Level in Residence City**  
    - Approximate level of air pollution in the patient’s usual place of residence:  
      - Low  
      - Moderate  
      - High  
    - Treated as an ordered categorical variable.

12. **Allergy**  
    - Presence of relevant allergies (e.g., chronic allergic rhinitis or other respiratory allergies).  
    - Encoded as **Yes** or **No**.

13. **Coughing Blood**  
    - Whether the patient reports coughing up blood (**hemoptysis**).  
    - Encoded as **Yes** or **No**.

14. **Immediate Family Smokers**  
    - Whether immediate family members (e.g., people living with the patient) are smokers.  
    - Encoded as **Yes** or **No**.  
    - Reflects **second-hand smoke exposure**.

15. **Fatigue**  
    - Persistent tiredness or fatigue, encoded as **Yes** or **No**.

16. **Hoarseness of Voice**  
    - Changes in voice quality, on an ordered scale:
      - None  
      - Mild  
      - Moderate  
      - Severe

17. **Lung Cancer**  
    - **Target label** indicating whether lung cancer is present.  
    - Recorded as **Yes** or **No** in the raw dataset; usually later encoded as 0/1 for modelling.

### Missing Values in the Original Dataset

In the original clinical dataset from Neera Hospital, several variables had missing values:

- **Family History of Cancer**: 74 missing  
- **Dyspnea**: 14 missing  
- **Chest Pain**: 121 missing  
- **Weight Loss**: 182 missing  
- **Previous Lung Disease**: 119 missing  
- **Occupational Hazards**: 135 missing  
- **Allergy**: 67 missing  
- **Immediate Family Smokers**: 102 missing  
- Other columns had **no missing values**.

#### Handling of Missing Values

To keep the analysis simple and transparent, the study used **row-wise deletion** for records with missing values in the above fields:

- Any row with a missing value in **Family History of Cancer**, **Dyspnea**, **Chest Pain**, **Weight Loss**, **Previous Lung Disease**, **Occupational Hazards**, **Allergy**, or **Immediate Family Smokers** was **dropped** from the dataset before model training.
- This approach avoids imputing clinical values but reduces the effective sample size.

In this repository’s code and notebooks, we reproduce that behaviour programmatically using pandas: we drop rows with missing values in this specified subset of columns before performing encoding and model training.

### Encoding Strategy

To make the dataset suitable for machine learning algorithms, the following encoding strategy was used in the original study and is replicated here:

- **Label Encoding (Ordinal)**
  - Applied to variables with a **natural order**:
    - Dyspnea  
    - Chest Pain  
    - Weight Loss  
    - Occupational Hazards  
    - Pollution Level in Residence City  
    - Hoarseness of Voice
  - Each level is mapped to an integer that reflects its order (e.g., None = 0, Mild = 1, Moderate = 2, Severe = 3).

- **One‑Hot Encoding (Nominal)**
  - Applied to variables with **no natural order**:
    - Gender  
    - Smoking  
    - Family History of Cancer  
    - Coughing  
    - Previous Lung Disease  
    - Allergy  
    - Coughing Blood  
    - Immediate Family Smokers  
    - Fatigue  
    - Lung Cancer (label) for some models (otherwise stored as a single binary column).
  - Each category becomes its own binary indicator column (0/1).

This combination preserves clinically meaningful order information where appropriate while giving flexible, model-agnostic inputs for algorithms like logistic regression and tree‑based ensembles.

### Synthetic Dataset in this Repository

The file `data/synthetic_lung_cancer_data.csv` is a **synthetic sample dataset** with approximately 200–300 rows. It is constructed to:

- Mirror the **feature names and data types** described above.  
- Use **realistic but clearly artificial** distributions:
  - Ages between 20 and 85, with older ages more common among synthetic lung cancer cases.  
  - Higher probability of **Lung Cancer = Yes** when:
    - Smoking is **Current** or **Former**.  
    - **Immediate Family Smokers = Yes**.  
    - **Family History of Cancer = Yes**.  
    - Dyspnea, Chest Pain, Weight Loss, and Coughing Blood severities are higher.
- Maintain a **reasonable class balance** so that both Lung Cancer = Yes and No are well represented.

Although this dataset is designed to behave qualitatively like the original clinical data, it **does not contain any real patient information**.

### Data Disclaimer

**Data Disclaimer**  
The dataset included in this repository (`synthetic_lung_cancer_data.csv`) is a **synthetic sample**, created solely for demonstration and reproducibility.  
The actual research study was conducted using **primary clinical data from Neera Hospital, Lucknow**, covering **2,512 Indian patients**, as described in the published paper.  
Due to patient privacy, ethics requirements, and data-protection policies, the original clinical dataset **cannot be publicly released**.  
All analyses in this repository replicate the methodology of the published study using synthetic data.





