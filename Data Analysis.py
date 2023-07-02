
##import required libraries

import streamlit as st
import pandas as pd
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)
##title
st.title("Data Analysis")
st.subheader("Data Analysis using Python and Streamlit")

##upload dataset
file = st.file_uploader("Please upload your dataset(in CSV) here:")

##read dataset
if file is not None:
    df = pd.read_csv(file)
    
##show dataset

if file is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Top data"):
            st.write(df.head(10))
        if st.button("Bottom data"):
            st.write(df.tail(10))
            
##data type of each columns
if file is not None:
    if st.button("Data Type"):
        st.text("Data Type of each column of your Dataset - ")
        st.write(df.dtypes)
    

##shape of dataset
if file is not None:
    if st.checkbox("Dimension of the Dataset"):   
        shape = st.radio("Which one?", 
                         ('Rows', 'Columns','Both'))
        
        if shape == 'Rows':
            st.text("Number of Rows in your Dataset:")
            st.write(df.shape[0])
        if shape == 'Columns':
            st.text("Number of Columns in your Dataset:")
            st.write(df.shape[1])
        if shape == 'Both':
            st.text("Number of Rows and Columns of Dataset:")
            st.write(df.shape)
            
##null value
if file is not None:
    null_value = df.isnull().values.any()
    if null_value == True:
        st.checkbox("Null Values in your Dataset.")
        sns.heatmap(df.isnull())
        st.pyplot()
    else:
        st.success("Congrats!! No Missing Value.")
        
##duplicate values
if file is not None:
    dup_test = df.duplicated().any()
    if dup_test == True:
        st.warning("Oops, Your Dataset contains duplicate values.")
        temp = st.selectbox("Do you want to delete duplicate data in your dataset",\
                           ("Select one : ","Yes","No"))
        if temp == "Yes":
           df.drop_duplicates()
           st.text("Duplicate Values are removed.")
        elif temp == "No":
            st.text("It's Okay, No Problem.")
    else:
        st.success("Nice, No Duplicate value found.")

##overall statistics of dataset
if file is not None:
    if st.checkbox("Summary of your dataset"):
        st.write(df.describe(include="all"))
        
##about 

if st.button("About"):
    st.text("Built with Streamlit")
    st.text("Thanks to visit!!")
    st.text("- By Swapnita Goyal")
            