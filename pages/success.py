from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import *

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash_bootstrap_templates import load_figure_template

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user
from dash.exceptions import PreventUpdate


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
                        dcc.Location(id='local_sucesso'),
                        html.Legend(fr'Sucesso!', style={'text-align':'center','display': 'flex', 'justify-content': 'center'}),
                        html.Br(),
                        html.Div(className="fa fa-check-circle", style=card_icon_succces),
                        dcc.Interval(interval=3000,id='interval_sucesso')
                        ])
                    ]), style={'widht':'100%', 'height': '100vh','background-color':'white', 'padding-left': '10px', 'padding-right': '10px','display': 'flex', 'justify-content': 'center','align-items':'center'})
    return template

# ================ Callbacks ================ #

@app.callback(
    Output('local_sucesso', 'pathname'),
    Input('interval_sucesso', 'n_intervals')
)
def voltar_homepage(interval):
    if interval == 1:
        return '/homepage'
    