#import required packages
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input,Output
import dash_bootstrap_components as dbc
#create styleshoot for bootstrap
external_stylesheets =[dbc.themes.BOOTSTRAP]
#Do data analysis
#read the file
patient_data=pd.read_csv('data/individualDetails.csv')
#count total number of patients
total_patient_number = patient_data.id.count()
#count number of recovered patients
recovered_patient_number = len(patient_data.query("current_status == 'Recovered'"))
#count number of hospitalized (active) patients
active_patient_number = len(patient_data.query("current_status == 'Hospitalized'"))
#count number of deceased (dead) patients
deceased_patient_number = len(patient_data.query("current_status == 'Deceased'"))

#create the app
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
#add layout
app.layout=html.Div([
	#add heading
	html.H1("Corona Virus Pandemic",style={'color':'#FFFFFF','text-align':'center'}),\
	#row 1
	html.Div([
		#row 1 column 1
		html.Div([
			#card
			html.Div([
				html.Div([html.H3("Total Cases",style={'color':'#FFFFFF','text-align':'center'}),
						  html.H3(total_patient_number,className='text-light',style={'text-align':'center'})
						  ],className='card-body')
			],className='card bg-danger')
		],className='col-md-3'),
	#row 1 column 2
	html.Div([
		#card
		html.Div([
			#card-body
			html.Div([html.H3("Active Cases",style={'color':'#FFFFFF','text-align':'center'}),
						  html.H3(active_patient_number,className='text-light',style={'text-align':'center'})
			],className='card-body')
		],className='card bg-info')

	],className='col-md-3'),
	#row 1 column 3
	html.Div([
		#card
		html.Div([
			#card-body
			html.Div([html.H3("Recovered",style={'color':'#FFFFFF','text-align':'center'}),
						  html.H3(recovered_patient_number,className='text-light',style={'text-align':'center'})
			],className='card-body')
		],className='card bg-warning')
	],
	className='col-md-3'),
	#row 1 column 4
	html.Div([
		#card
		html.Div([
			#card-body
			html.Div([html.H3("Total Death",style={'color':'#FFFFFF','text-align':'center'}),
						  html.H3(deceased_patient_number,className='text-light',style={'text-align':'center'})
			],className='card-body')
		],className='card bg-success')
	],
	className='col-md-3')
	],className='row'),
	#row 2
	html.Div([
		html.Div([html.H3("Row 2 Col 1",style={'color':'#FFFFFF','text-align':'center'})],className='col-md-6'),
		html.Div([html.H3("Row 2 Col 2",style={'color':'#FFFFFF','text-align':'center'})],className='col-md-6')
	],className='row'),
	#row 3
	html.Div([
				html.Div([dcc.Dropdown(id=,options=[],value='Montreal')
					],className='col-md-12')
			],className='row')#row 3 ends
	],className='container')#container ends

if __name__ == "__main__":
    app.run_server(debug=True)