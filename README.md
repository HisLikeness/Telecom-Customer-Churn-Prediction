# Telecom-Customer-Churn-Prediction
This repository contains a predictive modeling project aimed at identifying clients likely to switch to a different telecommunications service provider. The project utilizes a dataset provided by Expresso, an African telecommunications services company, containing demographic, behavioral, and transactional data on 2.5 million clients.

## Goal
The primary objective of this project is to develop a machine-learning model that accurately predicts client churn, enabling Expresso to take proactive measures to retain clients.

## Dataset Description
- Source: https://drive.google.com/file/d/12_KUHr5NlHO_6bN5SylpkxWc-JvpJNWe/view
- The dataset includes 19 variables, comprising 15 numeric and 4 categorical variables. These variables capture various aspects of client behavior, including demographic information, usage patterns, and revenue data.

## Key Findings
Correlation analysis revealed strong positive correlations between variables such as ARPU_SEGMENT, REVENUE, MONTANT, FREQUENCE, FREQUENCE_RECH, and FREQ_TOP_PACK. Weak correlations were observed between CHURN and most other variables. Based on these findings, dimensionality reduction techniques can be applied to combine strongly correlated variables and identify the most important factors contributing to client churn.

## Project Structure
This repository contains the following:
- Data: The raw dataset provided by Expresso
- Code: Python scripts for data preprocessing, feature engineering, and model development
- Models: Trained machine learning models for predicting client churn
- Results: Evaluation metrics and visualizations of model performance

## How to Run
- first run: "python main.py train" # to train the model
- then streamlit run app.py
  
## Contributing
Contributions to this project are welcome. If you're interested in collaborating, please fork the repository and submit a pull request with your changes.
