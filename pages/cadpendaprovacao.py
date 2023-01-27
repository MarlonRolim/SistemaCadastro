
from app import *

from pages.styles import *


# ================ Layout ================ #

def corStatus(status):
    if status == 'Completo': return '#14a583'
    elif status == 'Pendente': return 'orange'
    else: return 'red'


def card_cadastro(cadastro):
    id = cadastro['id']
    nome = cadastro['razao']
    cod = cadastro['cod_fornecedor']
    loja = cadastro['cod_loja']
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
                                html.Legend(fr"{cod}/{loja} - {nome}", style={'margin-bottom':'0', 'color':'#14a583', 'font-weight':'bold','font-size':'14px','overflow': 'hidden', 'text-overflow': 'ellipsis','white-space': 'nowrap'}),
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
                    dbc.Card(dbc.Button(html.Div(className="fa fa-angle-right", style=card_icon),id={'type': 'pendencias_cadastro', 'index': id}, href=fr'/app/cadpendaprovacao/aprovarcadastro/{id}', color='link', style=card_icon),
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
