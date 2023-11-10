### README.md

#### Diabetes Prediction Flask App

https://github.com/Nikkolas-Cage/practicalmidterms/assets/47923060/88090e28-fdb6-482b-bdc7-4cffae7adb29


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

#### Running the Flask Application:

To run the Flask application:

1. Ensure you have Python installed on your system.

2. Navigate to the root directory of the project.

3. Run the following commands:

    ```bash
    pip install -r requirements.txt
    python app.py
    ```

4. The Flask app will be running at [http://localhost:5001](http://localhost:5001).

#### Testing:

You can test the Flask app by accessing the sample route at [http://localhost:5001/test](http://localhost:5001/test). It should return a JSON response with the message "Flask app is running successfully!"

```bash
curl http://localhost:5001/test
```

Feel free to reach out if you have any questions or encounter any issues.

### Next.js Frontend (`App.js`)

This repository also includes a Next.js frontend (`App.js`) for interacting with the Flask backend. The frontend provides a user interface for entering patient data and obtaining diabetes predictions from the Flask API.

#### Setup Instructions:

1. Navigate to the `frontend` directory:

    ```bash
    cd frontend
    ```

2. Install the required packages:

    ```bash
    npm install
    ```

3. Run the Next.js application:

    ```bash
    npm run dev
    ```

#### Usage:

1. Access the application at [http://localhost:3000](http://localhost:3000) in your web browser.

2. Enter patient data in the provided text fields.

3. Click the "Submit Prediction" button to send the data to the Flask API for prediction.

4. View the prediction result on the page.

### Sample Values:

#### Diabetic

- Pregnancies: 1
- Glucose: 128
- BloodPressure: 72
- SkinThickness: 35
- Insulin: 0
- BMI: 33.6
- DiabetesPedigreeFunction: 0.627
- Age: 50

#### Non-Diabetic

- Pregnancies: 2
- Glucose: 110
- BloodPressure: 70
- SkinThickness: 20
- Insulin: 0
- BMI: 25.5
- DiabetesPedigreeFunction: 0.3
- Age: 30

Feel free to reach out if you have any questions or encounter any issues.
