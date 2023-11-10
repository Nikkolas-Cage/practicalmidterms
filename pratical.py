# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
df = pd.read_csv('diabetes.csv')  # Replace 'diabetes_dataset.csv' with your actual file name

# Split the data into features (X) and target variable (y)
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Perform data scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train different machine learning models
models = {
    'Random Forest': RandomForestClassifier(),
    'Support Vector Machine': SVC(),
    'K-Nearest Neighbors': KNeighborsClassifier()
}

accuracies = []

for model_name, model in models.items():
    # Train the model
    model.fit(X_train_scaled, y_train)

    # Save the trained model
    joblib.dump(model, f'{model_name.lower().replace(" ", "_")}_model.pkl')

    # Test the model on the test set
    y_pred = model.predict(X_test_scaled)
    test_accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(test_accuracy)
    print(f'{model_name} - Test Accuracy: {test_accuracy}')

# Visualize accuracy for all three models
plt.bar(models.keys(), accuracies, color=['blue', 'orange', 'green'])
plt.ylabel('Accuracy')
plt.title('Test Accuracy of Different Models')
plt.show()
print("")

# Visualize feature importance for the Random Forest model
random_forest_model = models['Random Forest']
feature_importances = random_forest_model.feature_importances_
feature_names = X.columns
sorted_idx = feature_importances.argsort()
print("")
plt.barh(range(len(sorted_idx)), feature_importances[sorted_idx], align="center")
plt.yticks(range(len(sorted_idx)), feature_names[sorted_idx])
plt.xlabel("Feature Importance")
plt.title("Random Forest Feature Importance")
plt.show()
