
from app import *


card_style = {
    'width': '300px',
    'min-height': '300px',
    'padding-top': '25px',
    'padding-right': '25px',
    'padding-left': '25px',
}

# =========  Layout  =========== #
def render_layout(message):
    message = "Ocorreu algum erro durante o login." if message == "error" else message
    login = html.Div([
                dbc.Card([
                    html.Legend("Login"),
                    dbc.Input(id="user_login", placeholder="Username", type="text"),
                    dbc.Input(id="pwd_login", placeholder="Password", type="password"),
                    dbc.Button("Login", id="login_button"),
                    html.Span(message, style={'text-align': 'center','margin-top': '5px', 'color': 'red'}),
                    
                    #html.Div([
                    #    html.Label("Ou", style={"margin-right": "5px"}),
                    #    dcc.Link("Registre-se", href="/register"),
                    #], style={"padding": "20px", "justify-content": "center", "display": "flex"})
            

                ], style=card_style, className="align-self-center")
            ],style={'height': '100vh', 'display': 'flex', 'justify-content': 'center'})
                 
    return login



# =========  Callbacks Page1  =========== #
@app.callback(
    Output('login-state', 'data'),

    Input('login_button', 'n_clicks'), 

    [State('user_login', 'value'), 
    State('pwd_login', 'value')],
    )
def successful(n_clicks, username, password):
    if n_clicks == None:
        raise PreventUpdate
    user = Users.query.filter_by(username=username.lower()).first()
    if user and password is not None:
        if check_password_hash(user.password, password):
            login_user(user)
            return "success"
        else:
            return "error"
    else:
        return "error"
    