
from app import *


# =========  Layout  =========== #
def render_layout(name):
    
    card_right["maxWidth"]= 15
    card_right['width']=15
    card_right['height'] = '100px'
    template = html.Div([
                            dcc.Location(id='data-url'),
                            
                            html.Br(),
                            dbc.Row([
                                dbc.Col([html.Legend(fr'Bem Vindo, {name}.', id="atualiza_valores",style={ 'padding-top':'10px', 'font-size': '18px'})],width=10),
                                
                            ]),
                            html.Hr(),
                            dbc.Row([
                                dbc.Col([dbc.Button("Novo Cadastro",href='/app/cadastro', style={'width': '100%'}),],md=2,style={'margin-bottom':"10px","min-width":'170px'}),
                                dbc.Col([dbc.Button("Notificações",href='https://cadastrorb.onrender.com/notification', style={'width': '100%',}),],md=2, style={"min-width":'170px'} ),      
                            ]),
                            
                            
                            
                            
                            
                            html.Hr(),
                            html.Legend("Indicadores",style={'text-align':'center'}),
                            
                            
                            
                            dbc.Row([
                                dbc.Col([dbc.CardGroup([
                                dbc.Card([html.A([
                                        html.Legend("Cadastros Pendentes"),
                                        html.H5("Carregando...", id="qtd-cad-pendentes", style={})], href='/app/cadastrospendentes', style={'text-decoration': 'none', 'color': 'grey'}),
                                ], style={"padding-left": "15px", "padding-top": "5px", 'height':100, 'width':'98%'}),
                                dbc.Card(
                                    color="warning",
                                    style=card_right,
                                )
                            ],style=card_group_css),],md=4, style={"min-width":"328px"}),
                                
                                dbc.Col([dbc.CardGroup([
                                dbc.Card([
                                        html.Legend("Cadastros Mês"),
                                        html.H5("Carregando...", id="qtd-cad-mes", style={}),
                                ], style={"padding-left": "15px", "padding-top": "5px", 'height':100, 'width':'98%'}),
                                dbc.Card(
                                    color="success",
                                    style=card_right,
                                )
                            ],style=card_group_css),],md=4, style={"min-width":"328px"}),
                                
                                dbc.Col([dbc.CardGroup([
                                dbc.Card([
                                        html.Legend("Cadastros Total"),
                                        html.H5("Carregando...", id="qtd-cad-total", style={}),
                                ], style={"padding-left": "15px", "padding-top": "5px", 'height':100, 'width':'98%'}),
                                dbc.Card(
                                    color="#23a6d5",
                                    style=card_right,
                                )
                            ],style=card_group_css),],md=4, style={"min-width":"328px"}),
                            ])
                            
                            
                            
                            
                            
                            
                            
        
        ], style={'widht':'100%', 'min-height': '100vh', "height":"100%", 'background-color':'white', 'padding-left': '10px', 'padding-right': '10px'})
    return template 


# =========  Callbacks Page1  =========== #


@app.callback(
    [
        Output("qtd-cad-pendentes", "children"),
        Output("qtd-cad-mes", "children"),
        Output("qtd-cad-total", "children")
    ],
    Input("atualiza_valores", "children")
)
def atualiza_valor(input):
    if input:
        df = pd.read_sql(fr"select usuario,data_cad,status_cad from cadastros where usuario = '{current_user.id}'", create_connection())
        df['data_cad'] = pd.to_datetime(df['data_cad'],  yearfirst = True)
        inicio, fim = data_mesAtual()
        return len(df[df['status_cad']!='Completo']),len(df[(df['data_cad'] >= inicio) & (df['data_cad'] <= fim)]),len(df)