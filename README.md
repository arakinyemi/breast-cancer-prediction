# Breast Cancer Prediction Web App

This is a Flask-based web application that predicts whether a breast tumor is **Benign** or **Malignant** based on its features.

## Project Structure
```
/BreastCancer_Project_yourName_matricNo/
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── BreastCancer_hosted_webGUI_link.txt # Submission details
├── model/
│   ├── breast_cancer_model.pkl  # Trained SVM model
│   └── model_building.ipynb     # Model training notebook
├── static/
│   └── style.css           # CSS styling
└── templates/
    └── index.html          # HTML template
```

## How to Run Locally

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application:**
   ```bash
   python app.py
   ```

3. **Open in Browser:**
   Go to `http://127.0.0.1:5000`

## Deployment (Render.com)

1. Push this repository to GitHub.
2. Create a new **Web Service** on Render.
3. Connect your GitHub repository.
4. Use the following settings:
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Click **Create Web Service**.

## Model Info
- **Algorithm:** Support Vector Machine (SVM)
- **Features:** Radius Mean, Texture Mean, Perimeter Mean, Smoothness Mean, Concavity Mean.
