# 🧠 Student Pass Prediction App

A simple machine learning web app built with *Streamlit* that predicts whether a student will pass based on study hours, attendance, assignment completion, and study group participation.

## 📁 Files in this Repository

| File | Description |
|------|-------------|
| student_pass_prediction.ipynb | The Jupyter Notebook where the model was trained and exported using joblib |
| student_model.pkl | The trained logistic regression model saved as a pickle file |
| app.py | The Streamlit web app script that loads the model and runs predictions |


## 📸 Screenshot

![App Screenshot](https://github.com/Jane-Emmanuel/student-pass-prediction/blob/main/student_pass_prediction_screenshot.PNG)


## 🔗 Notebook Preview

View the notebook directly on GitHub:  
[📘 View Jupyter Notebook](https://github.com/Jane_Emmanuel_student_pass_prediction.ipynb)


## ▶ How to Run the App

1. Make sure you have Python and Streamlit installed:
   bash
   pip install streamlit joblib scikit-learn
`

2. Run the app:

   bash
   streamlit run app.py
   

## 💡 Features

* Predicts student pass/fail status in real time
* Uses logistic regression trained on custom data
* Simple user interface with input widgets

## ✅ Future Improvements

* Add more features like exam score, previous grades
* Deploy the app to Streamlit Cloud or HuggingFace

## 📬 Author

Jane Emmanuel – [@LinkedIn](https://www.linkedin.com/in/jane-emmanuel-/)
