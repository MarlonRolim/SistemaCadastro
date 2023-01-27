from app import *

def createNavBar():
    
    if current_user.user_type == 1:
        admin = html.Div([
                            html.Br(),
                            html.Legend('Admin',style={'text-align':'center'}),
                            html.Hr(),
                            dbc.Button('Aprovar Cadastros', href='/app/cadpendaprovacao', style={'width': '100%','margin-top': '5px'}),
                            #html.Hr(style={'margin': '0px 0'}),
                            html.Br(),
                            dbc.Button('Cadastrar Usuário', href='/app/register', style={'width': '100%','margin-top': '5px'})  
                        ])
    else: 
        admin = html.Div()
    
    
    logout = dbc.Col(dbc.Button(html.Div(className="fa fa-sign-out", style=card_icon_menu),id='logout_button',href='/app/logout',style={'align-itens':'center','width': '100%', 'border': 'None' ,'background-color': 'transparent', 'box-shadow':'None'}),width=2)
    
        
    template= html.Div([
                            dbc.Row([
                            dbc.Col(dbc.Button(html.Div(className="fa fa-navicon", style=card_icon_menu),id='open-offcanvas-placement',style={'align-itens':'center','width': '100%', 'border': 'None' ,'background-color': 'transparent', 'box-shadow':'None'}),width=2),
                            dbc.Col(html.Div(html.A(html.Img(src='/static/images/logo_rb.png',style={'height':50}), href='/app/homepage'),style={'text-align':'center', 'padding':'0'}),width=8),
                            logout
                            
                            ], style={"padding": "0px", 'margin': '0px'}),
                                dbc.Offcanvas([
                                    html.Legend('Menu',style={'text-align':'center'}),
                                    html.Hr(),
                                    dbc.Button('Página Inicial', href='/app/homepage', style={'width': '100%','margin-top': '5px'}),
                                    #html.Hr(style={'margin': '0px 0'}),
                                    html.Br(),
                                    dbc.Button(children='Novo Cadastro', href='/app/cadastro', style={'width': '100%','margin-top': '5px'}),
                                    #html.Hr(style={'margin': '0px 0'}),
                                    html.Br(),
                                    dbc.Button('Cadastros Pendentes', href='/app/cadastrospendentes', style={'width': '100%','margin-top': '5px'}),
                                    #html.Hr(style={'margin': '0px 0'}),
                                    html.Br(),
                                    dbc.Button('Pesquisa de Cadastros', href='/app/pesquisacadastro', style={'width': '100%','margin-top': '5px'}),
                                    admin
                                    ],   
                                id="offcanvas-placement",
                                
                                is_open=False,
                                style={'text-align':'center'}
                            ),
                            ], style={'background-color': 'white', 'height':50, 'width':'100%', 'border-bottom':'1px solid grey','box-shadow': '0 4px 2px -3px gray', 'padding':'0','margin':'0'})
                        
    return template