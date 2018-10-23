import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

''' PROJECT DASHBOARD
'''

df = pd.read_csv('gem_temp.csv', delimiter=';')

def generate_table(dataframe, max_rows=5):
    return html.Table(
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    , style={'text-align':'center'})


app = dash.Dash(__name__)

# layout
app.layout = html.Div([

    # create a header
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
                        # row 1
                        html.Div([
                            html.Div([

                                html.H1('Welkom, dit is uw Dashboard')

                            ],
                            style={'background-color':'#FFFFFF', 'height':'100px', 'width':'99.3%', 'border':'0.1vw solid #C8D4E3', 'margin':'0.25%', 'text-align':'center'}
                            )


                        ]),
                        #row2
                        html.Div([
                            html.Div([

                                html.P('Uitleg')

                            ],
                            style={'background-color':'#FFFFFF', 'height':'600px', 'width':'49.3%', 'float':'left', 'border':'0.1vw solid #C8D4E3', 'margin':'0.25%', 'text-align':'center'}
                            ),

                            html.Div([

                                html.P('Temperatuur'),

                                dcc.Graph(

                                    id='temperatuur_grafiek_home'

                                )

                            ],
                            style={'background-color':'#FFFFFF', 'height':'600px', 'width':'49.3%', 'float':'left', 'border':'0.1vw solid #C8D4E3', 'margin':'0.25%', 'text-align':'center'}
                            )

                        ]),
                        #row3
                        html.Div([

                            html.Div([

                                html.P('Huidige temperatuur'),

                                html.Span('16°C.', id='temperatuur_home', style={'font-size': '24px', 'position':'relative', 'top':'25%'})

                            ],
                            style={'float':'left', 'width':'24.33%','height':'250px', 'margin':'0.25%', 'background-color':'#FFFFFF', 'border':'0.1vw solid #C8D4E3', 'text-align':'center'}
                            ),

                            html.Div([

                                html.P('Huidige lichtintensiteit'),

                                html.Span('135cd', id='lichtintensiteit_home', style={'font-size': '24px', 'position':'relative', 'top':'25%'})

                            ],
                            style={'float':'left', 'width':'24.3%', 'height':'250px', 'margin':'0.25%', 'background-color':'#FFFFFF','border':'0.1vw solid #C8D4E3', 'text-align':'center'}
                            ),

                            html.Div([

                                html.P('Huidige tijd'),

                                html.Span('17:30', id='tijd_home', style={'font-size': '24px', 'position':'relative', 'top':'25%'})

                            ],
                            style={'float':'left', 'width':'24.3%', 'height':'250px', 'margin':'0.25%', 'background-color':'#FFFFFF','border':'0.1vw solid #C8D4E3', 'text-align':'center'}
                            ),

                            html.Div([

                                html.P('Huidige datum'),

                                html.Span('31 Oktober', id='datum_home', style={'font-size': '24px', 'position':'relative', 'top':'25%'})

                            ],
                            style={'float':'left', 'width':'24.3%', 'height':'250px', 'margin':'0.25%', 'background-color':'#FFFFFF','border':'0.1vw solid #C8D4E3', 'text-align':'center'}
                            )

                        ],
                        style={'display': 'table', 'width':'100%'}
                        )
                ]),

                dcc.Tab(
                    label='Data',
                    value='data_tab',
                    children=[
                        # row 1
                        html.Div([
                            html.Div([

                                html.P('Huidige temperatuur'),

                                html.Span('16°C.', id='temperatuur_data', style={'font-size': '24px', 'position':'relative', 'top':'25%'})

                            ],
                            style={'background-color':'#FFFFFF', 'height':'200px', 'width':'32.65%', 'float':'left', 'border':'0.1vw solid #C8D4E3', 'margin':'0.25%', 'text-align':'center'}
                            ),

                            html.Div([

                                html.P('Huidige lichtintensiteit'),

                                html.Span('135cd', id='lichtintensiteit_data', style={'font-size': '24px', 'position':'relative', 'top':'25%'})

                            ],
                            style={'background-color':'#FFFFFF', 'height':'200px', 'width':'32.65%', 'float':'left','border':'0.1vw solid #C8D4E3', 'margin':'0.25%', 'text-align':'center'}
                            ),

                            html.Div([

                                html.P('Huidige status'),

                                html.Span('aangesloten', id='status_data', style={'font-size': '24px', 'position':'relative', 'top':'25%'})

                            ],
                            style={'background-color':'#FFFFFF', 'height':'200px', 'width':'32.65%', 'float':'left','border':'0.1vw solid #C8D4E3', 'margin':'0.25%', 'text-align':'center'}
                            )

                        ],
                        style={'display': 'table', 'width':'100%', 'margin-top':'10px'}
                        ),
                        # row 2
                        html.Div([
                            html.Div([

                                html.P('Temperatuur', style={'font-size':'24px'}),

                                dcc.Graph(
                                    id='temperatuur_grafiek'
                                )

                            ],
                            style={'background-color':'#FFFFFF', 'height':'600px', 'width':'49.3%', 'float':'left', 'border':'0.1vw solid #C8D4E3', 'margin':'0.25%', 'text-align':'center'}
                            ),

                            html.Div([

                                html.P('Lichtintensiteit', style={'font-size':'24px'}),

                                dcc.Graph(
                                    id='lichtintensiteit_grafiek'
                                )

                            ],
                            style={'background-color':'#FFFFFF', 'height':'600px', 'width':'49.3%', 'float':'left', 'border':'0.1vw solid #C8D4E3', 'margin':'0.25%', 'text-align':'center'}
                            )
                        ]
                        ),
                        # row 3
                        html.Div([
                            html.Div([

                                html.P('Gemiddelde temperatuur'),

                                generate_table(df)

                            ],
                            style={'background-color':'#FFFFFF', 'height':'400px', 'width':'49.3%', 'float':'left', 'border':'0.1vw solid #C8D4E3', 'margin':'0.25%', 'text-align':'center'}
                            ),

                            html.Div([

                                html.P('Gemiddelde lichtintensiteit'),

                                generate_table(df)

                            ],
                            style={'background-color':'#FFFFFF', 'height':'400px', 'width':'49.3%', 'float':'left', 'border':'0.1vw solid #C8D4E3', 'margin':'0.25%',  'text-align':'center'}
                            )
                        ]
                        )

                    ]
                ),

                dcc.Tab(
                    label='Bediening',
                    value='bediening_tab',
                    children=[
                        html.Div([
                            html.Div([

                                html.P('Handmatig', style={'font-size':'24px'}),

                                html.Div([
                                    # when button is pressed children changes to 'UIT', also need counter variable
                                    html.Button(
                                        children='AAN',
                                        id='bediening_knop_1'
                                    )

                                ]),

                                html.Div([

                                    html.P(children='Geef het gewenste uitrol bereik aan:'),

                                    dcc.RangeSlider(

                                        id='uitrol_bereik_handmatig',
                                        min=0,
                                        max=160,
                                        value=[10, 160],
                                        marks={
                                            0: {'label': '0cm'},
                                            20: {'label': '20cm'},
                                            40: {'label': '40cm'},
                                            60: {'label': '60cm'},
                                            80: {'label': '80cm'},
                                            100: {'label': '100cm'},
                                            120: {'label': '120cm'},
                                            140: {'label': '140cm'},
                                            160: {'label': '160cm'}
                                        },
                                        allowCross=False,
                                    )
                                ],
                                style={'width':'50%', 'margin':'0 auto', 'padding-top':'50px'}
                                )

                            ],
                            style={'background-color': '#FFFFFF',
                                'border':'0.1vw solid #C8D4E3','height': '500px','width':'49.3%',
                                'margin':'0.25%','text-align':'center', 'float':'left', 'padding-top':'10px'}
                            ),

                            html.Div([

                                html.P('Autonoom', style={'font-size':'24px'}),

                                html.Div([
                                    # when button is pressed change 'UIT' to 'AAN' and vice versa. Need counter variable
                                    html.Button(
                                        children='UIT',
                                        id='bediening_knop_2'
                                    )

                                ]),

                                html.Div([

                                    html.P(children='Geef het gewenste temperatuur bereik aan:'),

                                    dcc.RangeSlider(

                                        id='temperatuur_bereik_autonoom',
                                        min=-30,
                                        max=40,
                                        value=[10, 35],
                                        marks={
                                            -30: {'label': '-30°C', 'style': {'color': '#9EE4D9'}},
                                            -20: {'label': '-20°C'},
                                            -10: {'label': '-10°C'},
                                            0: {'label': '0°C', 'style': {'color':'#A5F2F3'}},
                                            10: {'label': '10°C'},
                                            20: {'label': '20°C'},
                                            30: {'label': '30°C'},
                                            40: {'label': '40°C', 'style': {'color':'#FF0000'}}
                                        },
                                        allowCross=False,
                                    )
                                ],
                                style={'width':'50%', 'margin':'0 auto', 'padding-top':'50px'}
                                ),

                                html.Div([

                                    html.P(children='Geef het gewenste uitrol bereik aan:'),

                                    dcc.RangeSlider(

                                        id='uitrol_bereik_autonoom',
                                        min=0,
                                        max=160,
                                        value=[10, 160],
                                        marks={
                                            0: {'label': '0cm'},
                                            20: {'label': '20cm'},
                                            40: {'label': '40cm'},
                                            60: {'label': '60cm'},
                                            80: {'label': '80cm'},
                                            100: {'label': '100cm'},
                                            120: {'label': '120cm'},
                                            140: {'label': '140cm'},
                                            160: {'label': '160cm'}
                                        },
                                        allowCross=False,
                                    )
                                ],
                                style={'width':'50%', 'margin':'0 auto', 'padding-top':'50px'}
                                )
                            ],
                            style={'background-color': '#FFFFFF',
                                'border':'0.1vw solid #C8D4E3', 'height': '500px','width':'49.3%',
                                'margin': '0.25%', 'text-align':'center', 'float':'left', 'padding-top':'10px'}
                            )
                        ],
                        style={'display': 'table', 'margin-top': '10px',  'width':'100%'}
                        ),
                        #'''BEWERKEN, v.l.n.r. huidige temperatuur, huidige lichtintensiteit, huidige tijd, huidige datum'''
                        html.Div([

                            html.Div([

                                html.P('Huidige temperatuur'),

                                html.Span('16°C.', id='temperatuur_bediening', style={'font-size': '24px', 'position':'relative', 'top':'25%'})

                            ],
                            style={'float':'left', 'width':'24.33%','height':'250px', 'margin':'0.25%', 'background-color':'#FFFFFF', 'border':'0.1vw solid #C8D4E3', 'text-align':'center'}
                            ),

                            html.Div([

                                html.P('Huidige lichtintensiteit'),

                                html.Span('135cd', id='lichtintensiteit_bediening', style={'font-size': '24px', 'position':'relative', 'top':'25%'})

                            ],
                            style={'float':'left', 'width':'24.3%', 'height':'250px', 'margin':'0.25%', 'background-color':'#FFFFFF','border':'0.1vw solid #C8D4E3', 'text-align':'center'}
                            ),

                            html.Div([

                                html.P('Huidige tijd'),

                                html.Span('17:30', id='tijd_bediening', style={'font-size': '24px', 'position':'relative', 'top':'25%'})

                            ],
                            style={'float':'left', 'width':'24.3%', 'height':'250px', 'margin':'0.25%', 'background-color':'#FFFFFF','border':'0.1vw solid #C8D4E3', 'text-align':'center'}
                            ),

                            html.Div([

                                html.P('Huidige datum'),

                                html.Span('31 Oktober', id='datum_bediening', style={'font-size': '24px', 'position':'relative', 'top':'25%'})

                            ],
                            style={'float':'left', 'width':'24.3%', 'height':'250px', 'margin':'0.25%', 'background-color':'#FFFFFF','border':'0.1vw solid #C8D4E3', 'text-align':'center'}
                            )

                        ],
                        style={'display': 'table', 'width':'100%'}
                        )
                    ]
                ),

                dcc.Tab(
                    label='Instellingen',
                    value='instellingen_tab'
                )

            ]
            , value='home_tab'
        )

    ])

], style={'width':'100%','background-color':'#e5e8e6','height':'100%','min-height':'1024px'})

if __name__ == '__main__':
    app.run_server(debug=True)
