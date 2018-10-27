from flask import Flask
from dash import Dash

server = Flask(__name__, root_path='/myproject')
app = Dash(server=server)
app.config['suppress_callback_exceptions']=True
