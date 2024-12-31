import streamlit as st
import numpy as np
import joblib
from sklearn.base import is_classifier

def load_model(file_path):
    return joblib.load(file_path)

# Create and run the Streamlit web application
def run_streamlit_app():
    st.title('Customer Churn Prediction App')
    
    # Load the saved model and scaler
    try:
        model = load_model('models/churn_model.pkl')
        scaler = load_model('models/scaler.pkl')
        st.write("Model and Scaler loaded successfully.")
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return
    
    # Create input fields for features
    st.header('Enter Customer Information')
    
    col1, col2 = st.columns(2)
    
    with col1:
        montant = st.number_input('MONTANT (Amount Spent)', min_value=0.0)
        frequence_rech = st.number_input('FREQUENCE_RECH (Recharge Frequency)', min_value=0.0)
        revenue = st.number_input('REVENUE (Monthly Income)', min_value=0.0)
        arpu_segment = st.number_input('ARPU_SEGMENT (income over 90 days/3)', min_value=0.0)
        frequence = st.number_input('FREQUENCE (No. of times income was made)', min_value=0.0)
        data_volume = st.number_input('DATA_VOLUME (No. of Connection)', min_value=0.0)
        on_net = st.number_input('ON_NET (No. of inter expresso call)', min_value=0.0)
            
    with col2:
        orange = st.number_input('ORANGE (call to orange)', min_value=0.0)
        tigo = st.number_input('TIGO (call to Tigo)', min_value=0.0)
        tenure_months = st.number_input('TENURE_MONTHS (No. of Months)', min_value=0.0)
        regularity = st.number_input('REGULARITY', min_value=0.0)
        freq_top_pack = st.number_input('FREQ_TOP_PACK', min_value=0.0)
        usage_ratio = data_volume / (montant + 1)
        call_ratio = (on_net + orange + tigo) / (montant + 1)
        region_encoded = st.number_input('REGION_ENCODED', min_value=0)
        top_pack_encoded = st.number_input('TOP_PACK_ENCODED', min_value=0)
        mrg_encoded = st.number_input('MRG_ENCODED', min_value=0)
    
    
    if st.button('Predict Churn'):
        # Calculate derived features
        usage_ratio = data_volume / (montant + 1)
        call_ratio = (on_net + orange + tigo) / (montant + 1)
        
        # Create feature array
        features = np.array([
            montant, frequence_rech, revenue, arpu_segment, frequence,
            data_volume, on_net, orange, tigo, tenure_months,
            regularity, freq_top_pack, usage_ratio, call_ratio,
            region_encoded, top_pack_encoded, mrg_encoded
        ]).reshape(1, -1)
        
        # Display the feature array
        st.write(f"Features: {features}")
        
        # Scale features
        features_scaled = scaler.transform(features)
        st.write(f"Scaled features: {features_scaled}")
        
        # Make prediction
        prediction = model.predict(features_scaled)
        probability = model.predict_proba(features_scaled)
        
        # Display results
        st.header('Prediction Results')
        if prediction[0] == 1:
            st.error('⚠️ High Risk of Churn')
        else:
            st.success('✅ Low Risk of Churn')
        
        st.write(f'Churn Probability: {probability[0][1]:.2%}')

if __name__ == "__main__":
    run_streamlit_app()

