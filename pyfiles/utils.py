import dash_html_components as html
import dash_core_components as dcc



themes={
    'theme2': {'button_color':'#ffffff','header':'#000000', 'background':'#ffffff', 'tbl_header':'#c7c6c1',
    'grid_color':'#e8edea','plot_header':'#000000', 'tbl_background':'#ffffff', 'plot_ticks':'#000000', 'login_out_color':'#000000'},
    
    'theme1': {'button_color':'#004E65','header':'#E2EFFA', 'background':'#027788', 'tbl_header':'#013044',
    'grid_color':'#038699','plot_header':'#E2EFFA', 'tbl_background':'#004E65', 'plot_ticks':'#E2EFFA', 'login_out_color':'#E2EFFA'}
}


def get_footer():
    footer = html.Div([
            html.Div([
                html.H3("© Adnan", style = {'position': 'relative', 'float': 'right', 'margin-top':'10px'})
            ]),

        ], className = 'banner3')
    
    return footer