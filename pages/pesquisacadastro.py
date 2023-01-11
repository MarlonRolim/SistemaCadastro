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

from pages.styles import *


# ================ Layout ================ #


def preencher_Cadastros(nomes):
    x = []
    for i in nomes: x.append(card_cadastro(nomes[i]))
    return html.Div(x)

def corStatus(status):
    if status == 'Completo': return '#14a583'
    elif status == 'Pendente': return 'orange'
    else: return 'red'

def card_cadastro(cadastro):
    id = cadastro['id']
    nome = cadastro['razao']
    cnpj = cadastro['cnpj']
    cpf = cadastro['cpf']
    ie = cadastro['ie']
    status = cadastro['status_cad']
    card_right['height'] = '110px'
    card_icon['color'] = 'white'
    card_right["maxWidth"]= 30
    card_right['width']=25
    card_group_css['height'] = '110px'
    
    template = html.Div(dbc.CardGroup([
                    dbc.Card([
                                html.Legend(nome, style={'margin-bottom':'0', 'color':'#14a583', 'font-weight':'bold','font-size':'18px'}),
                                dbc.Row([
                                    dbc.Col([
                                        dbc.Label(fr'CNPJ: {cnpj}', style={'margin':'0','padding':'0','font-size':'12px'}),
                                        html.Br(),
                                        dbc.Label(fr'CPF: {cpf}', style={'margin':'0','padding':'0','font-size':'12px'}),
                                         html.Br(),
                                        dbc.Label(fr'I.E.: {ie}', style={'margin':'0','padding':'0','font-size':'12px'}),
                                    ],width=7),
                                    dbc.Col([
                                        html.Legend('Status', style={'text-align':'center', 'margin-bottom':'0','font-size':'18px'}),
                                        html.Legend(status, style={'color': corStatus(status),'font-weight':'bold', 'text-align':'center','font-size':'14px'})
                                    ],width=5)
                                ])
                                ], style={"padding-left": "10px", "padding-top": "5px", 'height':'110px', 'width':'95%'}),
                    dbc.Card(dbc.Button(html.Div(className="fa fa-angle-right", style=card_icon),id='btn-altera', href=fr'/pesquisacadastro/visualizar/{id}', color='link', style=card_icon),
                        color="success",
                        style=card_right,
                    )
                ],style=card_group_css),style={'margin-bottom': '10px'})
  

    return template


def render_layout():
    card_icon['color'] = 'white'
    card_icon['fontSize'] = 20
    template = html.Div([
                            html.Br(),
                            html.Legend('Pesquisa de Cadastros', style={'text-align':'center', 'font-size':'28px', 'color':'#14a583'}),
                            html.Hr(),
                            dbc.Select(id='select_pesquisa', 
                                        options=[{'label': 'Nome / Razão Social', 'value': 'razao'},{'label': 'CNPJ', 'value': 'CNPJ'},{'label': 'CPF', 'value': 'cpf'},{'label': 'Inscrição Estadual', 'value': 'ie'}],
                                        value='razao',
                                        style={'height':'38px'}
                                    ),
                            dbc.Row([
                                
                                dbc.Col([dbc.Input(id='input_pesquisa',placeholder="pesquisa", type='text'),],width=10, style={'padding': 0, 'padding-right':'5px'}),
                                
                                dbc.Col([dbc.Button(html.Div(className="fa fa-search", style=card_icon),id='btn_pesquisa', style={'width':'100%'})],width=2, style={'padding': 0})
                            ],style={'padding-left': '10px', 'padding-right': '10px', 'margin-top':'10px'}),
                            
                            html.Legend('Resultados', style={'text-align':'center','font-size':'20px', 'color':'#14a583'}),
                            html.Hr(),
                            html.Div(id='result_pesquisa',style={'width':'100%', 'padding': 0, 'margin': 0})
                        ], style={'widht':'900px', 'height': '100vh', 'background-color':'white', 'padding-left': '10px', 'padding-right': '10px'})
    return template

# ================ Callbacks ================ #

@app.callback(
    Output('result_pesquisa', 'children'),
    Input('btn_pesquisa','n_clicks'),
    State('select_pesquisa','value'),
    State('input_pesquisa','value')
)
def pesquisa(n_clicks,select,texto):
    if n_clicks:
        #pesquisa = ''
        if select == 'CNPJ':
            pesquisa = 'cnpj'
        
        elif select == 'cpf':
            pesquisa = 'cpf'
        
        elif select == 'razao':
            pesquisa = 'razao'
        
        elif select == 'ie':
            pesquisa = 'ie'
        
        if texto == None:
            texto = ''
        
        df = pd.read_sql(fr"select * from cadastros where '{pesquisa}' like '{str(texto)}%'", create_connection())
        dic = df.to_dict('index')
        
        
        return preencher_Cadastros(dic)
        
        