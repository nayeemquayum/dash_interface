#We''' do our data analysis here and them add them to the webpage
#import required packages
import pandas as pd
import numpy as np
#read the file
patient_data=pd.read_csv('data/individualDetails.csv')
print (patient_data.head())