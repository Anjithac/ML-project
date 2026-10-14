# 🛡️ Fraud Detection System Using Machine Learning

## 📌 Project Overview
This project uses machine learning to identify potentially fraudulent financial transactions. It includes data analysis, model predictions, and a Streamlit web application for interactive fraud detection.

## 🎯 Business Problem
Financial fraud can cause significant financial losses. Detecting suspicious transactions helps businesses identify potential fraud and improve transaction security.

## 🎯 Objectives
- Analyze transaction data to identify patterns.
- Explore fraudulent and legitimate transactions.
- Build a machine learning model for fraud prediction.
- Develop an interactive Streamlit dashboard.

## 📂 Project Structure
- `Fraud_Detection_analysis.ipynb` — Data analysis and model development.
- `app.py` — Streamlit web application.
- `fraud_detection_model.pkl` — Saved machine learning model.
- `AIML_Dataset.csv` — Dataset used for analysis.
- `requirements.txt` — Required Python libraries.
- `README.md` — Project documentation.

## 📊 Dataset
The project uses transaction data containing fields such as:
- `step`
- `type`
- `amount`
- `oldbalanceOrg`
- `newbalanceOrig`
- `oldbalanceDest`
- `newbalanceDest`
- `isFraud`
- `isFlaggedFraud`

## 🔍 Exploratory Data Analysis
The analysis notebook explores transaction patterns, fraud distribution, and relationships between transaction amounts and account balances.

## 🤖 Machine Learning
The project includes a saved machine learning model for predicting potentially fraudulent transactions.

**Evaluation metrics:** Add the actual precision, recall, F1-score, and other evaluation results from your notebook here.

## 🖥️ Streamlit Application
The interactive application allows users to:
- Enter transaction details.
- Generate a fraud prediction.
- View the predicted fraud risk.
- Explore the prediction probability when supported by the model.

## 🛠️ Technologies Used
- Python
- Pandas and NumPy
- Scikit-learn
- Matplotlib and Seaborn
- Jupyter Notebook
- Streamlit
- Joblib

## 🚀 How to Run the Project

### 1. Install the dependencies
```bash
python -m pip install -r requirements.txt
```

### 2. Start the application
```bash
python -m streamlit run app.py
```

### 📈 Results
Add your actual model results and key findings here after checking your notebook. Do not report unverified performance numbers.

## 🔮 Future Improvements
- Improve fraud detection for highly imbalanced data.
- Compare different machine learning models.
- Tune the prediction threshold.
- Add more evaluation visualizations.
- Deploy the application online.

## 👩‍💻 Author
**Anjitha C**

- GitHub: https://github.com/Anjithac
- LinkedIn: https://www.linkedin.com/in/anjitha-c-remesh/

## ⚠️ Disclaimer
This project is intended for educational and demonstration purposes. Predictions should not be treated as definitive proof of financial fraud.