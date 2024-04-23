#We do our data analysis here and them add them to the webpage
#import required packages
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.offline as pyo
import plotly_express as px
#read the file
patient_data=pd.read_csv('data/individualDetails.csv')
print (patient_data.columns)
print (f"patient_data:{patient_data.info()}")
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
#Create a pie chart of patients based on state
age_fig = px.pie(patient_data, values='id', names='detected_state',hole=0.25)
age_fig.show()
'''#Create a chart to show patients diagnosed based on date
diagnosys_df=patient_data.groupby('diagnosed_date')['id'].agg(sum).reset_index().sort_values('diagnosed_date',ascending=False)
print (f"diagnosys_data:{diagnosys_df.head()}")
#1. Create trace
diagnosys_trace= go.Bar(x=diagnosys_df.diagnosed_date,y=diagnosys_df.id)
#2. Add to data
diagnosys_data=[diagnosys_trace]
#3. Create layout
#Setting barmode group,will draw two categoriesside by side.
diagnosys_layout=go.Layout(title='Diagnosys by day',\
                 xaxis={'title':'Day'},\
                 yaxis={'title':'Count'}
				 )
#4. Create figure with layout and data(trace)
diagnosys_fig=go.Figure(data=diagnosys_data,
              layout=diagnosys_layout)
#5. plot the figure
pyo.plot(diagnosys_fig,filename='plotly_graphs.html')
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
pyo.plot(fig,filename='plotly_graphs.html')'''