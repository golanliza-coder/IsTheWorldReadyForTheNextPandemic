
# Project Name: IsTheWorldReadyForTheNextPandemic?
                IsTheWorldReadyForTheNextPandemic aim to check how the world is managing or can handle Pandemic

## Team Members
* **Liza Golan** - Data Scientist Student
* **Ravit Bar-Lev** - Data Scientist Student
* **Hagit Niv-Drori** - Data Scientist Student
* **Hodaya Zinowits** - Data Scientist Student

---

## 1. Project Goal & Business/Research Problem
### What does this project solve?
The project examines the preparedness of countries worldwide for the next global pandemic by integrating global health variables and comparing them against a binary indicator—1 (prepared) or 0 (unprepared)—of a country's readiness to handle a global pandemic.

### Why is this important?
It is important beacuse it assesses the preparedness of countries worldwide by combining the following global health variables:
* Healthcare system resilienc
* Monitoring and early detection capabilities
* Technology adoption
* Demographic and geographic vulnerability

and by utilizing historical data regarding the response to the COVID-19 pandemic between 2019 and 2022.

---

## 2. Data Description & Sources
The project integrates multiple comprehensive datasets tracking global health security, demographic trends, and epidemiology:
* **`2021-GHS-Index-April-2022.csv`**: Global Health Security (GHS) Index scores tracking countries' capacities to prevent, detect, and respond to health emergencies.
* **`health.csv`**: Country-level public health metrics including life expectancy, smoking/diabetes prevalence, mortality rates, health expenditures (USD), and healthcare capacity (beds, physicians, nurses).
* **`demographics.csv`**: Detailed demographic breakdowns including total population, urban vs. rural ratios, density, Human Development Index (HDI), and specific age distribution brackets.
* **`WHO-COVID-19-global-daily-data.csv` & `epidemiology.csv`**: Time-series records of daily new and cumulative COVID-19 cases, deaths, and testing outputs.
* **`vaccinations.csv`**: Longitudinal data tracking vaccine rollout doses, individuals vaccinated, and specific vaccine manufacturers (Pfizer, Moderna, Janssen, etc.).
* **`ict adoption by 100 people.csv`**: Technology adoption metrics tracking fixed-line, mobile, broadband, and internet usage rates per 100 people over time.
* **`country Index.csv`**: Geographic reference table mapping location keys to country names and administrative subregions.

**Comment:** - Due to its huge size and size limitation in GitHub, data files for `vaccinations.csv`and `epidemiology.csv` are located in google drive share 
location '/content/drive/MyDrive/DS_IsTheWorldReadyForTheNextPandemic/DATASET TO USE/'


### Data Sources:
Our dataset files were driven from different resources. Below you can find files per resource:
* **`WHO` site**: `WHO-COVID-19-global-daily-data.csv`.
* **`Google Open Date` site**: `country Index.csv`, `demographics.csv`,`epidemiology.csv`,`health.csv` and `vaccinations.csv`.
* **`GHSI` site**: `2021-GHS-Index-April-2022.csv`.
* **`https://ourworldindata.org` site**: `ict adoption by 100 people.csv`.


---

## 3. Approach & Methodology
Our workflow follows the standard crisp-dm framework for data science projects:
1. **Data Integration & Cleaning**: Merging datasets using `location_key` or `Country_code` as relational anchors, handling missing structural information, and aligning dates for time-series features.
2. **Exploratory Data Analysis (EDA)**: Investigating correlations between healthcare expenditure, digital adoption, and pandemic outcomes. Visualizing feature distributions.
3. **Feature Engineering**: Analyze what are the most important/effective features to used during modeling that answer the research query.

    Nine are in used:
    
    X1 - Hospital beds per 1,000 inhabitants (%) ; X2 - Physicians per 1,000 inhabitants (%) ; X3 - "Early Detection & Reporting" score from the GHS Index

    X4 - COVID-19 testing rate in 2021 per 1,000 people (%); X5 - Overall GHSI score ; X6 - Percentage of internet users in the country (%)

    X7 - Percentage of the population aged 60+ (%) ; X8 - Prevalence of smokers in the population (%) ; X9 - Prevalence of diabetes in the population (%)

4. **Predictive Modeling**: TBD.


---

## 4. Workflow Overview
* `00_First_Analysis_IsTheWorldReadyForTheNextPandemic.ipynb`: Initial data analysis and missing value imputation.
* `01_Merge_and_Statistic_IsTheWorldReadyForTheNextPandemic.ipynb`: Preparation of the actual base dataset which trainig model will run upon - align per Country code.
* `02_Merge_Static_Base_IsTheWorldReadyForTheNextPandemic.ipynb`: Running of a comprehensive Exploratory Data Analysis on base dataSet ready for modeling + descriptive statistic.
* `03_Merge_Static_Base_IsTheWorldReadyForTheNextPandemic.ipynb`: Re-arrange base data by aligning it to be yearly based and prepare it for data modeling.
* `04_The Feature Matrix_of_IsTheWorldReadyForTheNextPandemic.ipynb`: Feature matrix of the model.
* `05_Logistic Regression_Vs_ Random Forrest_IsTheWorldReadyForTheNextPandemic.ipynb`: Model training - Random Forest Classifier vs Logistic Regression, confusion matrix,Scatter Plot and Violin Plot.

---

## 5. Models Tested & Results (TBD)
* **Logistic Regression**: Used for predicting ***.
* **Random Forest Classifier**: Used for .


---

## 6. Main Results
Main analysis results...

---

## 7. Running Instructions
Main analysis results...

---

## 8. Repository Structure
```text
├── data/                          # CSV files (demographics, health, epidemiology, etc.)
├── notebooks/                     # Jupyter Notebooks for analysis steps
│   ├── 01_eda_and_cleaning.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_modeling_and_evaluation.ipynb
├── src/                           # Custom python modules for data loading/helpers
├── README.md                      # Main project documentation
└── requirements.txt               # Dependencies file

---


## 9. Next Steps...
Main analysis results...

---
