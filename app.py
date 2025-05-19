import streamlit as st
import numpy as np
import joblib
from sklearn.linear_model import LogisticRegression

# model for demonstration

model = joblib.load("student_model.pkl")


st.title("Student Pass Prediction")

study_hours = st.number_input("Study Hours per Week", 0, 50)
attendance = st.slider("Attendance Percentage", 0, 100)
assignments = st.number_input("Assignments Submitted", 0, 10)
study_group = st.selectbox("In Study Group?", ["No", "Yes"])
study_group_value = 1 if study_group == "Yes" else 0

if st.button("Predict"):
    features = np.array([[study_hours, attendance, assignments, study_group_value]])
    prediction = model.predict(features)[0]
    if prediction == 1:
        st.success("Prediction: Pass")
    else:
        st.success("Prediction: Fail")