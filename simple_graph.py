import numpy as np
import pandas as pd
import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from dash import Dash

np.random.seed(42)

x1=np.random.randint(1,101,100)
y1=np.random.randint(1,101,100)

app=dash.Dash()
server=app.server


app.layout = html.Div([html.H1('Hello Dash', 
                               style={'textAlign': 'center'}), 
                       html.H2('Przechodzimy do wykonania zadania',
                              style={'textAlign': 'center'}),
                       html.H3('Poniżej zostanie przedstawiony graph',
                              style={'textAlign': 'center'}),
                      dcc.Graph(id='Example',
                               figure={'data':[go.Scatter(x=x1, 
                                                       y=y1,
                                                       mode='markers',
                                                         marker={'size':12,
                                                                'color':'rgb(15, 60, 120)',
                                                                'symbol':'pentagon'})],
                                      'layout':go.Layout(title='Pierwszy wykres',
                                                         xaxis={'title':'moja_os'},
                                                        yaxis={'title':'druga_os'}
                                                        )})])

#if __name__=='__main__':
 #   app.run_server(host='0.0.0.0', port=8080)
