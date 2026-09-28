# AI-Powered Explainable Fraud Detection & Risk Intelligence Platform

## Project Summary

The AI-Powered Explainable Fraud Detection & Risk Intelligence Platform is an end-to-end machine learning system designed to detect fraudulent financial transactions, explain the reasons behind fraud predictions, assess transaction risk, and provide real-time fraud analysis through a web-based dashboard.

The project was developed using the PaySim financial transaction dataset containing over 6.3 million transactions. The system performs data preprocessing, feature engineering, fraud classification, explainable AI analysis, risk scoring, backend API deployment, and dashboard visualization.

The workflow begins with transaction data processing and feature engineering, where important behavioral features such as balance changes and balance utilization ratios are generated. A Random Forest model is then trained to classify transactions as fraudulent or legitimate. To improve transparency, SHAP (SHapley Additive Explanations) is integrated to explain both global model behavior and individual transaction predictions.

A custom Risk Scoring Engine is developed to convert machine learning predictions into business-friendly risk assessments. Instead of only predicting fraud, the platform assigns a risk score (0–100), risk level (Low, Medium, High), and investigation reasons to support fraud analysts and decision-makers.

The trained model is deployed through a FastAPI backend, allowing real-time fraud analysis via REST APIs. Finally, a Streamlit dashboard provides an interactive interface where users can enter transaction details and instantly receive fraud predictions, risk scores, and investigation insights.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Random Forest
* SHAP (Explainable AI)
* FastAPI
* Streamlit
* Joblib
* Pydantic

## Key Features

* Fraud Detection using Machine Learning
* Feature Engineering for Fraud Pattern Discovery
* Explainable AI using SHAP
* Fraud Probability Prediction
* Risk Scoring Engine
* Risk Level Classification
* Investigation Reason Generation
* REST API Deployment using FastAPI
* Interactive Dashboard using Streamlit
* Real-Time Fraud Analysis

## System Architecture

Transaction Input
↓
Feature Engineering
↓
Random Forest Model
↓
Fraud Probability Prediction
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

### Component description 

1. Streamlit Dashboard
    User Interface
    Transaction Input
    Results Visualization

2. FastAPI Backend
    Receives transaction requests
    Performs prediction
    Returns fraud intelligence report

3. Feature Engineering Layer
Generates:

    balance_change_orig
    balance_change_dest
    amount_balance_ratio

4. Random Forest Model
    Fraud classification
    Fraud probability estimation

5. SHAP Explainability
    Global explanations
    Transaction-level explanations

6. Risk Scoring Engine
    Risk Score (0–100)
    Risk Level
    Investigation Reasons

### Working steps 

1. Transaction Input
User enters:
    Transaction Type
    Amount
    Account Balances
through Streamlit dashboard

2. API Request : Dashboard sends transaction data to FastAPI.

3. Feature Engineering
The system automatically generates:
    balance_change_orig
    balance_change_dest
    amount_balance_ratio

4. Fraud Prediction
Random Forest model predicts:
    Fraud
    or
    Legitimate
and calculates fraud probability.

5. Explainability Analysis
SHAP identifies:
    Important features
    Reasons behind prediction

6. Risk Scoring
Business rules calculate: Risk Score (0–100) based on:
    Fraud Probability
    Transaction Amount
    Balance Utilization
    Transaction Type

7. Risk Classification
Transaction is categorized as:
    LOW
    MEDIUM
    HIGH
risk.

8. Fraud Intelligence Report
System generates:
    Prediction
    Fraud Probability
    Risk Score
    Risk Level
    Investigation Reasons

9. Dashboard Display : Results are displayed in real time.


## Results

The Random Forest model achieved near-perfect fraud detection performance with extremely high precision and recall while significantly reducing false positives compared to the baseline Logistic Regression model.

The platform successfully generates:

* Fraud Prediction
* Fraud Probability
* Risk Score
* Risk Level
* Investigation Reasons
* Explainable AI Insights

making it suitable for real-world fraud monitoring and investigation scenarios.

# Novelty

Most existing fraud detection systems focus only on binary classification (Fraud / Not Fraud) and provide little or no explanation for their decisions. Many research works also stop at model accuracy evaluation without addressing transparency, analyst support, risk prioritization, or deployment aspects.

This project addresses several important research and practical gaps:

### Research Gap 1: Lack of Explainability

Traditional fraud detection models behave like black boxes and do not explain why a transaction is flagged as fraudulent.

**Solution:** Integrated SHAP Explainable AI to provide both global feature importance analysis and transaction-level explanations through waterfall plots.

### Research Gap 2: Absence of Risk Prioritization

Most studies only output fraud predictions without helping organizations prioritize investigations.

**Solution:** Developed a Risk Scoring Engine that converts machine learning outputs into risk scores and risk levels (Low, Medium, High).

### Research Gap 3: Limited Analyst Support

Many fraud detection systems identify fraud but do not provide actionable reasons for investigators.

**Solution:** Generated investigation reasons such as large transaction amount, high balance utilization, and high-risk transaction type to assist fraud analysts.

### Research Gap 4: Lack of End-to-End Deployment

A large number of academic projects remain limited to Jupyter notebooks and are not deployable.

**Solution:** Built a production-style architecture using FastAPI and Streamlit for real-time fraud analysis.

### Research Gap 5: Weak Integration Between AI and Business Rules

Most systems rely only on machine learning predictions.

**Solution:** Combined machine learning predictions with business-driven risk scoring rules, creating a hybrid AI + Risk Intelligence framework.

## Unique Contributions

1. Explainable Fraud Detection using SHAP.
2. Hybrid AI + Risk Intelligence Architecture.
3. Real-Time Fraud Analysis API using FastAPI.
4. Interactive Fraud Investigation Dashboard using Streamlit.
5. Automated Risk Score and Risk Level Generation.
6. Human-readable Fraud Investigation Reports.
7. Complete End-to-End Deployable System rather than a standalone ML model.

The final outcome is not merely a fraud classifier but a comprehensive Explainable Fraud Detection & Risk Intelligence Platform capable of supporting real-time decision-making, fraud investigation, and risk management workflows.

## Limitations : 
Limitation 1: Dataset Dependency
The model is trained on the PaySim dataset.
Therefore: Performance may vary on real banking datasets.
Additional retraining may be required.

Limitation 2: Rule-Based Risk Engine
Current risk scoring uses manually defined rules.
Example: Amount > 500000
Future work could use adaptive risk scoring.

Limitation 3: Limited User Features . The model only considers transaction information.
It does not use:
Customer history
Device information
IP address
Geolocation

Limitation 4: No Continuous Learning
The model does not automatically retrain on new fraud patterns.
Future versions can incorporate online learning.

Limitation 5: Local Deployment
Current implementation runs locally using:
FastAPI
Streamlit

Cloud deployment is not yet implemented.
