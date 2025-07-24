import streamlit as st
import numpy as np
import joblib
from sklearn.linear_model import LogisticRegression

# Write the requirements.txt file
with open("requirements.txt", "w") as f:
    f.write("streamlit\nnumpy\nscikit-learn\njoblib")

# Load your model
model = joblib.load("student_model.pkl")

# App title
st.title("🎓 Student Pass Prediction")

# Input for student name
student_name = st.text_input("Enter Student Name")

# Input fields for prediction features
study_hours = st.number_input("Study Hours per Week", 0, 50)
attendance = st.slider("Attendance Percentage", 0, 100)
assignments = st.number_input("Assignments Submitted", 0, 10)
study_group = st.selectbox("In Study Group?", ["No", "Yes"])
study_group_value = 1 if study_group == "Yes" else 0

# Predict button
if st.button("Predict"):
    features = np.array([[study_hours, attendance, assignments, study_group_value]])
    prediction = model.predict(features)[0]
    
    name_display = student_name.strip() if student_name.strip() else "The student"
    
    if prediction == 1:
        st.success(f"{name_display} is likely to **Pass** ✅")
    else:
        st.error(f"{name_display} is likely to **Fail** ❌")
