import pandas as pd
import numpy as np
import dash
from flask_login import login_user, logout_user, current_user
from dash.exceptions import PreventUpdate
from app import *
from routes import *



login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = '/login'


# =====================  Layout  ===================== #

def createNavBar():
    
    if current_user.user_type == 1:
        admin = html.Div([
                            html.Br(),
                            html.Legend('Admin',style={'text-align':'center'}),
                            html.Hr(),
                            dbc.Button('Aprovar Cadastros', href='/cadpendaprovacao', style={'width': '100%','margin-top': '5px'}),
                            #html.Hr(style={'margin': '0px 0'}),
                            html.Br(),
                            dbc.Button('Cadastrar Usuário', href='/register', style={'width': '100%','margin-top': '5px'})  
                        ])
    else: 
        admin = html.Div()
    
    
    logout = dbc.Col(dbc.Button(html.Div(className="fa fa-sign-out", style=card_icon_menu),id='logout_button',href='/logout',style={'align-itens':'center','width': '100%', 'border': 'None' ,'background-color': 'transparent', 'box-shadow':'None'}),width=2)
    
        
    template= html.Div([
                            dbc.Row([
                            dbc.Col(dbc.Button(html.Div(className="fa fa-navicon", style=card_icon_menu),id='open-offcanvas-placement',style={'align-itens':'center','width': '100%', 'border': 'None' ,'background-color': 'transparent', 'box-shadow':'None'}),width=2),
                            dbc.Col(html.Div(html.A(html.Img(src='/assets/logo_rb.png',style={'height':50}), href='/homepage'),style={'text-align':'center', 'padding':'0'}),width=8),
                            logout
                            
                            ], style={"padding": "0px", 'margin': '0px'}),
                                dbc.Offcanvas([
                                    html.Legend('Menu',style={'text-align':'center'}),
                                    html.Hr(),
                                    dbc.Button('Página Inicial', href='/homepage', style={'width': '100%','margin-top': '5px'}),
                                    #html.Hr(style={'margin': '0px 0'}),
                                    html.Br(),
                                    dbc.Button(children='Novo Cadastro', href='/cadastro', style={'width': '100%','margin-top': '5px'}),
                                    #html.Hr(style={'margin': '0px 0'}),
                                    html.Br(),
                                    dbc.Button('Cadastros Pendentes', href='/cadastrospendentes', style={'width': '100%','margin-top': '5px'}),
                                    #html.Hr(style={'margin': '0px 0'}),
                                    html.Br(),
                                    dbc.Button('Pesquisa de Cadastros', href='/pesquisacadastro', style={'width': '100%','margin-top': '5px'}),
                                    admin
                                    ],   
                                id="offcanvas-placement",
                                
                                is_open=False,
                                style={'text-align':'center'}
                            ),
                            ], style={'background-color': 'white', 'height':50, 'width':'100%', 'border-bottom':'1px solid grey','box-shadow': '0 4px 2px -3px gray', 'padding':'0','margin':'0'})
                        
    return template

def render_layout():
    template = html.Div(children=[
                    dbc.Row([
                            dcc.Location(id='base-url', refresh=False),
                            dcc.Location(id='log-url', refresh=False),
                            html.Div(id='navBar',style={'height': '100%','width':'100%','padding':'0' }),
                            
                    ],style={'--bs-gutter-x': '0'}),
                    html.Div([
                            html.Script(src='src="https://cdnjs.cloudflare.com/ajax/libs/jquery.mask/1.14.16/jquery.mask.min.js'),
                            dcc.Store(id='login-state',data=''),
                            dcc.Store(id='register-state',data=''),
                            dcc.Store(id='cad-store', data=''),
                            dcc.Store(id='alt-store', data=''),
                            dcc.Store(id='aprova-store', data=''),
                            html.Div(id='page-content', style={'width':'100%','padding-left': '10px', 'padding-right': '10px'})
                            
                        
                    ],style={'width':'100%'}),
                ], style={"padding": "0px",})
    return template

app.layout = render_layout()

# ===================== Callbacks ===================== #

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.callback(
    Output("offcanvas-placement", "is_open"),
    Input("open-offcanvas-placement", "n_clicks"),
    [State("offcanvas-placement", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open

@app.callback(Output("base-url", "pathname"), 
            [
                Input("login-state", "data"),
                Input("register-state", "data"),
                
                
            ])
def render_page_content(login_state, register_state):
    ctx = dash.callback_context
    if ctx.triggered:
        trigg_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        if trigg_id == 'login-state' and login_state == "success":
            return '/homepage'
        if trigg_id == 'login-state' and login_state == "error":
            return '/login'
        
                

        elif trigg_id == 'register-state':
            if register_state == "":
                return '/sucesso'
            else:
                return '/register'
    else:
        return '/'
    

    
    







if __name__ == "__main__":
    #app.run_server(host='172.16.50.62',port=8051, debug=True)
    app.run_server(debug=False)
    #app.run_server(host='192.168.1.17',port=8051, debug=True)
    
    
    
