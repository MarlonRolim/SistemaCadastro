
from app import *


def corStatus(status):
    if status == 'Completo': return '#14a583'
    elif status == 'Pendente': return 'orange'
    else: return 'red'

def render_layout(id,pagina):
    df = pd.read_sql(fr"select * from cadastros where id = '{id}'", create_connection())
    
    df['data_cad'] = pd.to_datetime(df['data_cad']).dt.strftime(f'%d/%m/%Y')
    dic = df.to_dict('index')
    dic = dic[0]
    
    botao_voltar = dbc.Button('Voltar', href=fr'/app/{pagina}',style={'width':'100%','margin-bottom':'10px'})
    botao_alterar = dbc.Button("Editar",href=f'/app/{pagina}/alteracadastro/{id}', style={'width':'100%'})
    solicitante = pd.read_sql(fr"select * from users where id = '{dic['usuario']}'", create_connection())
    solicitante = solicitante.to_dict('index')
    solicitante = solicitante[0]['name']
    template = html.Div([
                    html.Br(),
                    botao_voltar,
                    html.Br(),
                    botao_alterar,
                    html.Hr(),
                    html.Legend('Status Cadastro: ', style={'text-align':'center','font-size':'24px', 'color':'#14a583'}),
                    html.Br(),
                    html.Legend(dic['status_cad'],style={'text-align':'center','font-size':'20px','color':corStatus(dic['status_cad'])}),
                    
                    html.Hr(),
                    
                    html.Legend('Informações', style={'text-align':'center', 'font-size':'28px', 'color':'#14a583'}),
                    
                    
                    dbc.Label('Data Cadastro: ', style={'font-size':'18px', 'color':'#14a583'}),
                    html.Br(),
                    dbc.Label(fr"{dic['data_cad']}"),
                    html.Br(),
                    
                    dbc.Label('Solicitante: ', style={'font-size':'18px', 'color':'#14a583'}),
                    html.Br(),
                    dbc.Label(solicitante),
                    html.Br(),
                    
                    
                    dbc.Row([
                        
                        dbc.Col([
                            dbc.Label('Cod. Fornecedor: ', style={'font-size':'18px', 'color':'#14a583'}),
                            html.Br(),
                            dbc.Label(dic['cod_fornecedor']),
                        ], width=6, style={'padding-right': '10px'}),
                        
                        dbc.Col([
                            dbc.Label('Cod. Loja: ', style={'font-size':'18px', 'color':'#14a583'}),
                            html.Br(),
                            dbc.Label(dic['cod_loja']),
                        ], width=6),
                        
                    ],style={'padding-top': '10px'}),
                    
                    dbc.Label('CNPJ: ', style={'font-size':'18px', 'color':'#14a583'}),
                    html.Br(),
                    dbc.Label(dic['cnpj']),
                    html.Br(),
                    
                    dbc.Label('CPF: ', style={'font-size':'18px', 'color':'#14a583'}),
                    html.Br(),
                    dbc.Label(dic['cpf']),
                    html.Br(),
                    
                    dbc.Label('I.E: ', style={'font-size':'18px', 'color':'#14a583'}),
                    html.Br(),
                    dbc.Label(dic['ie']),
                    html.Br(),
                    
                    dbc.Label('Razão Social: ', style={'font-size':'18px', 'color':'#14a583'}),
                    html.Br(),
                    dbc.Label(dic['razao']),
                    html.Br(),
                    
                    dbc.Label('Nome do Sítio/Fazenda: ', style={'font-size':'18px', 'color':'#14a583'}),
                    html.Br(),
                    dbc.Label(dic['fazenda']),
                    html.Br(),
                    
                    dbc.Label('Tipo de Área: ', style={'font-size':'18px', 'color':'#14a583'}),
                    html.Br(),
                    dbc.Label(dic['area']),
                    html.Br(),
                    
                    dbc.Label('Nome do Proprietário: ', style={'font-size':'18px', 'color':'#14a583'}),
                    html.Br(),
                    dbc.Label(dic['proprietario']),
                    html.Br(),
                    
                    dbc.Label('Quantidade de Árvores: ', style={'font-size':'18px', 'color':'#14a583'}),
                    html.Br(),
                    dbc.Label(dic['arvores']),
                    html.Br(),
                    
                    dbc.Label('Quantidade de Faces Estriadas: ', style={'font-size':'18px', 'color':'#14a583'}),
                    html.Br(),
                    dbc.Label(dic['faces']),
                    html.Br(),
                    
                    html.Hr(),
                    
                    html.Legend('Localização', style={'text-align':'center'}),
                    
                    dbc.Label('Endereço: ', style={'font-size':'18px', 'color':'#14a583'}),
                    html.Br(),
                    dbc.Label(dic['endereco']),
                    dbc.Row([
                        
                        dbc.Col([
                            dbc.Label('Número: ', style={'font-size':'18px', 'color':'#14a583'}),
                            html.Br(),
                            dbc.Label(dic['numero']),
                        ], width=6, style={'padding-right': '10px'}),
                        
                        dbc.Col([
                            dbc.Label('Complemento: ', style={'font-size':'18px', 'color':'#14a583'}),
                            html.Br(),
                            dbc.Label(dic['complemento']),
                        ], width=6),
                        
                    ],style={'padding-top': '10px'}),  
                    
                    dbc.Label('Cidade: ', style={'font-size':'18px', 'color':'#14a583'}),
                    html.Br(),
                    dbc.Label(dic['cidade']),
                    html.Br(),
                    
                    dbc.Label('Bairro: ', style={'font-size':'18px', 'color':'#14a583'}),
                    html.Br(),
                    dbc.Label(dic['bairro']),
                    html.Br(),
                    
                    
                    dbc.Row([
                        dbc.Col([
                            dbc.Label('Estado: ', style={'font-size':'18px', 'color':'#14a583'}),
                            html.Br(),
                            dbc.Label(dic['estado']),
                        ],width=6, style={'padding-right': '10px'}),
                        dbc.Col([
                            dbc.Label('CEP: ', style={'font-size':'18px', 'color':'#14a583'}),
                            html.Br(),
                            dbc.Label(dic['cep']),
                        ], width=6),
                        
                    ],style={'padding-top': '10px'}),
                    
                    html.Hr(),
                    
                    html.Legend('Contato', style={'text-align':'center'}),
                    
                    dbc.Label('Nome Contato: ', style={'font-size':'18px', 'color':'#14a583'}),
                    html.Br(),
                    dbc.Label(dic['nome_contato']),
                    
                    dbc.Row([
                        
                        
                        dbc.Col([
                            dbc.Label('Tel. Comercial: ', style={'font-size':'18px', 'color':'#14a583'}),
                            html.Br(),
                            dbc.Label(dic['tel_com']),
                        ],width=6, style={'padding-right': '10px'}),
                        dbc.Col([
                            dbc.Label('Celular: ', style={'font-size':'18px', 'color':'#14a583'}),
                            html.Br(),
                            dbc.Label(dic['tel_cel']),
                        ], width=6),
                        
                        
                        
                    ],style={'padding-top': '10px','padding-bottom': '10px'}),
                    
                    dbc.Label('E-mail: ', style={'font-size':'18px', 'color':'#14a583'}),
                    html.Br(),
                    dbc.Label(dic['email']),
                    
                    html.Hr(),
                    
                    html.Label('Forma de Pagamento', style={'font-size':'18px', 'color':'#14a583'}),
                    
                    html.Br(),
                    dbc.Label(dic['forma_pagamento']),
                    
                    html.Hr(),
                    
                    
                    html.Legend('Dados Bancários', style={'text-align':'center'}),
            
                    dbc.Label('Banco: ', style={'font-size':'18px', 'color':'#14a583'}),
                    html.Br(),
                    dbc.Label(dic['banco']),
                    html.Br(),
                    
                    dbc.Label('Nº Banco: ', style={'font-size':'18px', 'color':'#14a583'}),
                    html.Br(),
                    dbc.Label(dic['n_banco']),
                    html.Br(),
                    
                    dbc.Label('Tipo Conta: ', style={'font-size':'18px', 'color':'#14a583'}),
                    html.Br(),
                    dbc.Label(dic['tipo_conta']),
                    
                    html.Br(),
                    dbc.Label('Agência: ', style={'font-size':'18px', 'color':'#14a583'}),
                    html.Br(),
                    dbc.Label(dic['agencia']),
                    
                    dbc.Row([
                        dbc.Col([
                            dbc.Label('Conta: ', style={'font-size':'18px', 'color':'#14a583'}),
                            html.Br(),
                            dbc.Label(dic['conta']),
                        ],width=8, style={'padding-right': '10px'}),
                        dbc.Col([
                            dbc.Label('Dígito: ', style={'font-size':'18px', 'color':'#14a583'}),
                            html.Br(),
                            dbc.Label(dic['dig_conta']),
                        ],width=4)
                                    
                    ]),
                    
                    
                    
                    html.Br(),
                    
                    html.Br()
                    
                ], style={'widht':'100%', 'height': '100%', 'background-color':'white', 'padding-left': '10px', 'padding-right': '10px'})
    return template



    
    
    
    
    


