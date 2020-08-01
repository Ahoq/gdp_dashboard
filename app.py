# Dash app initialization
import dash
import os
from flask import Flask


server = Flask(__name__)


app = dash.Dash(
    server=server
)

app.title = "ADNAN"
application = app.server
app.config.suppress_callback_exceptions = True





