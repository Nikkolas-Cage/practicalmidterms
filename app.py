from flask import Flask, request, jsonify
from flask_cors import CORS  # Import the CORS module
import pandas as pd
import joblib

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "http://localhost:3000"}})

# ... (rest of your Flask app code remains the same)

# Load the pre-trained model and scaler
model = joblib.load('random_forest_model.pkl')
scaler = joblib.load('scaler.pkl')

# Function to perform data pre-processing
def preprocess_data(data):
    if 'Outcome' in data.columns:
        data = data.drop('Outcome', axis=1)

    # Perform any necessary data pre-processing steps here
    # For example, handle missing values, scale the features, etc.

    # Use the pre-trained scaler to scale the input features
    data_scaled = scaler.transform(data)

    return data_scaled

# Function to make predictions
def make_prediction(input_data):
    input_df = pd.DataFrame([input_data])
    input_df = preprocess_data(input_df)
    prediction = model.predict(input_df)
    return int(prediction[0])

# Flask route to handle predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.get_json()
        result = make_prediction(input_data)
        response = {'prediction': result, 'message': 'Prediction successful.'}
    except Exception as e:
        response = {'prediction': None, 'message': f'Error: {str(e)}'}
    return jsonify(response)

# Sample route for testing
@app.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'Flask app is running successfully!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
