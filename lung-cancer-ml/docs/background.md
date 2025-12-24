## Background

Lung cancer is one of the leading causes of cancer-related deaths worldwide. Around 2020, there were roughly **10 million cancer deaths globally**, and lung cancer accounted for a substantial share of these deaths. Despite advances in imaging, chemotherapy, radiotherapy, and targeted therapies, **fewer than 16% of lung cancer cases are detected at an early stage**. As a result, many patients are diagnosed late and die within a year of diagnosis.

### Lung Cancer in the Indian Context

In India, lung cancer has emerged as a major public health concern:

- Over **~70,000** new lung cancer cases were estimated in 2022.  
- The number of cases is projected to exceed **~80,000** by 2025.  
- Lung cancer is among the most common cancers in Indian males.  
- The **five-year survival rate** for lung cancer in developing countries such as India is very low, around **5%**.

Several factors contribute to this poor outlook:

- High prevalence of **tobacco smoking** and **second-hand smoke** exposure.  
- Environmental exposures, including **air pollution** in urban areas and **occupational hazards** such as dust, fumes, and industrial chemicals.  
- Delayed presentation to healthcare facilities, often due to limited awareness, socio-economic barriers, and access to specialised care.

### Importance of Early Diagnosis

Lung cancer has a much better prognosis when detected early. Early-stage disease can often be treated with surgery and/or curative radiotherapy, sometimes combined with systemic therapy. However, **many Indian patients present with advanced-stage disease**, where:

- Treatment options are more aggressive and expensive.  
- The likelihood of long-term survival is substantially lower.  
- The burden on patients, families, and the health system is very high.

This creates a strong motivation to improve **early detection** and **risk stratification**, especially in resource-constrained settings.

### Motivation for Using Machine Learning

In typical clinical practice, physicians evaluate a combination of:

- Demographic factors (e.g., age, gender).  
- Lifestyle factors (e.g., smoking status, occupational exposures).  
- Clinical history (e.g., previous lung disease, family history of cancer).  
- Presenting symptoms (e.g., cough, dyspnea, chest pain, weight loss, hemoptysis).

While individual risk factors are well known, it can be challenging to integrate many variables at once and to recognise subtle combinations of symptoms that might signal increased lung cancer risk—especially in busy outpatient settings.

**Machine learning (ML)** methods are well suited for:

- Learning complex patterns and interactions among many variables.  
- Providing **probabilistic risk scores** rather than a simple yes/no decision.  
- Helping clinicians prioritise which patients might benefit from further diagnostic work‑up (e.g., imaging, specialist referral).

The study reproduced in this repository explores a range of classical ML algorithms applied to **structured clinical and symptom data** collected from Indian patients treated at **Neera Hospital, Lucknow**. The objective is to:

- Identify individuals at higher risk of lung cancer based on routinely collected data.  
- Identify the **most informative symptoms and risk factors** for lung cancer in this population.  
- Compare a set of ML models and understand which approaches yield the best diagnostic performance.

### Role of ML in Clinical Practice

It is important to emphasise that ML models are intended to function as **decision-support tools**, not as replacements for clinicians. In a practical deployment scenario, such models could:

- Flag **high-risk patients** for early imaging or specialist referral.  
- Highlight **key risk factors** contributing to an individual patient’s risk score.  
- Support hospitals and clinicians in developing **evidence-informed triage pathways** for lung cancer.

However, any such system must be:

- Carefully validated in diverse patient populations.  
- Integrated into clinical workflows in a way that supports, rather than burdens, healthcare providers.  
- Transparent about its limits and uncertainties.

The rest of this repository demonstrates, using synthetic data, how such a pipeline can be built and evaluated in a reproducible way.





