from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the model and scaler
model = pickle.load(open('rf_acc_68.pkl', 'rb'))
scaler = pickle.load(open('normalizer.pkl', 'rb'))

# Define the 37 features
features = [
    'Age', 'Gender (0=Male, 1=Female)', 'Total Bilirubin', 'Direct Bilirubin', 'Alkaline Phosphotase',
    'Alamine Aminotransferase', 'Aspartate Aminotransferase', 'Total Proteins', 'Albumin',
    'Albumin and Globulin Ratio', 'SGPT', 'SGOT', 'Hemoglobin', 'Platelets', 'WBC', 'RBC',
    'Mean Corpuscular Volume', 'Mean Corpuscular Hemoglobin', 'Mean Corpuscular Hemoglobin Concentration',
    'Packed Cell Volume', 'Serum Creatinine', 'Blood Urea', 'Sodium', 'Potassium', 'Blood Pressure',
    'Diabetes (0=No, 1=Yes)', 'Obesity (0=No, 1=Yes)', 'Smoking (0=No, 1=Yes)', 'Alcohol (0=No, 1=Yes)',
    'Hypertension (0=No, 1=Yes)', 'Fatigue (0=No, 1=Yes)', 'Nausea (0=No, 1=Yes)', 'Vomiting (0=No, 1=Yes)',
    'Ascites (0=No, 1=Yes)', 'Edema (0=No, 1=Yes)', 'Spider Angiomas (0=No, 1=Yes)' , 'Enlarged Liver (0=No, 1=Yes)'
]

@app.route('/')
def home():
    return render_template('index.html', features=features)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = [float(request.form.get(feature)) for feature in features]

        if len(input_data) != 37:
            return f"Error: Expected 37 input values, but got {len(input_data)}"

        input_array = np.array(input_data).reshape(1, -1)
        input_scaled = scaler.transform(input_array)
        prediction = model.predict(input_scaled)[0]

        return render_template('result.html', prediction=prediction)

    except Exception as e:
        return f"Error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
