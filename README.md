### README.md

#### Diabetes Prediction Flask App

This repository contains a Flask application for predicting diabetes based on a trained machine learning model. The machine learning model is trained using a dataset with features such as pregnancies, glucose level, blood pressure, etc. The training and visualization of the model are performed using the `practical.py` script.

### Flask App (`app.py`)

#### Setup Instructions:

1. Install the required packages by running:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the Flask application:

    ```bash
    python app.py
    ```

3. Once the Flask app is running, you can make predictions by sending a POST request to the `/predict` endpoint with input data in JSON format.

    Example using `curl`:

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"Pregnancies": 6, "Glucose": 148, "BloodPressure": 72, "SkinThickness": 35, "Insulin": 0, "BMI": 33.6, "DiabetesPedigreeFunction": 0.627, "Age": 50}' http://localhost:5000/predict
    ```
