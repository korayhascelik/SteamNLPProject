# SteamNLP

## Overview

SteamNLP is a Natural Language Processing and Machine Learning project developed to analyze Steam game reviews and classify user sentiment and recommendations. The project combines traditional text processing techniques with modern embedding methods to improve predictive performance.

The system includes data preprocessing pipelines, feature engineering, machine learning model training, evaluation workflows, and a Streamlit-based web application for interactive use.

---

## Project Objectives

* Process and clean large-scale Steam review datasets.
* Extract meaningful textual and numerical features from user reviews.
* Train and evaluate machine learning models for sentiment and recommendation prediction.
* Integrate transformer-based embeddings to enrich feature representations.
* Provide an interactive interface for model inference and analysis.

---

## Features

* Data preprocessing and cleaning pipeline
* TF-IDF text vectorization
* Numerical and categorical feature engineering
* BERT Sentence Transformer embeddings
* Feature fusion using combined feature matrices
* Machine learning model training and evaluation
* Best-model selection and serialization
* Streamlit web application for prediction and exploration

---

## Project Structure

```text
SteamNLP/
│
├── app.py
├── SteamNLP.ipynb
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── champion_model.joblib
│   └── features_champion.joblib
│
├── pages/
│
├── utils/
│   ├── feature_engineering.py
│   └── loader.py
│
└── reports/
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Sentence Transformers
* Streamlit
* Joblib

---

## Methodology

### Data Preprocessing

The raw Steam review dataset undergoes several preprocessing stages:

* Missing value handling
* Text normalization
* Feature extraction
* Dataset transformation
* Processed dataset generation

Processed outputs are stored in the `data/processed` directory.

### Feature Engineering

The project combines multiple feature sources:

#### TF-IDF Features

Term Frequency–Inverse Document Frequency is used to transform review texts into numerical vectors suitable for machine learning models.

#### Numerical Features

Additional metadata and numerical information extracted from reviews are incorporated into the training process.

#### Transformer Embeddings

Sentence Transformer models based on BERT are used to generate dense semantic embeddings. Dimensionality reduction and scaling techniques are applied before integration with the final feature set.

### Model Training

Multiple machine learning algorithms are evaluated and compared. The best-performing model is selected and stored as:

```text
models/champion_model.joblib
```

Associated preprocessing artifacts and metadata are also saved for inference.

---

## Running the Application

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Streamlit

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

The application will be accessible through the local Streamlit server.

---

## Current Limitations

* Training pipeline is not fully automated.
* Hyperparameter optimization is limited.
* Explainable AI integrations are incomplete.
* Cloud deployment configuration is not available.
* Docker support has not yet been implemented.
* Comprehensive cross-validation experiments remain limited.

---

## Future Improvements

* Automated training and evaluation pipeline
* Hyperparameter optimization using Optuna
* SHAP and LIME explainability modules
* Docker containerization
* Cloud deployment support
* Advanced ensemble methods
* Expanded transformer-based experimentation
* Performance monitoring and model versioning

---

## Repository Contents

| File / Directory | Description                                  |
| ---------------- | -------------------------------------------- |
| SteamNLP.ipynb   | Main analysis and experimentation notebook   |
| app.py           | Streamlit application entry point            |
| pages/           | Streamlit page modules                       |
| data/processed/  | Processed datasets and artifacts             |
| models/          | Trained models and metadata                  |
| utils/           | Helper functions and preprocessing utilities |

---

## License

This project was developed for educational and research purposes. License terms may be modified according to future project requirements.
