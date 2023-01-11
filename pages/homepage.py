from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import *

import numpy as np
import pandas as pd
import plotly.express as pxs
import plotly.graph_objects as go
from dash_bootstrap_templates import load_figure_template

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user
from dash.exceptions import PreventUpdate

from pages.styles import *

load_figure_template(["quartz"])

# =========  Layout  =========== #
def render_layout(name):
    df = pd.read_sql(fr"select * from cadastros where usuario = '{current_user.username}'", create_connection())
    df['data_cad'] = pd.to_datetime(df['data_cad'],  yearfirst = True)
    inicio, fim = data_mesAtual()
    card_right["maxWidth"]= 15
    card_right['width']=15
    card_right['height'] = '100px'
    template = html.Div([
                            dcc.Location(id='data-url'),
                            
                            html.Br(),
                            dbc.Row([
                                dbc.Col([html.Legend(fr'Bem Vindo, {name}.', style={ 'padding-top':'10px', 'font-size': '18px'})],width=10),
                                
                            ]),
                            html.Hr(),
                            dbc.Button("Novo Cadastro",href='/cadastro', style={'width': '100%'}),
                            html.Hr(),
                            html.Legend("Indicadores",style={'text-align':'center'}),
                            dbc.CardGroup([
                                dbc.Card([html.A([
                                        html.Legend("Cadastros Pendentes"),
                                        html.H5(len(df[df['status_cad']=='Pendente']), id="qtd-cad-pendentes", style={})], href='/cadastrospendentes', style={'text-decoration': 'none', 'color': 'grey'}),
                                ], style={"padding-left": "15px", "padding-top": "5px", 'height':100, 'width':'98%'}),
                                dbc.Card(
                                    color="warning",
                                    style=card_right,
                                )
                            ],style=card_group_css),
                            
                            dbc.CardGroup([
                                dbc.Card([
                                        html.Legend("Cadastros Mês"),
                                        html.H5(len(df[(df['data_cad'] >= inicio) & (df['data_cad'] <= fim)]), id="qtd-cad-pendentes", style={}),
                                ], style={"padding-left": "15px", "padding-top": "5px", 'height':100, 'width':'98%'}),
                                dbc.Card(
                                    color="success",
                                    style=card_right,
                                )
                            ],style=card_group_css),
                            
                            dbc.CardGroup([
                                dbc.Card([
                                        html.Legend("Cadastros Total"),
                                        html.H5(len(df), id="qtd-cad-pendentes", style={}),
                                ], style={"padding-left": "15px", "padding-top": "5px", 'height':100, 'width':'98%'}),
                                dbc.Card(
                                    color="#23a6d5",
                                    style=card_right,
                                )
                            ],style=card_group_css),
                            
                            
        
        ], style={'widht':'100%', 'height': '100vh', 'background-color':'white', 'padding-left': '10px', 'padding-right': '10px'})
    return template 


# =========  Callbacks Page1  =========== #


