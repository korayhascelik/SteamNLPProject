import pandas as pd
import joblib

def load_data():
    return pd.read_csv("data/processed/df_processed.csv")

def load_model():
    return joblib.load("models/champion_model.joblib")

def load_scaler():
    return joblib.load("models/scaler_champion.joblib")

def load_features():
    """Load selected features from champion model"""
    return joblib.load("models/features_champion.joblib")