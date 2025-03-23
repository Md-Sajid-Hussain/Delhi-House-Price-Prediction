import pandas as pd
import pickle as pk
import streamlit as st

model = pk.load(open(r'D:\ML Project\House_prediction_model.pkl', 'rb'))


st.header("Delhi House Price Pridictor")
data = pd.read_csv(r'D:\ML Project\Cleaned_data.csv')

sqft = st.number_input("Enter Total Sqft")
bedro = st.number_input("Enter No of Bedrooms")
bath = st.number_input("Enter No of Bathrooms")
furni = st.selectbox("Choose the Furnicher Status", data['Furnishing'].unique())
loc = st.selectbox('Choose the Location', data['Locality'].unique())


input =pd.DataFrame([[sqft,bedro,bath,furni,loc]],columns =['Area','BHK','Bathroom','Furnishing','Locality'])

if st.button("Pridict Price"):
    output = model.predict(input)
    out_str = 'Price of the House is ' + str(output[0])
    st.write(out_str)