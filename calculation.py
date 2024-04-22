#We do our data analysis here and them add them to the webpage
#import required packages
import pandas as pd
import numpy as np
#read the file
patient_data=pd.read_csv('data/individualDetails.csv')
print (patient_data.columns)
#count total number of patients
total_patient_number = patient_data.id.count()
print (f"number of patients:{total_patient_number}")
print (patient_data.current_status.unique())
#count number of recovered patients
recovered_patient_number = len(patient_data.query("current_status == 'Recovered'"))
print (f"recovered:{recovered_patient_number}")
#count number of hospitalized (active) patients
active_patient_number = len(patient_data.query("current_status == 'Hospitalized'"))
print (f"active: {active_patient_number}")
#count number of deceased (dead) patients
deceased_patient_number = len(patient_data.query("current_status == 'Deceased'"))
print (f"dead: {deceased_patient_number}")