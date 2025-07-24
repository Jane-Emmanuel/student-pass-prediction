
#  Student Pass Prediction App

A simple machine learning web app built with **Streamlit** that predicts whether a student will pass based on their study hours, attendance, assignment completion, and study group participation.

---

##  Files in this Repository

| File                             | Description                                                       |
|----------------------------------|-------------------------------------------------------------------|
| `student_pass_prediction.ipynb` | Jupyter Notebook for training and exporting the model using joblib |
| `student_model.pkl`             | Trained Logistic Regression model saved as a pickle file          |
| `app.py`                        | Streamlit app script for running the web app and predictions      |
| `requirements.txt`              | Python dependencies required to run the app                      |

---

##  Screenshot

![App Screenshot](https://github.com/Jane-Emmanuel/student-pass-prediction/blob/main/student_pass_prediction_screenshot.PNG)

---

##  Notebook Preview

View the notebook directly on GitHub:  
[📘 Jane_Emmanuel_student_pass_prediction.ipynb](https://github.com/Jane-Emmanuel/student-pass-prediction/blob/main/Jane_Emmanuel_student_pass_prediction.ipynb)

---

##  View the Live App

Try it out on Streamlit Cloud:  
 [**Launch the App**](https://student-pass-prediction-c7qmxbng5ee6zk8jtftwmv.streamlit.app/)

---

##  Run Locally (Optional)

1. **Install dependencies**  
```bash
pip install streamlit joblib scikit-learn numpy
````

2. **Run the app**

```bash
streamlit run app.py
```

---

##  Features

* Predicts student pass/fail status using logistic regression
* Real-time prediction with interactive UI
* Lightweight and easy to deploy on Streamlit Cloud

---

##  Future Improvements

* Include more features like exam scores, previous grades, or study duration trend
* Support CSV upload for batch predictions
* Deploy to HuggingFace or render as a mobile app

---

##  Author

**Jane Emmanuel**
 [LinkedIn](https://www.linkedin.com/in/jane-emmanuel-/)

---

*Don't forget to give this project a star ⭐ if you found it helpful!*

```
