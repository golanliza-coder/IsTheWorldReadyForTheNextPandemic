
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
* **`vaccinations.csv`**: Time series data tracking vaccine rollout doses, individuals vaccinated, and specific vaccine manufacturers (Pfizer, Moderna, Janssen, etc.).
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
    Three files were modified and time series were removed from there and replaced by Year. Those files are: `epidemiology.csv`, `vaccinations.csv` and `WHO-COVID-19-global-daily-data.csv.
2. **Exploratory Data Analysis (EDA)**: 
    2.1 Merging `health` and `demographic`csv files in order to get X1 and X2 features.
    2.2 Pull X3 feature from `GHS-Index`csv file.
    2.3 Merging `epidemiology` and `demographics`csv files in order to calculate X4 feature.
    2.4 Pull in X5 feature from `GHSI`csv file.
    2.5 Merging `GHS-Index` and `ICT_Adoption`csv files in order to get X6 feature.
    2.6 Merging `epidemiology` and `demographics`csv files in order to get X7 feature.
    2.7 Pull in X8 and X9 features from `demographics`csv file.
    
3. **Feature Engineering**: Analyze what are the most important/effective features to used during modeling that answer the research query.

    Nine are in used:
    
    X1 - Hospital beds per 1,000 inhabitants (%)

    X2 - Physicians per 1,000 inhabitants (%) 

    X3 - "Early Detection & Reporting" score from the GHS Index

    X4 - COVID-19 testing rate in 2021 per 1,000 people (%)

    X5 - Overall GHSI score 

    X6 - Percentage of internet users in the country (%)
    
    X7 - Percentage of the population aged 60+ (%) 

    X8 - Prevalence of smokers in the population (%) 

    X9 - Prevalence of diabetes in the population (%)

4. **Predictive Modeling**: 
    
    While Y equal 1 - The country is ready for future world academic.

    While Y equal 0 - The country is not ready for future world academic.

    When country's mortality is greater than the international median mortality then the country is not ready for world academic [Y=0].

    When country's mortality is less than the international median mortality then the country is ready for world academic [Y=1].


---

## 4. Workflow Overview
* `00_First_Analysis_IsTheWorldReadyForTheNextPandemic.ipynb`: Initial data analysis and missing value imputation.
* `01_Merge_and_Statistic_IsTheWorldReadyForTheNextPandemic.ipynb`: Preparation of the actual base dataset which trainig model will run upon - align per Country code.
* `02_Merge_Static_Base_IsTheWorldReadyForTheNextPandemic.ipynb`: Running of a comprehensive Exploratory Data Analysis on base dataSet ready for modeling + descriptive statistic.
* `03_Merge_Static_Base_IsTheWorldReadyForTheNextPandemic.ipynb`: Re-arrange base data by aligning it to be yearly based and prepare it for data modeling.
* `04_The Feature Matrix_of_IsTheWorldReadyForTheNextPandemic.ipynb`: Feature matrix of the model.
* `05_Logistic Regression_Vs_ Random Forrest_IsTheWorldReadyForTheNextPandemic.ipynb`: Model training - Random Forest Classifier vs Logistic Regression, confusion matrix,Scatter Plot and Violin Plot.

---

## 5. Models Tested & Results
Following Supervised modeling were used
* **Logistic Regression**
* **Random Forest Classifier** - this one was given the best accuracy - 83.32%.


---

## 6. Main Results
Main analysis results are as follow

### 📊 טבלת השוואה רשמית: מודל הבסיס מול המודל המתקדם (ממוצע ± סטיית תקן)

| Metric / מדד ביצוע | Logistic Regression (Baseline) | Random Forest (Winner 🏆) |
| :--- | :---: | :---: |
| 📈 דיוק כללי (Accuracy) | 81.36% (±4.80%) | **83.55% (±4.11%)** |
| 🎯 ציון F1-Score | 81.49% (±5.23%) | **83.30% (±4.45%)** |
| 🔍 רגישות (Recall) | **82.64% (±9.56%)** | 82.36% (±8.51%) |
| 📍 דיוק הסיווג (Precision) | 81.24% (±5.80%) | **85.23% (±6.47%)** |

---

## 7. Running Instructions [TBD]
Whatneed to be added?...

---

## 8. Repository Structure
```text

📁 Repository Structure / מבנה התיקייה
├── 📁 Presentation/                                                    # Main Project presentation
├── 📁 data/                                                            # CSV files (demographics, health, epidemiology, etc.)
│   ├── 📁 processed/
│   ├── 📁 raw/
│   └── 📄 data_disctionary_MiniProject.md
├── 📁 notebooks/                                                        # Jupyter Notebooks for analysis steps
│   ├── 📄 00_First_Analysis_IsTheWorldReadyForTheNextPandemic.ipynb
│   ├── 📄 01_Merge_and_Statistic_IsTheWorldReadyForTheNextPandemic.ipynb
│   ├── 📄 02_Merge_Static_Base_IsTheWorldReadyForTheNextPandemic.ipynb
│   ├── 📄 03_Merge_Static_Base_IsTheWorldReadyForTheNextPandemic.ipynb
│   ├── 📄 04_The Feature Matrix_of_IsTheWorldReadyForTheNextPandemic.ipynb
│   └── 📄 05_Logistic Regression_Vs_Random Forrest_IsTheWorldReadyForTheNextPandemic.ipynb
├── 📁 reports/
├── 📁 src/                                                             # Optional - Custom python modules for data loading/helpers
├── 📄 Mid-Proj_README.md                                               # Main project documentation
└── 📄 requirements.txt                                                 # Dependencies file

```

---


## 9. Next Steps... [TBD]
Main analysis results...

---
