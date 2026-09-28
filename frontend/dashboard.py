import streamlit as st
import requests

st.set_page_config(
    page_title="Fraud Detection Dashboard",
    layout="wide"
)

st.title(
    "💳 AI Fraud Detection & Risk Intelligence Platform"
)

st.markdown(
    "Enter transaction details and analyze fraud risk."
)

# Input Fields

transaction_type = st.selectbox(
    "Transaction Type",
    [
        "CASH_OUT",
        "TRANSFER",
        "PAYMENT",
        "CASH_IN",
        "DEBIT"
    ]
)

amount = st.number_input(
    "Amount",
    min_value=0.0,
    value=1000.0
)

oldbalanceOrg = st.number_input(
    "Old Balance Origin",
    min_value=0.0,
    value=10000.0
)

newbalanceOrig = st.number_input(
    "New Balance Origin",
    min_value=0.0,
    value=5000.0
)

oldbalanceDest = st.number_input(
    "Old Balance Destination",
    min_value=0.0,
    value=0.0
)

newbalanceDest = st.number_input(
    "New Balance Destination",
    min_value=0.0,
    value=5000.0
)

if st.button("Analyze Transaction"):

    payload = {

        "type": transaction_type,

        "amount": amount,

        "oldbalanceOrg": oldbalanceOrg,

        "newbalanceOrig": newbalanceOrig,

        "oldbalanceDest": oldbalanceDest,

        "newbalanceDest": newbalanceDest
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        result = response.json()

        st.success("Analysis Complete")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Prediction",
                result["prediction"]
            )

        with col2:
            st.metric(
                "Fraud Probability",
                f"{result['fraud_probability']}%"
            )

        with col3:
            st.metric(
                "Risk Score",
                result["risk_score"]
            )

        st.subheader("Risk Level")

        st.warning(
            result["risk_level"]
        )

        st.subheader(
            "Investigation Reasons"
        )

        for reason in result["reasons"]:
            st.write(
                f"• {reason}"
            )

    except Exception as e:

        st.error(
            f"API Error: {e}"
        )