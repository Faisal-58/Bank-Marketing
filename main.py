import pandas as pd
from src.data_loader import load_data
from src.preprocess import build_pipeline
from src.train import train_model
from src.evaluate import evaluate_model
import joblib
import json

if __name__ == "__main__":

    df = load_data('data/bank.csv')
    X= df.drop('y', axis=1)
    y=df['y']

    best_pipeline, X_test,y_test,y_pred,y_proba,threshold,best_model_name = train_model(X,y)

    evaluate_model(y_test, y_pred, y_proba)

    # Save best pipeline
    joblib.dump(best_pipeline, "models/xgb_pipeline.pkl")

    # Save threshold and model name
    with open("config/threshold.json", "w") as f:
        json.dump({
            "threshold": threshold,
            "best_model": best_model_name
        }, f)

    print(f"\n Saved best model: {best_model_name}")



