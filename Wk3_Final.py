#Creating a streamlit dashboard after preparing and wrangling a dataset

#Importing dependencies

import pandas as pd 
import streamlit as st 
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

#Pulling in dataset

df=pd.read_csv(r"C:\Users\lilco\myenv\AirPassengers.csv", encoding='utf-8') #I had issues with the system reading my dataset. Had to look up a fix

#Read the data and data types
print(df.head())
print(df.dtypes)

#Converting Month to datetime format
df.Month = pd.to_datetime(df.Month)

#Checking to make sure datatype changed
print(df.dtypes)

#----Creating Streamlit Dashboard-----
#Create Title
st.title('Air Passenger Data')

#Add Image
st.image(r"C:\Users\lilco\myenv\OIP.jpg")
st.divider()

#Create graph to show number of passenger over time
fig = px.line(df, x="Month", y="#Passengers" , title="Number of Passengers over Time")
st.plotly_chart(fig)

#Create graph to show trend over time
fig2 = px.scatter(df, x="Month", y="#Passengers", trendline="ols", title="Time Trend")
st.plotly_chart(fig2)

#Create columns
col1, col2 = st.columns(2)
with col1:  #First column to show average number of passengers per year
   st.subheader("Avg Passengers Per Year", divider='blue')
   df['Year'] = df['Month'].dt.year
   df['Month'] = df['Month'].dt.month
   grouped = df.groupby(df['Year'])
   aggregated = grouped.agg({'#Passengers': 'mean'})
   st.dataframe (aggregated)

with col2:  #2nd column to show max number of passengers per month
   st.subheader("Max Passengers per Month", divider='blue')
   grouped = df.groupby(df['Month'])
   aggregated = grouped.agg({'#Passengers': 'max'})
   st.dataframe (aggregated)
    
 





