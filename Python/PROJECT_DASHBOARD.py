import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

import home_tab
import data_tab
import bediening_tab


''' PROJECT DASHBOARD
'''


# __name__ uses css in assets/
app = dash.Dash(__name__)

# layout
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
                    value='home_tab',
                    children=[
                        home_tab.layout
                ]),

                dcc.Tab(
                    label='Data',
                    value='data_tab',
                    children=[
                        data_tab.layout
                    ]
                ),

                dcc.Tab(
                    label='Bediening',
                    value='bediening_tab',
                    children=[
                        bediening_tab.layout
                    ]
                ),

                dcc.Tab(
                    label='Instellingen',
                    value='instellingen_tab',
                    children=[
                        #instellingen_tab.layout aanmaken
                    ]
                )

            ]
            , value='home_tab'
        )

    ])

], style={'width':'100%','background-color':'#e5e8e6','height':'100%','min-height':'1024px'})

if __name__ == '__main__':
    app.run_server(debug=True)
