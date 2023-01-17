from dash import html, dcc
from dash.dependencies import Input, Output, State, ALL
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
import json
from pages.styles import *


# ================ Layout ================ #

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
    user = cadastro['name']
    status = cadastro['status_cad']
    card_right['height'] = '135px'
    card_icon['color'] = 'white'
    card_right["maxWidth"]= 30
    card_right['width']=25
    card_group_css['height'] = '135px'
    template = html.Div(dbc.CardGroup([
                    dbc.Card([
                                html.Legend(nome, style={'margin-bottom':'0', 'color':'#14a583', 'font-weight':'bold','font-size':'16px'}),
                                dbc.Row([
                                    dbc.Col([
                                        dbc.Label(fr'CNPJ: {cnpj}', style={'margin':'0','padding':'0','font-size':'12px'}),
                                        html.Br(),
                                        dbc.Label(fr'CPF: {cpf}', style={'margin':'0','padding':'0','font-size':'12px'}),
                                         html.Br(),
                                        dbc.Label(fr'I.E.: {ie}', style={'margin':'0','padding':'0','font-size':'12px'}),
                                        html.Br(),
                                        dbc.Label(fr'SOLICITANTE: {user}', style={'margin':'0','padding':'0','font-size':'12px'}),
                                    ],width=7),
                                    dbc.Col([
                                        html.Br(),
                                        html.Legend('Status', style={'text-align':'center', 'margin-bottom':'0','font-size':'18px'}),
                                        html.Legend(status, style={'color': corStatus(status),'font-weight':'bold', 'text-align':'center','font-size':'14px'})
                                    ],width=5)
                                ]),
                    ], style={"padding-left": "10px", "padding-top": "5px", 'height':'135px', 'width':'95%'}),
                    dbc.Card(dbc.Button(html.Div(className="fa fa-angle-right", style=card_icon),id={'type': 'pendencias_cadastro', 'index': id}, href=fr'/cadpendaprovacao/aprovarcadastro/{id}', color='link', style=card_icon),
                        color="success",
                        style=card_right,
                    )
                ],style=card_group_css),id=fr"{nome}-{id}",style={'margin-bottom': '10px'})
  

    return template

def preencher_Cadastros(nomes):
    x = []
    for i in nomes: 
               
        x.append(card_cadastro(nomes[i]))
            
    return html.Div(x)

def render_layout():
    df = pd.read_sql(fr"select c.*, u.name from cadastros c left join users u on c.usuario=u.id where c.status_cad <> 'Completo'", create_connection())
    cadastros = df.to_dict('index')
    if len(df) == 0:
        pendencias = html.Legend('Não há Cadastros Pendentes',style={'text-align': 'center'})
    else:
        pendencias = preencher_Cadastros(cadastros)
    template = html.Div([
                            dcc.Location(id='data-url-aprova'),
                            html.Br(),
                            html.Legend('Cadastros Pendentes', style={'text-align':'center','font-size':'28px', 'color':'#14a583'}),
                            html.Hr(),
                            pendencias,
                            html.Div(id='testeids'),
                            html.Br(),
                            html.Hr()
                        ], style={'widht':'100%', 'min-height':'100vh','height': '100%', 'background-color':'white', 'padding-left': '10px', 'padding-right': '10px'})
    return template

# ================ Callbacks ================ #
'''
@app.callback(
    Output('modal-sm','is_open'),
    Output('pendencias_modal','children'),
    Output('btns_footer','children'),
    Input({'type': 'pendencias_cadastro', 'index': ALL}, 'n_clicks'),
    State('modal-sm', 'is_open')
)
def abrir_modal_pendencias(n_click,is_open):
    if n_click == None:
        raise PreventUpdate
    if n_click:
        ctx = dash.callback_context
        trigg_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if trigg_id == None or trigg_id == '':
            return is_open,"",""
        else:
            trigg_id_dict = json.loads(trigg_id)
            id_cadastro = trigg_id_dict['index']
            df = pd.read_sql(fr"select * from pendencias where id_cadastro = '{id_cadastro}'", create_connection())
            btns = dbc.Row([
                                dbc.Col(dbc.Button("Visualizar",href=fr'/cadastrospendentes/visualizar/{id_cadastro}', style={'width':'100%'}), width=6),
                                dbc.Col(dbc.Button("Editar",href=f'/cadastrospendentes/alteracadastro/{id_cadastro}', style={'width':'100%'}), width=6),
                            ],style={'width':'100%','padding':'0', 'margin':'0'})
                    
            if len(df) == 0:
                
                return not is_open, "Aguardando Aprovação", btns
            else:
                dic = df.to_dict('index')
                lista = []
                for i in dic: 
                    lista.append(html.Label(dic[i]['observacao'],style={'color':'red'}))
                return not is_open, lista, btns
    return is_open, "", ""
'''