import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image

# Assuming NewFeatures module contains the necessary functions for feature extraction
import NewFeatures

pickle_in = open("./rf_model.pkl","rb")
classifier = pickle.load(pickle_in)


def predict_url_phishing(url):
    # Extract features from the URL using NewFeatures.py module
    lexical_features = NewFeatures.main(url)
    #print(lexical_features,'########')
    lexical_features = [0 if x == 'False' else 1 if x == 'True' else x for x in lexical_features]
    lf_array = np.array(lexical_features).reshape(1,-1)
    #print(lf_array)
    prediction = classifier.predict(lf_array)
    #prediction = classifier.predict(np.array(lexical_features).reshape(-1,1))
    return prediction, lexical_features


def main():
    st.title("Check for Legitimate/Malicious URLs")
    html_temp = """
    <div style="background-color:#4169E1;padding:10px">
    <h2 style="color:white;text-align:center;"> Phishing URL Checker </h2>
    </div>
    """
    
    st.markdown(html_temp, unsafe_allow_html=True)
    st.subheader("Designed by L.O.K.I.")
    st.subheader("Lookout Operatives Keeping the Internet")

    url = st.text_input("Enter the URL you want to check", "", key="url_input", placeholder="Type Here")

    
    pred, feat = predict_url_phishing(url)

    if st.button("Predict"):
        if pred == 1:
            st.success('The URL is Phishing - Malicious')
            st.image("phish.jpg", use_column_width=True)
        elif pred == 2:
            st.success('The URL is Non-Phishing - Legitimate')
            st.image("nonphish.jpg", use_column_width=True)

    
    if st.button("Data Extracted"):
        st.write("## Extracted Features")
        feature_names = ["No. of '.'s in URL", "No. of '-'s in URL", "No. of '_'s in URL", "No. of '/'s in URL", "No. of '?'s in URL", 
                "No. of '='s in URL", "No. of '@'s in URL","No. of '&'s in URL","No. of '!'s in URL","No. of ' 's in URL",
                "No. of '~'s in URL","No. of ','s in URL", "No. of '+'s in URL","No. of '*'s in URL","No. of '#'s in URL",
                "No. of '$'s in URL","No. of '%'s in URL", "Top level domain character length", "Number of characters", "No. of alphabets in URL",
                "Domain lookup time response", "Domain activation time (in days)", "Domain expiration time (in days)", "Has URL shortener", "No. of '.'s in domain", 
                "No. of '-'s in domain", "No. of '_'s in domain", "No. of '/'s in domain", "No. of '?'s in domain", "No. of '='s in domain", 
                "No. of '@'s in domain", "No. of '&'s in domain", "No. of '!'s in domain", "No. of ' 's in domain", "No. of '~'s in domain", 
                "No. of ','s in domain", "No. of '+'s in domain", "No. of '*'s in domain", "No. of '#'s in domain", "No. of '$'s in domain",
                "No. of '%'s in domain", "No. of vowels in Domain", "length of the Domain", "Does IP Exist", "Does Server Clinet exist", 
                "No. of '.'s in path", "No. of '-'s in path", "No. of '_'s in path", "No. of '/'s in path", "No. of '?'s in path", 
                "No. of '='s in path", "No. of '@'s in path", "No. of '&'s in path", "No. of '!'s in path", "No. of ' 's in path", 
                "No. of '~'s in path", "No. of ','s in path", "No. of '+'s in path", "No. of '*'s in path", "No. of '#'s in path", 
                "No. of '$'s in path", "No. of '%'s in path", "Length of the path", "No. of '.'s in file", "No. of '-'s in file", 
                "No. of '_'s in file", "No. of '/'s in file", "No. of '?'s in file", "No. of '='s in file", "No. of '@'s in file", 
                "No. of '&'s in file", "No. of '!'s in file", "No. of ' 's in file", "No. of '~'s in file", "No. of ','s in file", 
                "No. of '+'s in file", "No. of '*'s in file", "No. of '#'s in file", "No. of '$'s in file", "No. of '%'s in file", 
                "Length of the file", "No. of '.'s in parameters", "No. of '-'s in parameters", "No. of '_'s in parameters", "No. of '/'s in parameters", 
                "No. of '?'s in parameters", "No. of '='s in parameters", "No. of '@'s in parameters", "No. of '&'s in parameters", "No. of '!'s in parameters", 
                "No. of ' 's in parameters", "No. of '~'s in parameters", "No. of ','s in parameters", "No. of '+'s in parameters", "No. of '*'s in parameters", 
                "No. of '#'s in parameters", "No. of '$'s in parameters", "No. of '%'s in parameters", "Length of the parameters", "No. of parameters", "whether email exist"]
        
        feat = ['N/A' if x == -1 else x for x in feat]
        data = {"Feature": feature_names, "Value": feat}
        st.table(data)

    if st.button("About"):
        st.text("Brought to you by")
        st.markdown("**Anurag Joardar** & **Debayan Datta** - RKMVERI")
        with st.expander("Contact details"):
            st.markdown("**Anurag**: anuragjoardar10@gmail.com")
            st.markdown("**Debayan**: debayan.datta0206@gmail.com")




if __name__=='__main__':
    main()
#-----------------------------------------------    
