"""
IsTheWorldReadyForTheNextPandemic - Mini Project
Logistic Regression vs. Random Forest Model Comparison
"""

import os
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import RepeatedStratifiedKFold, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# Suppress non-critical user warnings
warnings.filterwarnings('ignore', category=UserWarning)

# Fixed seed for global reproducibility
np.random.seed(42)

# =====================================================================
# PATH CONFIGURATION (Configured for data/processed/)
# =====================================================================
def get_data_directory():
    """
    Determines dataset path dynamically.
    Checks for local 'data/processed' directory first, with fallback to Google Drive if in Colab.
    """
    # Updated relative path pointing to data/processed
    local_data_dir = Path(__file__).resolve().parent / "data" / "processed"
    
    if local_data_dir.exists():
        return local_data_dir
    
    # Fallback for Google Colab environment
    if 'google.colab' in sys.modules:
        try:
            from google.colab import drive
            drive.mount('/content/drive', force_remount=False)
            colab_dir = Path('/content/drive/MyDrive/DS_IsTheWorldReadyForTheNextPandemic/DATASET TO USE/')
            if colab_dir.exists():
                return colab_dir
        except Exception as e:
            print(f"⚠️ Colab Drive Mount failed: {e}")

    # Fallback to current working directory
    return Path(".")

DATA_DIR = get_data_directory()
FILE_NAME = "master_model_feature_matrix.csv"
DATA_PATH = DATA_DIR / FILE_NAME

print(f"📁 Loading dataset from: {DATA_PATH.resolve()}")

if not DATA_PATH.exists():
    raise FileNotFoundError(
        f"Could not locate '{FILE_NAME}'. Please place it in the folder: {DATA_DIR.resolve()}"
    )

# Load feature matrix
df_model = pd.read_csv(DATA_PATH)

# =====================================================================
# DATA PREPARATION
# =====================================================================
X = df_model.drop(columns=['location_key', 'Y_is_ready'], errors='ignore')
y = df_model['Y_is_ready']

print(f"   - Total countries in model: {X.shape[0]}")
print(f"   - Total predictor variables: {X.shape[1]}")
print(f"   - Features included: {X.columns.tolist()}\n")

# Standard CV Strategy across models (5 Folds x 10 Repeats = 50 runs)
cv_strategy = RepeatedStratifiedKFold(n_splits=5, n_repeats=10, random_state=42)
scoring_metrics = ['accuracy', 'f1', 'precision', 'recall']

# =====================================================================
# PART 1: LOGISTIC REGRESSION (BASELINE)
# =====================================================================
pipeline_lr = Pipeline([
    ('imputer', SimpleImputer(strategy='median', keep_empty_features=True)),
    ('classifier', LogisticRegression(max_iter=1000, random_state=42))
])

print("1. Running Logistic Regression (50 CV rounds)...")
cv_results_lr = cross_validate(pipeline_lr, X, y, cv=cv_strategy, scoring=scoring_metrics)

print("=========================================================")
print("📊 Baseline Model Results: Logistic Regression 📊")
print("=========================================================")
print(f"📈 Accuracy:  {cv_results_lr['test_accuracy'].mean():.2%} (±{cv_results_lr['test_accuracy'].std():.2%})")
print(f"🎯 F1-Score:  {cv_results_lr['test_f1'].mean():.2%} (±{cv_results_lr['test_f1'].std():.2%})")
print(f"🔍 Recall:    {cv_results_lr['test_recall'].mean():.2%} (±{cv_results_lr['test_recall'].std():.2%})")
print(f"📍 Precision: {cv_results_lr['test_precision'].mean():.2%} (±{cv_results_lr['test_precision'].std():.2%})")
print("=========================================================\n")

# Feature Importance - Logistic Regression
pipeline_lr.fit(X, y)
features_lr = pipeline_lr.named_steps['imputer'].get_feature_names_out(X.columns)
importance_df_lr = pd.DataFrame({
    'Feature': features_lr,
    'Coefficient': pipeline_lr.named_steps['classifier'].coef_[0]
}).sort_values(by='Coefficient', ascending=False)

print("🔍 Logistic Regression Coefficients:")
print(importance_df_lr.to_string(index=False))
print("\n")

# =====================================================================
# PART 2: RANDOM FOREST CLASSIFIER
# =====================================================================
pipeline_rf = Pipeline([
    ('imputer', SimpleImputer(strategy='median', keep_empty_features=True)),
    ('classifier', RandomForestClassifier(
        n_estimators=100,
        max_depth=4,
        min_samples_split=5,
        random_state=42
    ))
])

print("2. Running Random Forest Classifier (50 CV rounds)...")
cv_results_rf = cross_validate(pipeline_rf, X, y, cv=cv_strategy, scoring=scoring_metrics)

print("=========================================================")
print("🌲 Advanced Model Results: Random Forest Classifier 🌲")
print("=========================================================")
print(f"📈 Accuracy:  {cv_results_rf['test_accuracy'].mean():.2%} (±{cv_results_rf['test_accuracy'].std():.2%})")
print(f"🎯 F1-Score:  {cv_results_rf['test_f1'].mean():.2%} (±{cv_results_rf['test_f1'].std():.2%})")
print(f"🔍 Recall:    {cv_results_rf['test_recall'].mean():.2%} (±{cv_results_rf['test_recall'].std():.2%})")
print(f"📍 Precision: {cv_results_rf['test_precision'].mean():.2%} (±{cv_results_rf['test_precision'].std():.2%})")
print("=========================================================\n")

# =====================================================================
# PART 3: MODEL COMPARISON & REPORTING
# =====================================================================
results_data = {
    'Metric': [
        '📈 Accuracy',
        '🎯 F1-Score',
        '🔍 Recall',
        '📍 Precision'
    ],
    'Logistic Regression (Baseline)': [
        f"{cv_results_lr['test_accuracy'].mean():.2%} (±{cv_results_lr['test_accuracy'].std():.2%})",
        f"{cv_results_lr['test_f1'].mean():.2%} (±{cv_results_lr['test_f1'].std():.2%})",
        f"{cv_results_lr['test_recall'].mean():.2%} (±{cv_results_lr['test_recall'].std():.2%})",
        f"{cv_results_lr['test_precision'].mean():.2%} (±{cv_results_lr['test_precision'].std():.2%})"
    ],
    'Random Forest': [
        f"{cv_results_rf['test_accuracy'].mean():.2%} (±{cv_results_rf['test_accuracy'].std():.2%})",
        f"{cv_results_rf['test_f1'].mean():.2%} (±{cv_results_rf['test_f1'].std():.2%})",
        f"{cv_results_rf['test_recall'].mean():.2%} (±{cv_results_rf['test_recall'].std():.2%})",
        f"{cv_results_rf['test_precision'].mean():.2%} (±{cv_results_rf['test_precision'].std():.2%})"
    ]
}

df_comparison = pd.DataFrame(results_data)
print("====================================================================================")
print("📊 Official Model Comparison (Mean ± Std) 📊")
print("====================================================================================")
print(df_comparison.to_string(index=False))
print("====================================================================================\n")

# Export CSV summary locally
output_csv_path = DATA_DIR / 'models_comparison_results.csv'
df_comparison.to_csv(output_csv_path, index=False)
print(f"📁 Saved comparison table to: {output_csv_path.resolve()}\n")

# =====================================================================
# PART 4: FEATURE IMPORTANCE ANALYSIS (X1 - X7)
# =====================================================================
desired_features = [
    'X1_hospital_beds',
    'X2_physicians',
    'X3_ghs_early_detection',
    'X4_testing_rate',
    'X5_ghs_index',
    'X6_internet_users',
    'X7_age_60_plus'
]

X_raw = pd.DataFrame(index=df_model.index)
for col in desired_features:
    if col in df_model.columns:
        X_raw[col] = df_model[col]
    else:
        print(f"⚠️ Feature '{col}' missing from source data! Initializing defaults...")
        X_raw[col] = 0.0

# Impute medians safely
for col in desired_features:
    if X_raw[col].isnull().sum() < len(X_raw):
        median_value = X_raw[col].median()
        X_raw[col] = X_raw[col].fillna(median_value)
    X_raw[col] = X_raw[col].fillna(0.0)

rf_model = RandomForestClassifier(n_estimators=100, max_depth=4, min_samples_split=5, random_state=42)
rf_model.fit(X_raw, y)

df_importance = pd.DataFrame({
    'Feature': desired_features,
    'Importance': rf_model.feature_importances_
}).sort_values(by='Importance', ascending=False)

# Render & Save Feature Importance Plot
plt.figure(figsize=(10, 6))
sns.barplot(
    x='Importance',
    y='Feature',
    data=df_importance,
    palette='viridis',
    hue='Feature',
    legend=False
)

plt.title('Feature Importance - Random Forest Classifier\nReadiness for World Pandemic', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Relative Importance Weight', fontsize=12, labelpad=10)
plt.ylabel('Model Features (X1 - X7)', fontsize=12)

for index, value in enumerate(df_importance['Importance']):
    plt.text(value + 0.005, index, f'{value:.1%}', va='center', ha='left', fontsize=10, fontweight='bold')

plt.xlim(0, df_importance['Importance'].max() + 0.05)
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()

plot_output = DATA_DIR / 'feature_importance.png'
plt.savefig(plot_output, dpi=300)
print(f"📊 Saved feature importance plot to: {plot_output.resolve()}")
plt.show()

print("\n📋 Final Feature Importance Table:")
print("====================================")
for idx, row in df_importance.iterrows():
    print(f"{row['Feature']}: {row['Importance']:.2%}")
print("====================================")