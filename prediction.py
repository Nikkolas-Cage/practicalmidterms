# Import necessary libraries
import pandas as pd
import joblib

# Load the pre-trained model and scaler
model = joblib.load('random_forest_model.pkl')
scaler = joblib.load('scaler.pkl')

# Function to perform data pre-processing
def preprocess_data(data):
    # Assuming 'data' is a DataFrame with the same format as the input dataset
    # Drop 'Outcome' column if it exists (as it's the target variable)
    if 'Outcome' in data.columns:
        data = data.drop('Outcome', axis=1)

    # Perform any necessary data pre-processing steps here
    # For example, handle missing values, scale the features, etc.

    # Use the pre-trained scaler to scale the input features
    data_scaled = scaler.transform(data)

    return data_scaled

# Function to make predictions
def make_prediction(input_data):
    # Create a DataFrame from the input data
    input_df = pd.DataFrame([input_data])

    # Perform data pre-processing
    input_df = preprocess_data(input_df)

    # Make a prediction using the pre-trained model
    prediction = model.predict(input_df)

    return int(prediction[0])

if __name__ == '__main__':
    # Example input data, replace this with user input or your own dataset
    # This data is non diabetic 
    user_input_data = {
      'Pregnancies': 2,
      'Glucose': 110,
      'BloodPressure': 70,
      'SkinThickness': 20,
      'Insulin': 0,
      'BMI': 25.5,
      'DiabetesPedigreeFunction': 0.3,
      'Age': 30
    }
    # Heres the diabetic data
        #'Pregnancies': 1,
        #'Glucose': 128,
        #'BloodPressure': 72,
        #'SkinThickness': 35,
        #'Insulin': 0,
        #'BMI': 33.6,
        #'DiabetesPedigreeFunction': 0.627,
        #'Age': 50
        
    # Make a prediction
    result = make_prediction(user_input_data)

    # Print the result
    print(f'The model predicts that the patient is {"diabetic" if result == 1 else "not diabetic"}.')
