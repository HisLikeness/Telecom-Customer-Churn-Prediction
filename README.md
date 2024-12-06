# Telecom-Customer-Churn-Prediction
# Problem Statement:
Expresso, an African telecommunications services company, wants to predict the likelihood of its clients switching to a different service provider. The company has provided a dataset containing information on 2.5 million clients, including demographic, behavioral, and transactional data.
## Goal:
The goal is to develop a predictive model that can accurately identify clients who are likely to churn, allowing Expresso to take proactive measures to retain them.

### Variables Description:
The churn dataset includes 19 variables including 15 numeric variables and 04 categorical variables.
- user_id	
- REGION -  The location of each client
- TENURE – The duration in the network
- MONTANT - top-up amount
- FREQUENCE_RECH - Â number of times the customer refilled
- REVENUE - monthly income of each client
- ARPU_SEGMENT - income over 90 days / 3
- FREQUENCE - number of times the client has made an income
- DATA_VOLUME	-  number of connections
- ON_NET - inter expresso call
- ORANGE - call to orange
- TIGO - call to Tigo
- ZONE1 - call to zones1
- ZONE2 - call to zones2
- MRG - a client who is going
- REGULARITY - number of times the client is active for 90 days
- TOP_PACK - the most active packs
- FREQ_TOP_PACK - number of times the client has activated the top pack packages
- CHURN	- variable to predict - Target

#### Correlation Result Interpretation:
Based on the correlation matrix, the following are identified:
##### Strong Positive Correlations
- ARPU_SEGMENT and REVENUE have a very strong positive correlation (1.000), indicating that they are likely measuring the same underlying concept.
- ARPU_SEGMENT, MONTANT, FREQUENCE, FREQUENCE_RECH, and FREQ_TOP_PACK all have strong positive correlations with each other, suggesting that they are related to the same underlying factors.
##### Strong Negative Correlations
- There are no strong negative correlations in the matrix.
##### Weak Correlations
- CHURN has weak correlations with most of the other variables, suggesting that it may not be strongly related to the other factors in the dataset.
- REGION, TENURE, ZONE1, and ZONE2 all have weak correlations with most of the other variables, indicating that they may not be strongly related to the other factors in the dataset.
##### With the observations from the matrix, one can:
- Remove REVENUE from the dataset, as it is highly correlated with ARPU_SEGMENT.
- Combine all strongly correlated variables like FREQUENCE, FREQUENCE_RECH, and FREQ_TOP_PACK into a single variable using dimensionality reduction techniques, such as PCA or t-SNE, to reduce the number of variables in the dataset and identify the most important factors.
