from sklearn.model_selection import train_test_split
from imblearn.pipeline import Pipeline as ImbPipeline
from src.preprocess import build_pipeline
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import SMOTE
from sklearn.metrics import roc_auc_score
import pandas as pd


def train_model(X, y, threshold=0.4):
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    # Get column types from training set
    numeric_cols = X_train.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = X_train.select_dtypes(include=['object']).columns.tolist()

    # Build preprocessor
    preprocessor = build_pipeline(numeric_cols, categorical_cols)

    # Define models
    models = {
        "Random Forest": RandomForestClassifier(random_state=42),
        "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
        "XGBoost": XGBClassifier(random_state=42, verbosity=0)
    }

    # Initialize tracking
    best_score = 0
    best_model_name = None
    best_pipeline = None
    best_y_pred = None
    best_y_proba = None

    # Loop through models
    for name, model in models.items():
        print(f"\n Training model: {name}")

        pipeline = ImbPipeline(steps=[
            ('preprocessor', preprocessor),
            ('smote', SMOTE(random_state=42)),
            ('model', model)
        ])

        # Fit on training
        pipeline.fit(X_train, y_train)

        # Predict
        y_proba = pipeline.predict_proba(X_test)[:, 1]
        y_pred = (y_proba >= threshold).astype(int)

        score = roc_auc_score(y_test, y_proba)
        print(f" {name} ROC-AUC: {score:.4f}")

        if score > best_score:
            best_score = score
            best_model_name = name
            best_pipeline = pipeline
            best_y_pred = y_pred
            best_y_proba = y_proba

    print(f"\n Best model: {best_model_name} with ROC-AUC: {best_score:.4f}")

    return best_pipeline, X_test, y_test, best_y_pred, best_y_proba, threshold,best_model_name
