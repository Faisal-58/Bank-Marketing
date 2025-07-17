# 🏦 Bank Marketing Subscription Prediction (ML + Power BI)

This project focuses on predicting whether a client will subscribe to a term deposit based on their demographic and behavioral data. The solution combines **Exploratory Data Analysis (EDA)** in Power BI and a **Machine Learning classification model** in Python. Further the best model pipeline is selected and wrapped in an API using FASTAPI. It is further connected with a streamlit frontend. Let us have a walkthrough for a complete project.

---

## 🔍 Problem Statement

Marketing campaigns are costly and time-sensitive. Using client data from a Portuguese bank, the goal is to build a machine learning model to:
- Identify customers who are likely to subscribe to a term deposit.
- Help the bank make informed targeting decisions for future campaigns.

---

## 📁 Dataset

- **Source**: UCI Bank Marketing Dataset  
- **Records**: 41,188  
- **Target Variable**: `y` → (Subscribed: Yes/No)

Key features:
- Age, Job, Marital Status, Education  
- Balance, Housing loan, Previous contact outcomes  
- Duration of last contact, Campaign details, etc.

---

## 🧠 Machine Learning Approach

### ✅ Steps:
1. **Data Cleaning** (handled unknowns, encoded categories)
   Data is clenaed and preprocessed where categorical variables are encoded using OneHotEncoder() and numerical varibales are standardized using StandardScaler().
2. **Exploratory Data Analysis** (Power BI visualization)
   A basic PowerBI dashboard is used for viewing the important insights of the dataset.
   
5. **Feature Engineering**
6. **Balancing**: Used SMOTE to handle class imbalance
7. **Model Selection**:
   - Logistic Regression  
   - Random Forest  
   - XGBoost (Best performer)
8. **Evaluation**:
   - Confusion Matrix  
   - Classification Report  
   - ROC-AUC Curve

---

## 📊 Power BI Dashboard

An interactive Power BI dashboard was created to understand:
- Subscription distribution across jobs, age groups, marital status
- Balance and duration impact
- Overall success rate of marketing campaign

![Dashboard Screenshot](path/to/your/dashboard.png)

---

## ⚙️ Tools & Technologies

- **Python** (Pandas, Scikit-learn, XGBoost, Matplotlib)
- **Power BI** for EDA and storytelling
- **Jupyter Notebook / VS Code**
- **SMOTE** for class balancing

---

## 📈 Results

- **Best Model**: XGBoost  
- **Accuracy**: ~89%  
- **AUC Score**: ~0.91  
- Feature importance and visual patterns aligned well with domain intuition.

---

## 📂 Folder Structure

```bash
bank-marketing-ml/
│
├── data/                  # Raw and processed datasets
├── notebook/              # ML model training notebooks
├── reports/               # Visualizations, EDA exports
├── model/                 # Saved models (e.g. xgboost.pkl)
├── powerbi/               # Power BI dashboard file (.pbix)
└── README.md
