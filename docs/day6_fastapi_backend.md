# Day 6 - FastAPI Backend & Fraud Intelligence API

## Objective

* Convert the fraud detection model into a deployable API.
* Expose predictions through HTTP endpoints.

## FastAPI Setup

Installed:

* FastAPI
* Uvicorn
* Joblib
* Pydantic

Created backend structure:

* app.py
* model_utils.py
* schemas.py

## Model Deployment

Saved trained Random Forest model:

random_forest_model.pkl

Loaded model dynamically using Joblib.

## API Endpoints

### GET /

Returns API status.

Example Response:

{
"message": "Fraud Detection API Running"
}

### POST /predict

Accepts transaction data and returns fraud analysis.

## Request Validation

Implemented Pydantic schema:

Transaction

Fields:

* type
* amount
* oldbalanceOrg
* newbalanceOrig
* oldbalanceDest
* newbalanceDest

## Feature Engineering Inside API

Generated:

* balance_change_orig
* balance_change_dest
* amount_balance_ratio

Automatically before prediction.

## Fraud Prediction

Used deployed Random Forest model.

Generated:

* Prediction
* Fraud Probability

## Risk Intelligence Integration

Added:

### Risk Score

Range: 0 - 100

### Risk Levels

LOW

MEDIUM

HIGH

### Investigation Reasons

* Large transaction amount
* High balance utilization
* High-risk transaction type

## Example API Response

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

## Key Achievement

Successfully transformed the machine learning model into a real-time Fraud Intelligence API capable of receiving transaction data, performing predictions, calculating risk scores, and generating investigation reports.

## Observation

The project now functions as a deployable backend service and can be integrated with web dashboards, mobile applications, or banking systems.
