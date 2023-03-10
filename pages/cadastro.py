
from app import *



estados = ('AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG',
       'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR',
       'RS', 'SC', 'SE', 'SP', 'TO')



def render_layout():
    
    template = html.Div([
                    dcc.Location(id='location_cad'),
                    html.Br(),
                    html.Legend('Cadastro de Fornecedor', style={'text-align':'center'}),
                    html.Hr(),
                    dbc.Label('CNPJ: '),
                    dbc.Input(placeholder='__.___.___/____.__', type="text", minLength=14, maxLength=14, id='txt-cnpj', className='cnpj'),
                    
                    dbc.Label('CPF: '),
                    dbc.Input(placeholder='___.___.___-__', type="text", minLength=11, maxLength=11, id='txt-cpf', className='cpf'),
                    
                    dbc.Label('I.E: '),
                    dbc.Input(placeholder='', type="text", id='txt-inscricao'),
                    
                    dbc.Label('Razão Social: '),
                    dbc.Input(placeholder='', type="text", id='txt-razao'),
                    
                    dbc.Label('Nome do Sitio/Fazenda: '),
                    dbc.Input(placeholder='', type="text", id='txt-fazenda'),
                    
                    dbc.Label('Tipo de Área: '),
                    dbc.Select(id='select_area', 
                            options=[{'label': "Própria", 'value': "Propria"},{'label': "Arrendamento", 'value': "Arrendamento"}],
                            value="Propria"),
                    html.Br(),
                    html.Div([
                            dbc.Label('Nome do Proprietário: '),
                            dbc.Input(placeholder='', type="text", id='txt-proprietario'),
                    ], id="div_arrend", style={'display':'None'}),
                   
                    dbc.Label('Quantidade de Árvores: '),
                    dbc.Input(placeholder='', type="number", id='txt-arvores'),
                    
                    dbc.Label('Quantidade de Faces Estriadas: '),
                    dbc.Input(placeholder='', type="number", id='txt-faces'),
                    
                    html.Hr(),
                    
                    html.Legend('Localização', style={'text-align':'center'}),
                    dbc.Label('Endereço: '),
                    dbc.Input(placeholder='', type="text", id='txt-endereco'),
                    dbc.Row([
                        
                        dbc.Col([
                            dbc.Label('Número: '),
                            dbc.Input(placeholder='Ex: 1665 ou S/N', type="text", id='txt-end-numero'),
                        ], width=6, style={'padding-right': '10px'}),
                        
                        dbc.Col([
                            dbc.Label('Complemento: '),
                            dbc.Input(placeholder='Ex: Apto 4...', type="text", id='txt-complemento'),
                        ], width=6),
                        
                    ],style={'padding-top': '10px'}),  
                    
                    dbc.Label('Cidade: '),
                    dbc.Input(placeholder='Ex: Avaré, São Paulo', type="text", id='txt-cidade'),
                    
                    dbc.Label('Bairro: '),
                    dbc.Input(placeholder='Ex: Rural', type="text", id='txt-bairro'),
                    
                    
                    dbc.Row([
                        dbc.Col([
                            dbc.Label('Estado: '),
                            dbc.Select(id='txt-estado', 
                                    options=[{'label': i, 'value': i} for i in estados],
                                    value='SP'),
                        ],width=6, style={'padding-right': '10px'}),
                        
                        dbc.Col([
                            dbc.Label('CEP: '),
                            dbc.Input(placeholder='_____-___', type="text", id='txt-cep'),
                        ], width=6),
                        
                    ],style={'padding-top': '10px'}),
                    
                    html.Hr(),
                    
                    html.Legend('Contato', style={'text-align':'center'}),
                    
                    dbc.Label('Nome Contato: '),
                    dbc.Input(placeholder='', type="text", id='txt-nome-contato'),
                    
                    dbc.Row([
                        
                        
                        dbc.Col([
                            dbc.Label('Tel. Comercial: '),
                            dbc.Input(placeholder='(__) _________', type="text", id='txt-tel-comercial'),
                        ],width=6, style={'padding-right': '10px'}),
                        dbc.Col([
                            dbc.Label('Celular: '),
                            dbc.Input(placeholder='(__) _________', type="text", id='txt-celular'),
                        ], width=6),
                        
                        
                        
                    ],style={'padding-top': '10px','padding-bottom': '10px'}),
                    
                    dbc.Label('E-mail: '),
                    dbc.Input(placeholder='', type="email", id='txt-email'),
                    
                    html.Hr(),
                    
                    html.Legend('Forma de Pagamento', style={'text-align':'center'}),
                    
                    dbc.Select(id='select_pagamento', 
                                    options=[{'label': 'Cheque', 'value': 'Cheque'},{'label': 'Depósito', 'value': 'Depósito'}],
                                    value='Cheque'),
                    
                    html.Hr(),
                    
                    html.Div([
                                html.Legend('Dados Bancários', style={'text-align':'center'}),
                        
                                dbc.Label('Banco: '),
                                dbc.Input(placeholder='Ex: Itau, Caixa...', type="text", id='txt-banco'),
                                
                                dbc.Label('Nº Banco: '),
                                dbc.Input(placeholder='', type="text", id='txt-numero-banco'),
                                
                                dbc.Label('Tipo Conta: '),
                                dbc.Select(id='select-tipo-conta', 
                                            options=[{'label': 'Corrente', 'value': 'Corrente'},{'label': 'Poupança', 'value': 'Poupança'}],
                                            value='Corrente'),
                                html.Br(),
                                dbc.Label('Agência: '),
                                dbc.Input(placeholder='', type="text", id='txt-agencia'),
                                
                                dbc.Row([
                                    dbc.Col([
                                        dbc.Label('Conta: '),
                                        dbc.Input(placeholder='', type="text", id='txt-conta'),
                                    ],width=8, style={'padding-right': '10px'}),
                                    dbc.Col([
                                        dbc.Label('Dígito: '),
                                        dbc.Input(placeholder='', type="text", id='txt-dig-conta'),
                                    ],width=4)
                                    
                                ])
                        ],id='dados-bancarios', style={'display':'None'}),
                    html.Div(id='fantasma'),
                    dbc.Button("Cadastrar", id='btn_cadastro', style={'width': '100%'}),
                    html.Br(),
                    
                    html.Br(),
                    html.Script('''$(document).ready(function(){
  $('.cpf').mask('000.000.000-00', {reverse: true});
  $('.cnpj').mask('00.000.000/0000-00', {reverse: true});
});''')
                ], style={'widht':'100%', 'height': '100%', 'background-color':'white', 'padding-left': '10px', 'padding-right': '10px'})
    return template


# =============== Calback ================ #
@app.callback(
    Output('dados-bancarios','style'),
    Input('select_pagamento','value'),
    State('select_pagamento','value')
)
def banco(n_clicks,pagamento):
    
    if pagamento == 'Depósito':
        return {}
    else: return {'display':'None'}
    
@app.callback(
    Output('div_arrend','style'),
    Input('select_area','value'),
    State('select_area','value')
)
def banco(n_clicks,pagamento):
    
    if pagamento == "Arrendamento":
        return {}
    else: return {'display':'None'}
    
@app.callback(
    [Output('cad-store', 'data'),
    Output('fantasma', 'children')],
    Input('btn_cadastro', 'n_clicks'),
    [
        State('txt-cnpj', 'value'),
        State('txt-cpf', 'value'),
        State('txt-inscricao', 'value'),
        State('txt-razao', 'value'),
        State('txt-endereco', 'value'),
        State('txt-end-numero', 'value'),
        State('txt-complemento', 'value'),
        State('txt-cidade', 'value'),
        State('txt-bairro', 'value'),
        State('txt-estado', 'value'),
        State('txt-cep', 'value'),
        State('txt-nome-contato', 'value'),
        State('txt-tel-comercial', 'value'),
        State('txt-celular', 'value'),
        State('txt-email', 'value'),
        State('select_pagamento', 'value'),
        State('txt-banco', 'value'),
        State('txt-numero-banco', 'value'),
        State('select-tipo-conta', 'value'),
        State('txt-agencia', 'value'),
        State('txt-conta', 'value'),
        State('txt-dig-conta', 'value'),
        State('txt-fazenda', 'value'),
        State('select_area', 'value'),
        State('txt-proprietario', 'value'),
        State('txt-arvores', 'value'),
        State('txt-faces', 'value'),
        
    ]
)
def cadastrar(n_clicks, cnpj, cpf, ie, razao, endereco, n_endereco, complemento, cidade, bairro, estado, cep, nome_contato, tel_com, tel_cel, email, form_pagamento, banco, n_banco, tipo_conta, agencia, conta, n_conta, fazenda, area, proprietario, arvores, faces):
    if n_clicks == None:
        raise PreventUpdate
    
    if (cnpj == None and cpf == None) or (cnpj == "" and cpf == None) or (cnpj == None and cpf == "") or (cnpj == "" and cpf == ""):
        return '',dbc.Alert('Preencha os campos CNPJ ou CPF!',color='danger')
    
    if cpf == None:
        cpf = ''
        
    if cnpj == None:
        cnpj = ''
    if ie == None or ie == "":
        return '',dbc.Alert('Preencha a Iscrição Estadual! Se não possuir, colocar como ISENTO',color='danger')
    
    if razao == None or razao == "":
        return '',dbc.Alert('Preencha a Razão Social!',color='danger')
    
    if fazenda == None or fazenda == "":
        return '',dbc.Alert('Preencha a o Sitio/Fazenda!',color='danger')
    
    if area == None or area == "":
        return '',dbc.Alert('Preencha o tipo de Área!',color='danger')
    
    if area == "Arrendamento" and (proprietario == None or proprietario == ""):
        return '',dbc.Alert('Preencha o Nome do Proprietário!',color='danger')
    
    if arvores == None or arvores == "":
        return '',dbc.Alert('Preencha a Quantidade de Árvores!',color='danger')
    if faces == None or faces == "":
        return '',dbc.Alert('Preencha a Quantidade de Faces estriadas!',color='danger')
    
    if endereco == None or endereco == '' or n_endereco == None or n_endereco == '' or cidade == None or cidade == '' or estado == None or estado == '' or cep == None or cep == '':
        return '',dbc.Alert('Preencha todos os campos de endereço!',color='danger')
    
    if nome_contato == None or nome_contato == "":
        return '',dbc.Alert('Preencha o Nome do Contato!',color='danger')
    
    if tel_cel == None or tel_cel == "":
        return '',dbc.Alert('Preencha o Número do Celular para contato!',color='danger')
    
    
    if form_pagamento == 'Depósito':
        if banco == None or banco == '' or agencia == None or agencia == '' or conta == None or conta == '' or n_conta == None or n_conta == '':
            return '',dbc.Alert('Preencha todos os campos de Dados bancários!',color='danger')
    
    if complemento == None:
        complemento = ''
    
    if proprietario == None:
        proprietario = ''
        
    if bairro == None:
        bairro = ''
    
    if nome_contato == None:
        nome_contato = ''
    
    if tel_com == None:
        tel_com = ''
        
    if tel_cel == None:
        tel_cel = ''
        
    if email == None:
        email = ''
        
    if banco == None:
        banco = ''
    
    if n_banco == None:
        n_banco = ''
    
    if form_pagamento == "Cheque":
        tipo_conta = ''
    
    
    if agencia == None:
        agencia = ''
    
    if conta == None:
        conta = ''
    
    if n_conta == None:
        n_conta = ''
    
    ins = Cadastros_tbl.insert().values(
                                    
                                    cnpj = str(cnpj),
                                    cpf = str(cpf),
                                    ie = str(ie),
                                    razao = str(razao),
                                    endereco = str(endereco),
                                    numero = str(n_endereco),
                                    complemento = str(complemento),
                                    cidade = str(cidade),
                                    bairro = str(bairro),
                                    estado = str(estado),
                                    cep = str(cep),
                                    nome_contato = str(nome_contato),
                                    tel_com = str(tel_com),
                                    tel_cel = str(tel_cel),
                                    email = str(email),
                                    forma_pagamento = str(form_pagamento),
                                    banco = str(banco),
                                    n_banco = str(n_banco),
                                    tipo_conta = str(tipo_conta),
                                    agencia = str(agencia),
                                    conta = str(conta),
                                    fazenda = fazenda,
                                    area = area,
                                    proprietario = proprietario,
                                    arvores = arvores,
                                    faces = faces,
                                    dig_conta = str(n_conta),
                                    usuario = current_user.id,
                                    status_cad = "Pendente",
                                    data_cad = datetime.date.today()
                                    )
    conn = engine.connect()
    conn.execute(ins)
    conn.close()
    
    mensagem = fr"""Novo Cadastro
{razao}"""
    df =  pd.read_sql(fr"select id from users where user_type = '{1}'", create_connection())
    admins = df['id'].unique()
    for i in admins:
        enviar_notificacao(id_notificacao(i), mensagem)
    
    return 'Sucesso',''
    
@app.callback(
    Output(component_id='txt-cpf', component_property='value'),
    [Input(component_id='txt-cpf', component_property='value')]
)

def format_cpf(cpf):
    if cpf == None:
        raise PreventUpdate
    cpf = re.sub(r'(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.\2.\3-\4', cpf)
    return cpf

@app.callback(
    Output(component_id='txt-cnpj', component_property='value'),
    [Input(component_id='txt-cnpj', component_property='value')]
)

def format_cnpj(cnpj):
    if cnpj == None:
        raise PreventUpdate
    cnpj = re.sub(r'(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})', r'\1.\2.\3/\4-\5', cnpj)
    return cnpj

@app.callback(
    Output(component_id='txt-cep', component_property='value'),
    [Input(component_id='txt-cep', component_property='value')]
)

def format_cep(cep):
    if cep == None:
        raise PreventUpdate
    cep = re.sub(r'(\d{5})(\d{3})', r'\1-\2', cep)
    return cep
    
@app.callback(
    Output('location_cad', 'pathname'),
    Input('cad-store', 'data'),
    State('cad-store', 'data')
)
def sucesso(trig, data):
    if data == "Sucesso":
        return '/app/sucesso'
    


