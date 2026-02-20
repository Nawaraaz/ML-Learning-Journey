# Step 2: Streamlit App (app.py)

import streamlit as st
import joblib
import numpy as np

# Loading trained model
model = joblib.load("student_marks_model.pkl")
st.title("Student Marks Prediction using Logistic Regression")
st.write("Enter student details to predict result")

# Created a slider for User Inputs
study_hours = st.slider("Study Hours", 0.0, 10.0, 3.0)
attendance = st.slider("Attendance (%)", 40, 100, 70)

# Prediction Button to display predicition after being clicked
if st.button("Predict"):
    features = np.array([[study_hours, attendance]])
    prediction = model.predict(features)[0]    
    if prediction == 1:
        st.success("Prediction: Pass")
    else:
        st.error("Prediction: Fail")
