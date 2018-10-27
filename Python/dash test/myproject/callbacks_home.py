from .server import app
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import time
import pandas as pd

import random
from collections import deque

# show the temperatuur
@app.callback(
    Output('temperatuur_home', 'children'),
    [Input('hidden_temp', 'children')]
)
def show_temp(n):
    return n

# show the light intensity
@app.callback(
    Output('lichtintensiteit_home', 'children'),
    [Input('hidden_light', 'children')]
)
def show_temp(n):
    return n

# show the time
@app.callback(
    Output('tijd_home', 'children'),
    [Input('hidden_time', 'children')]
)
def show_time(n):
    return n

# show the date
@app.callback(
    Output('datum_home', 'children'),
    [Input('hidden_date', 'children')]
)
def show_date(n):
    return n
