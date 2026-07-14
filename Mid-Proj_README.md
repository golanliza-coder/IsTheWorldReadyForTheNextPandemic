
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
The COVID-19 pandemic highlighted massive disparities in how nations handle public health crises. This project aims to analyze and model how a country's underlying demographics, public health infrastructure, economic health expenditure, and technological adoption (ICT) impact its overall life expectancy and its empirical resilience to health emergencies (measured via COVID-19 transmission/mortality rates and vaccination rollouts).

### Why is this important?
Understanding these relationships allows global health organizations and policymakers to identify critical vulnerabilities before the next pandemic hits. By leveraging machine learning, we can uncover which features (e.g., physicians per 1,000, digital adoption, age distribution) are the strongest predictors of robust public health outcomes and resilient crisis response.

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
3. **Feature Engineering**: TBD.
4. **Predictive Modeling**: TBD.


---

## 4. Workflow Overview
* `notebooks/01_eda_and_cleaning.ipynb`: Initial data ingestion, parsing, missing value imputation, and correlation heatmaps.
* `notebooks/02_feature_engineering.ipynb`: Feature aggregation, spatial merging, and scaling.
* `notebooks/03_modeling_and_evaluation.ipynb`: Model training, hyperparameter optimization, and statistical validation.

---

## 5. Models Tested & Results (Current Progress)
* **Baseline Linear Regression**: Used for predicting life expectancy. Achieved an $R^2$ score of `0.XX` with features like `physicians_per_1000` showing high predictive weight.
* **Random Forest Regressor**: Outperformed the linear baseline, reducing Mean Absolute Error (MAE) by `XX%`.
* **K-Means Clustering**: Applied to group countries into distinct resilience profiles based on GHS index and actual COVID-19 outcome rates.
* *Note: Complete performance charts, feature importance scores, and metric tables are continuously updated in the final modeling notebook.*

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
