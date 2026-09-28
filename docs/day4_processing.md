# Day 4 - Explainable AI (SHAP) & Fraud Investigation

## Objective

* Make fraud predictions interpretable.
* Explain why a transaction was classified as fraudulent.

## SHAP Integration

* Installed and configured SHAP.
* Created TreeExplainer for the Random Forest model.
* Generated SHAP values for model explanations.

## Global Explainability

### SHAP Summary Plot

Generated a global feature importance visualization showing how each feature influences fraud predictions.

### Most Influential Features

1. balance_change_orig
2. amount_balance_ratio
3. amount
4. oldbalanceOrg
5. type_TRANSFER

## Transaction-Level Explainability

Selected a real fraud transaction from the test dataset:

Transaction ID: 6202693

Transaction Type: CASH_OUT

Transaction Amount: 759,701

## SHAP Waterfall Plot

Generated a transaction-level explanation showing the contribution of each feature toward the fraud prediction.

### Top Positive Contributors

1. balance_change_orig (+0.17)
2. amount_balance_ratio (+0.13)
3. newbalanceOrig (+0.06)
4. oldbalanceOrg (+0.05)
5. amount (+0.04)

### Negative Contributor

* oldbalanceDest (-0.03)

## Fraud Investigation Report

### Findings

* Sender account balance dropped to zero.
* Transaction consumed nearly 100% of available balance.
* Large transaction amount.
* CASH_OUT transaction type.
* Model predicted fraud with near-certain confidence.

## Screenshots Saved

* shap_summary_plot.png
* shap_waterfall_plot.png

## Key Achievements

* Implemented Explainable AI using SHAP.
* Added global model interpretability.
* Added transaction-level fraud explanations.
* Created fraud investigation reporting capability.

## Observation

The fraud detection system can now explain its decisions, making the model transparent, trustworthy, and suitable for real-world fraud investigation workflows.
