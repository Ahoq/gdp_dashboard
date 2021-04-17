# Dash app initialization
import dash
import os
from flask import Flask

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

server = Flask(__name__)


app = dash.Dash(
    server=server,
    external_stylesheets=external_stylesheets
)

app.title = "ADNAN HOQ"
application = app.server
app.config.suppress_callback_exceptions = True





