import pandas as pd
from config import DATA_PATH

def load_data(file_path=DATA_PATH):
    """Load the dataset from CSV file"""
    try:
        df = pd.read_csv("c:\\Users\\HP\\Documents\\STUDY\\DATA SCIENCE AND ANALYSIS - GOMYCODE\\Data Sets\\Expresso_churn_dataset.csv")
        print(f"Data loaded successfully from {file_path}")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None