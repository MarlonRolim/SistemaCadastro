
from app import *



card_icon_succces = {
                    "color": "green",
                    "textAlign": "center",
                    "fontSize": 50,
                    "margin": 'auto',
                    'align-items':'center',
                    'display': 'flex',
                    'justify-content': 'center'
                }

# ================ Layout ================ #

def render_layout():
    
    template = html.Div(dbc.Row([dbc.Col([
                        dcc.Location(id='local_deslogando'),
                        html.Legend(fr'Deslogando...', style={'text-align':'center','display': 'flex', 'justify-content': 'center'}),
                        #html.Br(),
                        #html.Div(className="fa fa-check-circle", style=card_icon_succces),
                        dcc.Interval(interval=3000,id='interval_deslogando')
                        ])
                    ]), style={'widht':'100%', 'height': '100vh','background-color':'white', 'padding-left': '10px', 'padding-right': '10px','display': 'flex', 'justify-content': 'center','align-items':'center'})
    return template

# ================ Callbacks ================ #

@app.callback(
    Output('local_deslogando', 'pathname'),
    Input('interval_deslogando', 'n_intervals')
)
def voltar_homepage(interval):
    if interval == 1:
        if current_user.is_authenticated:
            logout_user()
            return '/app/login'
        else: 
            return '/app/login'
    