# Phishing URL Detection using Machine Learning

This project explores the development and evaluation of various machine learning models to enhance the efficiency of phishing URL detection. Every URL is broken into several parts. Features are extracted from the URs which help ensuring whether an URL is phishing or not. Machine Learning techniques are applied to build an effective model for predicting the legitimacy of the website provided which is further deployed.
It involves:

1. **Feature Extraction**: Analyzing URLs to extract lexical and web-scraped features that can distinguish between phishing and legitimate URLs.

2. **Modeling**: Implementing and comparing different machine learning algorithms, including K-Nearest Neighbors, Naive Bayes, Logistic Regression, Decision Trees, Random Forests, AdaBoost, XGBoost, and Support Vector Machines.

3. **Performance Evaluation**: Assessing the models based on metrics such as accuracy, precision, recall, and F1-score to determine the most effective approach.


### Need for Phising URL Detection System

Phishing poses a substantial threat to individuals and organizations, leading to identity theft and financial fraud. Traditional detection methods are often inadequate due to the constantly changing nature of phishing tactics. Therefore, there is a critical need for more sophisticated and adaptive detection mechanisms to better protect users from phishing attempts.

## Requirements
    requests == 2.31.0
    whois == 1.20240129.2
    scikit-learn == 1.4.0
    pandas == 2.1.3
    python == 3.10.11

## Dataset Description

- Dataset is available at https://web.cs.hacettepe.edu.tr/~selman/grambeddings-dataset/

- Dataset contains 400K legitimate and 400K Phishing URLs.

- We use 350000 URLs for our Classification/Modeling purpose.

## Feature Extraction
A total of 100 features (lexical and web-scrapped features) are extracted from the URLs.

- Separate URLs from class annotation column into a new CSV.
- Run Extraction.ipynb

## Modeling

We use a number of ML models from Scikit-Learn Library for the purpose of modeling to predict if an URL is Phishing or Non-Phishing.

- K-Nearest Neighbours Algorithm
- Support Vector Machine
- Naive Bayes algorithm
- Logistic Regression
- Decision Tree
- Random Forest
- Adaboost
- XGBoost

For Preproccessing and Modeling run **URL Phishing Detection.ipynb**

## Deployment

You need to deploy the model yourself. Save the model using a pickle file. We used StreamLit to deploy the model.
I couldn't upload the pickle file because it a file with a large space.
Inorder to use ngrok, you need to have an account in ngrok. The system commands are given in 'ngrok token' file

the correct order to run the lines for setting up and exposing your local application using ngrok and Streamlit:
1. Log in to ngrok and get the authtoken
2. Add the ngrok authtoken to the config:  ngrok config add-authtoken your_authtoken //change your_authtoken to you authtoken
3. Start the streamlit app:  streamlit run app_ultimate.py
4. Expose your local server using ngrok:  ngrok http http://localhost:8501  //your application can run on some other port
This sequence ensures that your ngrok is authenticated, your Streamlit app is running, and then your local server is exposed to the internet.
