#We do our data analysis here and them add them to the webpage
#import required packages
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.offline as pyo

#read the file
patient_data=pd.read_csv('data/individualDetails.csv')
print (patient_data.columns)
#count total number of patients
total_patient_number = patient_data.id.count()
print (f"number of patients:{total_patient_number}")
patient_status_list=patient_data.current_status.dropna().unique().tolist()

#count number of recovered patients
recovered_patient_number = len(patient_data.query("current_status == 'Recovered'"))
print (f"recovered:{recovered_patient_number}")
#count number of hospitalized (active) patients
active_patient_number = len(patient_data.query("current_status == 'Hospitalized'"))
print (f"active: {active_patient_number}")
#count number of deceased (dead) patients
deceased_patient_number = len(patient_data.query("current_status == 'Deceased'"))
print (f"dead: {deceased_patient_number}")
#based on the category we'll draw a bar graph for all the states
#create the dataframe
df=patient_data[patient_data.current_status == 'Deceased']
stat_df=df.groupby('detected_state')['current_status'].agg('count').reset_index()
print (f"df head:{stat_df.shape}")
#1. Create trace
trace_patient= go.Bar(x=stat_df.detected_state,y=stat_df.current_status)
#2. Add to data
data_patient=[trace_patient]
#3. Create layout
layout_patient=go.Layout(title='Patient status by State',\
                 xaxis={'title':'State'}
				 )
#4. Create figure with layout and data(trace)
fig=go.Figure(data=data_patient,layout=layout_patient)
#5. plot the figure
pyo.plot(fig,filename='plotly_graphs.html')