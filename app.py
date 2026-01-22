import os
import numpy as np
import pandas as pd
import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the trained model
model_path = os.path.join('model', 'breast_cancer_model.pkl')
with open(model_path, 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from the form
        features = [
            float(request.form['radius_mean']),
            float(request.form['texture_mean']),
            float(request.form['perimeter_mean']),
            float(request.form['smoothness_mean']),
            float(request.form['concavity_mean'])
        ]
        
        # Create a DataFrame for the model (since it was trained on a DataFrame)
        feature_names = ['radius_mean', 'texture_mean', 'perimeter_mean', 'smoothness_mean', 'concavity_mean']
        input_data = pd.DataFrame([features], columns=feature_names)
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        
        # Map prediction to label (0 -> Benign, 1 -> Malignant)
        result = "Malignant" if prediction == 1 else "Benign"
        
        return render_template('index.html', prediction_text=f'Prediction: {result}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
