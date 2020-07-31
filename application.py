import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app, application
from pyfiles import dd





app.layout = html.Div(
    [ 
        html.Div(
            html.Div(id='page-content')
        ),
        dcc.Location(id='url', refresh=False),
    ]
)

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return dd.layout
    else:
        return '404'




if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8080)