import dash_html_components as html
import dash_core_components as dcc



themes={
    'theme1': {
    'header':'#333','plot_title':'#333','axis_title':'#000000', 'grid_color':'#e8edea', 'plot_ticks':'#000000',
    'background':'#ffffff','legend': '#000000'
    }
}


def get_footer():
    footer = html.Div([
            html.Div([
                html.H5("© Adnan Hoq", style = {'position': 'relative', 'float': 'right', 'margin-top':'0px','margin-bottom':'0px'})
            ]),

        ], className = 'banner3')
    
    return footer