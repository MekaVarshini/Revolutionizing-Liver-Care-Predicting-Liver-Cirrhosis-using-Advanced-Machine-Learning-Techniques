🩺 Liver Cirrhosis Prediction using Machine Learning
This project aims to detect Liver Cirrhosis using a machine learning model deployed with a Flask web application. Users can enter 37 clinical parameters, and the model predicts whether the patient is likely to suffer from liver cirrhosis.
Flask/
│
├── app.py                      # Flask web server
├── rf_acc_68.pkl               # Trained Random Forest model
├── normalizer.pkl              # StandardScaler for input preprocessing
├── requirements.txt            # Python dependencies
├── readme.md                   # Description of Flask folder
│
├── dataset/
│   ├── HealthCareData.xlsx     # Raw healthcare dataset
│   └── readme.md               # Dataset info
│
├── static/
│   ├── background_image.avif   # Background image
│   ├── liver_image.webp        # Liver illustration image
│   └── readme.md               # Description of assets
│
└── templates/
    ├── index.html              # Input form for 37 features
    ├── result.html             # Output prediction view
    └── readme.md               # Description of template functionality
