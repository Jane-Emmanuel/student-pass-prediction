# 🎓 Student Pass Prediction App

This project is a simple machine learning app that predicts whether a student will pass or fail based on study hours, attendance, assignment submission, and study group participation.

##  Project Files

1. *student_pass_prediction.ipynb*
   - Jupyter Notebook containing the full process:
     - Data preparation
     - Model training (Logistic Regression)
     - Model saving using joblib

2. *student_model.pkl*
   - Serialized (saved) model file created from the trained model in the notebook.
   - This file is used by the Streamlit app to make predictions.

3. *app.py*
   - A simple Streamlit app that:
     - Loads the saved model
     - Accepts user input (study hours, attendance, etc.)
     - Predicts and displays whether the student will *Pass* or *Fail*

## How to Run the App

1. Make sure you have Python and Streamlit installed.
2. Open your terminal or command prompt.
3. Navigate to the folder containing app.py and student_model.pkl.
4. Run the following command:

bash
streamlit run app.py


## Requirements

Install the required packages if you don't have them yet:

bash
pip install streamlit scikit-learn pandas joblib

