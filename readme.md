# Explainable AI-Based Fraud Detection & Risk Intelligence Platform

An end-to-end Explainable AI-powered fraud detection platform that identifies fraudulent financial transactions, explains model predictions using SHAP, assigns transaction risk scores, and provides real-time fraud analysis through a FastAPI backend and Streamlit dashboard.

---

## Features

- Fraud Detection using Random Forest
- Explainable AI using SHAP
- Risk Intelligence Engine
- Fraud Probability Prediction
- Risk Score (0–100)
- Risk Level Classification
- Human-readable Investigation Reasons
- FastAPI REST API
- Interactive Streamlit Dashboard
- Real-Time Fraud Analysis

---

## Dataset

**PaySim Financial Transactions Dataset**

- Total Transactions: **6,362,620**
- Fraud Cases: **8,213**
- Fraud Rate: **0.13%**

---

## Tech Stack

### Machine Learning

- Python
- Scikit-learn
- Random Forest
- SHAP
- Pandas
- NumPy

### Backend

- FastAPI
- Pydantic
- Joblib
- Uvicorn

### Frontend

- Streamlit

---

## Project Architecture

```
Transaction Input
        ↓
Feature Engineering
        ↓
Random Forest Model
        ↓
SHAP Explainability
        ↓
Risk Scoring Engine
        ↓
FastAPI Backend
        ↓
Streamlit Dashboard
        ↓
Fraud Intelligence Report
```

---

## Research Gaps Addressed

- Explainability in fraud detection
- Risk prioritization
- Fraud investigation support
- End-to-end deployable AI system
- Hybrid AI + Risk Intelligence framework

---

## Example Output

```json
{
  "prediction": "Fraud",
  "fraud_probability": 84,
  "risk_score": 92,
  "risk_level": "HIGH",
  "reasons": [
    "Large transaction amount",
    "High balance utilization",
    "High-risk transaction type"
  ]
}
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-CREDIT-CARD-FRAUD-DETECTION-SYSTEM.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run FastAPI Backend

```bash
cd backend
uvicorn app:app --reload
```

Backend:

```
http://127.0.0.1:8000
```

API Documentation:

```
http://127.0.0.1:8000/docs
```

---

## Run Streamlit Dashboard

```bash
cd frontend
streamlit run dashboard.py
```

Dashboard:

```
http://localhost:8501
```

---

## Project Workflow

1. User enters transaction details.
2. Feature engineering generates fraud-specific features.
3. Random Forest predicts fraud probability.
4. SHAP explains the prediction.
5. Risk Intelligence Engine calculates risk score.
6. FastAPI returns prediction.
7. Streamlit visualizes results.

---

## Future Improvements

- XGBoost & LightGBM comparison
- Deep Learning models
- Graph Neural Networks
- Kafka streaming
- Cloud Deployment (AWS/Azure/GCP)
- Real Banking Dataset Integration
