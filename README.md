🩺 Liver Cirrhosis Prediction using Machine Learning
This project aims to detect Liver Cirrhosis using a machine learning model deployed with a Flask web application. Users can enter 37 clinical parameters, and the model predicts whether the patient is likely to suffer from liver cirrhosis.
=========================
📁 Liver Cirrhosis Prediction Project - File Descriptions
=========================

This document explains the role of each file and folder used in the Flask application for liver cirrhosis prediction.

-------------------------
📁 Flask/
-------------------------

1. app.py
   - Main Python script to run the Flask server.
   - Loads the trained Random Forest model and scaler.
   - Defines routes:
     • "/" renders the form (index.html)
     • "/predict" processes form input and shows result.html

2. rf_acc_68.pkl
   - Serialized trained Random Forest model using pickle.
   - Predicts liver cirrhosis based on input features.

3. normalizer.pkl
   - Serialized StandardScaler object.
   - Normalizes user input before prediction.

4. requirements.txt
   - Contains all required Python packages for the project.
   - Used with `pip install -r requirements.txt`

5. readme.md (Flask folder)
   - Describes the structure and purpose of all files in the Flask folder.

-------------------------
📁 dataset/
-------------------------

1. HealthCareData.xlsx
   - Original healthcare dataset used for training the model.
   - Includes clinical features and target (cirrhosis status).

2. readme.md
   - Explains the structure and source of the dataset.

-------------------------
📁 static/
-------------------------

1. background_image.avif
   - Image used as the background for the web app.

2. liver_image.webp
   - Medical image (healthy vs. cirrhosis liver) displayed on the form page.

3. readme.md
   - Explains the purpose of each static file (images, etc.)

-------------------------
📁 templates/
-------------------------

1. index.html
   - The input form page with fields for 37 clinical parameters.
   - Users enter patient data here.

2. result.html
   - Displays prediction result after form submission.
   - Indicates whether the patient is at risk of cirrhosis.

3. readme.md
   - Describes the HTML templates and their function in the Flask app.

-------------------------
✅ Summary
-------------------------

- The app collects 37 features related to liver health.
- Inputs are normalized using the scaler.
- A trained model predicts the presence of liver cirrhosis.
- Results are shown in a styled HTML page.
