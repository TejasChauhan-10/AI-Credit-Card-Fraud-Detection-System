# Day 5 - Risk Scoring Engine & Fraud Intelligence

## Objective

* Convert fraud predictions into actionable business intelligence.
* Assign risk scores and risk levels to suspicious transactions.

## Fraud Probability

Used Random Forest prediction probabilities:

* predict_proba()

Example:

Fraud Probability = 100%

## Risk Scoring Engine

Developed a custom risk scoring system combining:

1. Machine Learning Probability
2. Transaction Amount
3. Balance Utilization Ratio
4. Transaction Type Risk

### Scoring Rules

* ML Fraud Probability → 0–50 Points
* Large Transaction Amount (>500,000) → +20 Points
* High Balance Utilization (>80%) → +15 Points
* High-Risk Transaction Type (TRANSFER/CASH_OUT) → +15 Points

Maximum Risk Score = 100

## Risk Levels

### LOW

Risk Score < 50

### MEDIUM

Risk Score 50–79

### HIGH

Risk Score ≥ 80

## Fraud Investigation Report

Generated structured fraud reports containing:

* Fraud Probability
* Risk Score
* Risk Level
* Risk Reasons

### Example Output

Fraud Probability: 100%

Risk Score: 100

Risk Level: HIGH

Reasons:

* Large transaction amount
* High balance utilization
* High-risk transaction type

## Key Achievement

Successfully transformed the fraud detection model into a Fraud Intelligence Engine capable of producing interpretable risk assessments instead of simple fraud predictions.

## Observation

The system now combines AI predictions with business rules, making the platform more practical and aligned with real-world fraud monitoring systems used in banking and fintech environments.
