import streamlit as st
import plotly_express as px
import pandas as pd
import numpy as np
import datetime

data = pd.read_csv('cleaned_data.csv', index_col=0)

# Sidebar
st.sidebar.title("Sidebar Search")
st.sidebar.info("This is an application for our data analysis")

facility = st.sidebar.multiselect('What is the facility?', data['facilityID'].unique())
apt_title = st.sidebar.multiselect('Select Appointment?', data['appointmentTitle'].unique())

# Page

'''
# Observations:
- We can see that majority of our data is duplicates.
- Our memory usage has comedown from ***183 MB*** to ***4 MB*** .
- eventDate must be changed to a DateTime type
- We do not know what **pid** , **providerID** and **appointmentStatus** actually represent
- our memory usage is 183.1 MB, which will slow things down when using complex transformations.
- We need a different data slice from out database. This dataset is very imbalances.
- If we had access to the database scema, it would help in feature engineering


--------------------------------------------------------------------------------------------------------------------------------------

# ML model

--------------------------------------------------------------------------------------------------------------------------------------

## Dataset and Historical Analysis
'''
st.dataframe(data)
'''
### Unique counts
'''

st.dataframe(data.nunique()) 
'''
### Discription of Numerical 
'''
st.dataframe(data.describe()) 

'''
### Appointment Titles

'''
st.dataframe(data.appointmentTitle.value_counts())
'''
### Facility
'''
st.dataframe(data.facilityID.value_counts())

'''
### Appointment Status
'''
st.dataframe(data.appointmentStatus.value_counts())

'''
### Datewise
'''
st.dataframe(data.eventDate.value_counts())

'''
### Grouped 
'''
st.dataframe(data.groupby(['eventDate','lastName', 'firstName','facilityID']).nunique().sort_values(by=['facilityID'], ascending=False).head(20))

st.dataframe(data.groupby(['eventDate', 'facilityID','appointmentTitle']).nunique())

'''
---------------------------------------------------------------------------------------------------------------
'''
'''
## Running the model
'''

t = st.time_input("Run the model at:", datetime.time(8, 45))
st.write("The model will run at:", t)

option = st.selectbox( "How would you like to be contacted?", ("Email", "Home phone", "Mobile phone"))

'''
---------------------------------------------------------------------------------------------------------------
'''

'''
## Input from streamlit
'''

Patitent = st.text_input("Name of Patient ")
sex = st.selectbox("Sex",options=['Male' , 'Female'])
age = st.slider("Age", 1, 100,1)
p_class = st.selectbox("Patient Class",options=['A Class' , 'B Class' , 'C Class'])


# Filter dataframe
#new_df = data[(data['facilityID'].isin(facility)) & (data['appointmentTitle'].isin(apt_title))]
# write dataframe to screen
#st.dataframe(new_df)
