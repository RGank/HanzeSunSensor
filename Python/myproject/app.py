from .server import app, server
from . import callbacks_home
from . import callbacks_data
from . import callbacks_bediening
from .layout import home
from .layout import bediening
from .layout import data

import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

import random
import time
import datetime

app.layout = html.Div([


    html.Div([

        html.H1('DSIO Dashboard', style={'color':'#FFFFFF', 'margin-left':'10px'})

    ], style={'background-color': '#1f618d ', 'overflow':'hidden'}),

    html.Div([

        dcc.Tabs(
            id='tabs',
            children=[

                dcc.Tab(
                    label='Home',
                    value='home_tab'
                    ),

                dcc.Tab(
                    label='Data',
                    value='data_tab',
                ),

                dcc.Tab(
                    label='Bediening',
                    value='bediening_tab',
                ),

                dcc.Tab(
                    label='Instellingen',
                    value='instellingen_tab',
                )

            ]
            , value='home_tab'
        )

    ]),

    html.Div(id='tab_content'),

    html.Div(id='hidden_temp', style={'display':'none'}),
    dcc.Interval(id='hidden_temp_interval', interval=1*5000, n_intervals=0),

    html.Div(id='hidden_light', style={'display':'none'}),
    dcc.Interval(id='hidden_light_interval', interval=1*5000, n_intervals=0),

    html.Div(id='hidden_time', style={'display':'none'}),
    dcc.Interval(id='hidden_time_interval', interval=1*1000, n_intervals=0),

    html.Div(id='hidden_date', style={'display':'none'}),
    dcc.Interval(id='hidden_date_interval', interval=1*5000, n_intervals=0)


], style={'width':'100%','background-color':'#e5e8e6','height':'100%','min-height':'1024px'})

@app.callback(Output("tab_content", "children"), [Input("tabs", "value")])
def render_content(tab):
    if tab == "home_tab":
        return home.layout
    elif tab == "data_tab":
        return data.layout
    elif tab == "bediening_tab":
        return bediening.layout
    else:
        return 'must still be done :D'

# update temperature
@app.callback(
    Output('hidden_temp', 'children'),
    [Input('hidden_temp_interval', 'n_intervals')]
)
def update_temp(n):
    temp = round(random.randint(0, 3000)/100, 1)
    return '{}°C.'.format(temp)

# update light
@app.callback(
    Output('hidden_light', 'children'),
    [Input('hidden_light_interval', 'n_intervals')]
)
def update_light(n):
    light = round(random.randint(0, 200))
    return light

# update time
@app.callback(
    Output('hidden_time', 'children'),
    [Input('hidden_time_interval', 'n_intervals')]
)
def update_time(n):
    current = time.strftime('%H:%M:%S')
    return current

# update date
@app.callback(
    Output('hidden_date', 'children'),
    [Input('hidden_date_interval', 'n_intervals')]
)
def update_date(n):
    current_date = datetime.datetime.now().strftime('%d/%m/%y')
    return current_date
