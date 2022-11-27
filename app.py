import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write("""
# Credit Card Approval Prediction App

This app predicts the credit card approval probablity
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    num = st.number_input("INPUT_NUMBER",min_value=0,max_value=2000000,step=1)
    
    data = {'INPUT_NUMBER': num,
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())

#Model Inferencing

st.subheader('Class labels and their corresponding index number')
st.write(pd.DataFrame({'Labels': ['Even','Odd']}))

st.subheader('Prediction')
if df['INPUT_NUMBER']%2 == 0:
    st.write('Even')
else:
    st.write('Odd')
