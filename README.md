# Phishing-URL-Detection
Every URL is broken into several parts. Features are extracted from the URs which help ensuring whether an URL is phishing or not. Machine Learning techniques are applied to build an effective model for predicting the legitimacy of the website provided which is further deployed 

You need to deploy the model yourself. Save the model using a pickle file. We used StreamLit to deploy the model.
I couldn't upload the pickle file because it a file with a large space.
Inorder to use ngrok, you need to have an account in ngrok. The system commands are given in 'ngrok token' file

the correct order to run the lines for setting up and exposing your local application using ngrok and Streamlit:
1. Log in to ngrok and get the authtoken
2. Add the ngrok authtoken to the config:  ngrok config add-authtoken your_authtoken //change your_authtoken to you authtoken
3. Start the streamlit app:  streamlit run app_ultimate.py
4. Expose your local server using ngrok:  ngrok http http://localhost:8501  //your application can run on some other port
This sequence ensures that your ngrok is authenticated, your Streamlit app is running, and then your local server is exposed to the internet.
