# Day 2 - Preprocessing & Baseline Model

## Data Cleaning
- Removed nameOrig
- Removed nameDest

## Feature Engineering
- balance_change_orig
- balance_change_dest
- amount_balance_ratio

## Preprocessing
- OneHotEncoder for transaction type
- Train/Test Split with stratify

## Baseline Model
- Logistic Regression

## Results
Precision: 3%
Recall: 92%
F1 Score: 6%

## Observation
Model catches most fraud transactions but generates too many false positives.