
from app import *
from routes import *
from pushnotification import *


login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = '/app/login'


# =====================  Layout  ===================== #



def render_layout():
    template = html.Div(children=[
                    dbc.Row([
                            dcc.Location(id='base-url', refresh=False),
                            dcc.Location(id='log-url', refresh=False),
                            dbc.Col(html.Div(id='navBar',style={'width':'100%','padding':'0' }),md=12, style={"position": "fixed", "top": "0"})
                            
                            
                    ],style={'--bs-gutter-x': '0'}),
                    html.Div([
                            dcc.Store(id='login-state',data=''),
                            dcc.Store(id='register-state',data=''),
                            dcc.Store(id='cad-store', data=''),
                            dcc.Store(id='alt-store', data=''),
                            dcc.Store(id='aprova-store', data=''),
                            html.Div(id='page-content', style={'width':'100%','padding-left': '10px', 'padding-right': '10px',"overflow-y": "hidden"})
                            
                        
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
            return '/app/homepage'
        if trigg_id == 'login-state' and login_state == "error":
            return '/app/login'
        
                

        elif trigg_id == 'register-state':
            if register_state == "":
                return '/app/sucesso'
            else:
                return '/app/register'
    else:
        return '/app/'
    

    
    







if __name__ == "__main__":
    #app.run_server(host='172.16.50.62',port=8051, debug=True)
    app.run_server(debug=False)
    #app.run_server(host='192.168.1.17',port=8051, debug=True)
    
    
    
