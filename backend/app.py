from fastapi import FastAPI
from schemas import Transaction
from model_utils import model

import pandas as pd

app = FastAPI()


def calculate_risk_score(
    transaction,
    fraud_probability
):

    score = fraud_probability * 0.5

    if transaction["amount"] > 500000:
        score += 20

    if transaction["amount_balance_ratio"] >= 0.8:
        score += 15

    if transaction["type"] in [
        "TRANSFER",
        "CASH_OUT"
    ]:
        score += 15

    return min(
        100,
        round(score)
    )


def risk_level(score):

    if score >= 80:
        return "HIGH"

    elif score >= 30:
        return "MEDIUM"

    else:
        return "LOW"


@app.get("/")
def home():

    return {
        "message":
        "Fraud Detection API Running"
    }


@app.post("/predict")
def predict(
    transaction: Transaction
):

    data = pd.DataFrame([{

        "step": 1,

        "type": transaction.type,

        "amount": transaction.amount,

        "oldbalanceOrg": transaction.oldbalanceOrg,

        "newbalanceOrig": transaction.newbalanceOrig,

        "oldbalanceDest": transaction.oldbalanceDest,

        "newbalanceDest": transaction.newbalanceDest,

        "isFlaggedFraud": 0

    }])

    # Feature Engineering

    data["balance_change_orig"] = (
        data["oldbalanceOrg"]
        -
        data["newbalanceOrig"]
    )

    data["balance_change_dest"] = (
        data["newbalanceDest"]
        -
        data["oldbalanceDest"]
    )

    data["amount_balance_ratio"] = (
        data["amount"]
        /
        (data["oldbalanceOrg"] + 1)
    )

    # Model Prediction

    probability = (
        model.predict_proba(data)[0][1]
    )

    fraud_probability = round(
        probability * 100,
        2
    )

    risk_score = calculate_risk_score(
        data.iloc[0],
        fraud_probability
    )

    reasons = []

    if data.iloc[0]["amount"] > 500000:
        reasons.append(
            "Large transaction amount"
        )

    if data.iloc[0][
        "amount_balance_ratio"
    ] >= 0.8:

        reasons.append(
            "High balance utilization"
        )

    if data.iloc[0]["type"] in [
        "TRANSFER",
        "CASH_OUT"
    ]:

        reasons.append(
            "High-risk transaction type"
        )

    return {

        "prediction":
            "Fraud"
            if probability > 0.5
            else "Legitimate",

        "fraud_probability":
            fraud_probability,

        "risk_score":
            risk_score,

        "risk_level":
            risk_level(
                risk_score
            ),

        "reasons":
            reasons
    }