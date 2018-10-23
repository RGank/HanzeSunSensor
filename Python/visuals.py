import dash
import dash_core_components as dcc
import dash_html_components as html

'''
def send_col_data(html, children):
    


'''

# Huidige temperatuur, huidige lichtintensiteit, huidige tijd, huidige datum
temp_licht_tijd_datum_4 = html.Div([

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
