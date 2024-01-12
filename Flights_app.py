import streamlit as st
import pandas as pd
import category_encoders
import sklearn
import xgboost
import joblib

Model = joblib.load("Model.pkl")
Inputs = joblib.load("Inputs.pkl")

def Prediction (Airline , Source , Destination , Total_Stops , Month , Day , Day_Number , Duration_Length , Dep_Daytime , Arrival_Daytime , Distance , Meal , Check_in_Baggage ):
    df = pd.DataFrame(columns= Inputs)
    df.at[ 0 ,"Airline"] = Airline
    df.at[ 0 ,"Source"] = Source
    df.at[ 0 ,"Destination"] = Destination
    df.at[ 0 ,"Total_Stops"] = Total_Stops
    df.at[ 0 ,"Month"] = Month
    df.at[ 0 ,"Day"] = Day
    df.at[ 0 ,"Day_Number"] = Day_Number
    df.at[ 0 ,"Duration_Length"] = Duration_Length
    df.at[ 0 ,"Dep_Daytime"] = Dep_Daytime
    df.at[ 0 ,"Arrival_Daytime"] = Arrival_Daytime
    df.at[ 0 ,"Distance"] = Distance
    df.at[ 0 ,"Meal"] = Meal
    df.at[ 0 ,"Check_in_Baggage"] = Check_in_Baggage
    Result = Model.predict(df)
    return Result[0]

def Main():
    Airline = st.selectbox('Airline Company' , ['Air Asia','Air India','GoAir','IndiGo','Jet Airways','Multiple carriers','SpiceJet','Vistara'])
    Source = st.selectbox('Source' , ['Banglore','Chennai','Delhi','Kolkata','Mumbai'])
    Destination = st.selectbox('Destination' , ['Banglore','Cochin','Delhi','Hyderabad','Kolkata','New Delhi'])
    Total_Stops = st.selectbox('Number of Stops' , ['non-stop', '1 stop', '2 stops', '3 stops' , '4 stops' ])
    Month = st.selectbox('Journeys Month' , ['March','April','May','June'])
    Day = st.selectbox('Journeys Day' , ['Friday','Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday'])
    Day_Number = st.selectbox('Journys Day Number' , [1 , 3 , 6 , 9 , 12 , 15 , 18 , 21 , 24 , 27])
    Duration_Length = st.selectbox('Duration' , ['Short_Duration','Medium_Duration','Long_Duration'])
    Dep_Daytime = st.selectbox('Depature Time' , ['Early_Morning','Late_Morning','Early_Afternoon','Late_Afternoon','Evening','Night'])
    Arrival_Daytime = st.selectbox('Arrival Time' , ['Early_Morning','Late_Morning','Early_Afternoon','Late_Afternoon','Evening','Night'])
    Distance = st.selectbox('Distance' , ['Short_Distance','Medium_Distance','Long_Distance'])
    Meal = st.selectbox('Meal', [0,1])
    Check_in_Baggage = st.selectbox('Baggage' , [0,1])
    if st.button('Predict!'):
        Result = Prediction(Airline , Source , Destination , Total_Stops , Month , Day , Day_Number , Duration_Length , Dep_Daytime , Arrival_Daytime , Distance , Meal , Check_in_Baggage )
        st.text(f'The Price of the flight will be {round(Result,1)}₹') 
Main()
    
