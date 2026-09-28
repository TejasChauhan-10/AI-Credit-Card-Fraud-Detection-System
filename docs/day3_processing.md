# Day 3 - Random Forest Model & Feature Importance Analysis

## Objective

* Improve fraud detection performance beyond Logistic Regression.
* Reduce false positives while maintaining high fraud detection accuracy.

## Data Preparation

* Loaded PaySim dataset.
* Removed:

  * nameOrig
  * nameDest
* Recreated engineered features:

  * balance_change_orig
  * balance_change_dest
  * amount_balance_ratio

## Train-Test Split

* 80% Training Data
* 20% Testing Data
* Used stratified sampling to preserve fraud distribution.

## Model Training

* Trained Random Forest Classifier.
* Parameters:

  * n_estimators = 100
  * class_weight = balanced
  * random_state = 42
  * n_jobs = -1

## Sampling Strategy

* Used a training sample of 500,000 transactions to reduce training time and memory usage.

## Model Evaluation

### Classification Report

Precision: 100%

Recall: 99%

F1 Score: 99%

### Confusion Matrix

True Negatives: 1,270,879

False Positives: 2

False Negatives: 16

True Positives: 1,627

## Feature Importance Analysis

### Top Features

1. balance_change_orig
2. amount_balance_ratio
3. newbalanceOrig
4. oldbalanceOrg
5. amount
6. type_TRANSFER

## Key Findings

* Random Forest significantly outperformed Logistic Regression.
* Engineered features became the strongest predictors of fraud.
* Fraud detection accuracy improved dramatically.
* False positive alerts were almost eliminated.

## Observation

Random Forest successfully captured complex fraud patterns and became the primary fraud detection model for the project.
