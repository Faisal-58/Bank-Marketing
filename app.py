import streamlit as st
import requests

st.set_page_config(page_title="Bank Subscription Predictor", page_icon="🏦")

st.title("🏦 Bank Term Deposit Subscription Predictor")
st.markdown("Check if a client is likely to subscribe to a term deposit based on their information.")


with st.form("client_form"):
    age = st.number_input("Age", 18, 100, 30)
    job = st.selectbox("Job", ["admin.", "technician", "services", "management", "retired", "blue-collar", "unemployed", "entrepreneur", "housemaid", "student", "self-employed", "unknown"])
    marital = st.selectbox("Marital Status", ["married", "single", "divorced"])
    education = st.selectbox("Education", ["primary", "secondary", "tertiary", "unknown"])
    default = st.selectbox("Has Credit in Default?", ["no", "yes"])
    housing = st.selectbox("Has Housing Loan?", ["no", "yes"])
    loan = st.selectbox("Has Personal Loan?", ["no", "yes"])
    contact = st.selectbox("Contact Type", ["cellular", "telephone", "unknown"])
    month = st.selectbox("Last Contact Month", ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])
    day_of_week = st.selectbox("Day of Week", ["mon", "tue", "wed", "thu", "fri"])
    duration = st.slider("Last Contact Duration (sec)", 0, 4000, 200)
    campaign = st.number_input("Campaign Contacts", 1, 50, 2)
    pdays = st.number_input("Days Since Last Contact", -1, 999, 999)
    previous = st.number_input("Previous Contacts", 0, 50, 0)
    poutcome = st.selectbox("Previous Campaign Outcome", ["nonexistent", "failure", "success"])
    emp_var_rate = st.number_input("Employment Variation Rate", -3.0, 2.0, 1.1, step=0.1)
    cons_price_idx = st.number_input("Consumer Price Index", 90.0, 100.0, 93.994)
    cons_conf_idx = st.number_input("Consumer Confidence Index", -60.0, 0.0, -36.4)
    euribor3m = st.number_input("Euribor 3 Month Rate", 0.0, 6.0, 4.857)
    nr_employed = st.number_input("Number of Employees", 4000.0, 6000.0, 5191.0)

    submit = st.form_submit_button("Predict")


if submit:
    payload = {
        "age": age,
        "job": job,
        "marital": marital,
        "education": education,
        "default": default,
        "housing": housing,
        "loan": loan,
        "contact": contact,
        "month": month,
        "day_of_week": day_of_week,
        "duration": duration,
        "campaign": campaign,
        "pdays": pdays,
        "previous": previous,
        "poutcome": poutcome,
        "emp.var.rate": emp_var_rate,
        "cons.price.idx": cons_price_idx,
        "cons.conf.idx": cons_conf_idx,
        "euribor3m": euribor3m,
        "nr.employed": nr_employed
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        result = response.json()

        st.success(" Prediction: {}".format(result["subscribed"]))
        st.metric(label=" Probability", value=result["probability"])

    except Exception as e:
        st.error(" Prediction failed. Please check the backend is running.")
        st.exception(e)
