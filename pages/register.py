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
            dbc.Card([
                html.Legend('Cadastre-se',style={'text-align': 'center'}),
                dbc.Input(id='name_register', placeholder="Nome e Sobrenome", type='text'),
                dbc.Input(id='user_register', placeholder="Usuário", type='text'),
                dbc.Input(id='pwd_register', placeholder="Senha", type='password'),
                dbc.Input(id='email_register', placeholder="E-mail", type='email'),
                dbc.Button('Cadastrar', id='register_button'),
                html.Span(message, style={'text-align': 'center','margin-top': '5px', 'color': 'red'}),
                html.Div([
                    html.Label("Ou", style={'margin-right': '5px'}),
                    dcc.Link("Faça Login", href='/login'),
                    
                    ], style={'padding': '20px', 'justify-content': 'center', 'display': 'flex'}),
        
    ], style=card_style)
],style={'height': '100vh', 'display': 'flex', 'justify-content': 'center'})
    return registro

@app.callback(
    Output('register-state', 'data'),
    Input('register_button', 'n_clicks'),
    [
        State('name_register', 'value'),
        State('user_register', 'value'),
        State('pwd_register', 'value'),
        State('email_register', 'value')     
    ]
)
def register(n_clicks,name,usuario,senha,email):
    if n_clicks == None:
        raise PreventUpdate

    if usuario is not None and senha is not None and email is not None:
        hashed_password = generate_password_hash(senha, method='sha256')
        ins = Users_tbl.insert().values(name=name,username=usuario,password=hashed_password,email=email)
        conn = engine.connect()
        conn.execute(ins)
        conn.close()
        return ''
    else:
        return 'error'