import dash
import dash_core_components as dcc
import dash_html_components as html

import visuals

layout = html.Div([

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

])
