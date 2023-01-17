from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash
from dash.exceptions import PreventUpdate
import numpy as np
import pandas as pd
from app import *
from werkzeug.security import generate_password_hash




card_style= {
    'width': '300px',
    'min-height': '300px',
    'padding-top': '25px',
    'padding-right': '25px',
    'padding-left': '25px',
    'align-self': 'center',
    
    
}

def render_layout(message):
    
    message = "Ocorreu um erro durante o registro" if message == 'error' else message
    registro = html.Div([
                html.Br(),
                html.Br(),
                html.Legend('Cadastrar Novo Usuário',style={'text-align': 'center'}),
                dbc.Input(id='name_register', placeholder="Nome e Sobrenome", type='text'),
                dbc.Input(id='user_register', placeholder="Usuário", type='text'),
                dbc.Input(id='pwd_register', placeholder="Senha", type='password'),
                dbc.Input(id='email_register', placeholder="E-mail", type='email'),
                dbc.Select(id='select_typeuser', 
                                    options=[{'label': 'Admin', 'value': 1},{'label': 'Normal', 'value': 2}],
                                    value=2),
                html.Br(),
                dbc.Button('Cadastrar', id='register_button', style={'width': '100%'}),
                html.Span(message, style={'text-align': 'center','margin-top': '5px', 'color': 'red'}),
               
        
    
], style={'widht':'100%', 'min-height':'100vh','height': '100%', 'background-color':'white', 'padding-left': '10px', 'padding-right': '10px'})
    return registro

@app.callback(
    Output('register-state', 'data'),
    Input('register_button', 'n_clicks'),
    [
        State('name_register', 'value'),
        State('user_register', 'value'),
        State('pwd_register', 'value'),
        State('email_register', 'value'),
        State('select_typeuser', 'value')     
    ]
)
def register(n_clicks,name,usuario,senha,email,type):
    if n_clicks == None:
        raise PreventUpdate

    if usuario is not None and senha is not None and email is not None:
        hashed_password = generate_password_hash(senha, method='sha256')
        ins = Users_tbl.insert().values(name=name,username=usuario,password=hashed_password,email=email, user_type=type)
        conn = engine.connect()
        conn.execute(ins)
        conn.close()
        return ''
    else:
        return 'error'