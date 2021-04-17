import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.graph_objects as go
from app import app
from pyfiles.utils import themes, get_footer
import os


dd = pd.read_csv('gdp_csv.csv')



layout = html.Div([
    html.Div([
        html.Div(
            [
                # html.Img(
                #     src=("/assets/orig.jpg"),
                #     className="logo",
                # ),
                html.H5("GDP Dashboard")
                
            ],
            className="two columns main-title",
            ),
    ], className='row'),
    
    html.Br(),
    html.Div([
            html.Div([
                html.Div([
                    html.H5("Country:", style = {'color':themes['theme1']['header']}),
                    dcc.Dropdown(
                        id='key-picker',
                        options = [{'label': x, 'value': x} for x in dd['Country Name'].unique()],
                        value=['United States','China', 'Germany', 'Japan'],
                        multi = True
                    )
                ],className = 'multi')
            ], className = 'mini_container')
    

    ]),
    html.Div([
                html.Div([
                    html.H4("GDP Over Time", style = {'text-align' : 'center', 'color':themes['theme1']['header']}),
                    dcc.Graph(
                            id='graph_dd',
                            config = {
                                'toImageButtonOptions': {
                                    'format': 'png',
                                    'height': 800,
                                    'width': 1200,
                                    'scale': 1
                                }
                            }
                    )
                ], className = 'pretty_container'),

    ], style = {'margin-bottom': '0px'}),
    
    get_footer()
  
],className='ten columns offset-by-one')


@app.callback(
    Output('graph_dd', 'figure'),
    [Input('key-picker', 'value'), 
     ])
     
def update_dd(selected_key):
    ndd = dd.sort_values(by = 'Year', ascending = True)
    
    traces = []
    for i in selected_key:
        dd_by_key = ndd.loc[ndd['Country Name'] == i]

        df2=dd_by_key.pivot(index='Year', columns='Country Name', values='Value')

    

        traces.append(go.Scatter(
                x=dd_by_key['Year'],
                y=dd_by_key['Value'],
                text=dd_by_key['Country Name'],
                hovertemplate= "Country: %{text}<br>Year: %{x}<br>GDP: %{y}",
                name="%s's GDP"%i,
                opacity=0.8,
                mode='lines+markers'
                )
            )
        

    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'title': None,'titlefont':{'color':'#858585'},'linecolor':'#000000',
                   'tickfont':{'color':'#858585','size':18},'showgrid':False,'showline':False},

            yaxis={'title': 'GDP','titlefont':{'color':'#858585','size':20}, 'tickfont':{'color':'#858585','size':18},
                   'showgrid':False},
            margin={'l': 80, 'b': 40, 't': 30, 'r': 40},
            template = 'none',
            hovermode='closest',
            showlegend =  True
        )
    }



