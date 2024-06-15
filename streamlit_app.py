import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import pickle as pkl

st.write("Hellow worlds")
with st.sidebar:
    monthlyIncome = st.number_input ("Monthly Income ($)",0,500000,1000,1)
    maritalStatus = st.selectbox("Marital Status",("Single","Married"))
    environmentSatisfaction = st.selectbox("Environment Satisfaction",("Very Satisfied","Satisfied","Disatisfied","Very Disatisfied"))
    yearsAtCompnay = st.number_input ("No. Years At Company",0,50,1,1)
    yearsWithCurrentManager = st.number_input ("No. Years With Current Manager",0,yearsAtCompnay,1,1)
    Age = st.number_input ("Age",18,60,20,1)
    jobSatisfaction = st.selectbox("Job Satisfaction",("Very Satisfied","Satisfied","Disatisfied","Very Disatisfied"))
    with st.expander("Additional Fields"):
        #don't forget to convert to miles ( multiply by 0.6 )
        distanceFromeHome = st.slider("Distance From Home (KM)",1,200,2,1)
        