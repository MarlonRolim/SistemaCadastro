from app import *
from pages import cadastrospendentes, success, logout, homepage, login, register, cadastro, pesquisacadastro, alteracadastro, visualizarcadastro, aprovarcadastro, cadpendaprovacao
from pages.navbar import createNavBar


@app.callback(
            Output("navBar", "children"),
            Output("page-content", "children"),
              
            Input("base-url", "pathname"),
            [State("login-state", "data"), State("register-state", "data")],
            
            )
def render_page_content(pathname, login_state, register_state):
    if current_user.is_authenticated:
        if (pathname == "/app/login" or pathname == "/app/"):
            
                return  createNavBar(), homepage.render_layout(current_user.name)
        

        if pathname == "/app/register":
            
            if current_user.user_type == 1:
                return createNavBar(),register.render_layout(register_state)
            else:
                return createNavBar(), homepage.render_layout(current_user.name)
            
        if pathname == "/app/cadastro":
            return createNavBar(), cadastro.render_layout()
        
        if pathname == "/app/cadastrospendentes":
            return createNavBar(), cadastrospendentes.render_layout()
        
        if  "/alteracadastro" in pathname:
            pagina_origem = pathname.split('/')[2]
            id = pathname.split('/')[4]
            return createNavBar(), alteracadastro.render_layout(id,pagina_origem)
        
        if  "/visualizar" in pathname:
            pagina_origem = pathname.split('/')[2]
            id = pathname.split('/')[4]
            return createNavBar(), visualizarcadastro.render_layout(id,pagina_origem)
        
        if pathname == "/app/pesquisacadastro":
            return createNavBar(), pesquisacadastro.render_layout()
        
        
        if pathname == "/app/cadpendaprovacao":
            return createNavBar(), cadpendaprovacao.render_layout()
        
        if  "/aprovarcadastro" in pathname:
            pagina_origem = pathname.split('/')[2]
            id = pathname.split('/')[4]
            return createNavBar(), aprovarcadastro.render_layout(id,pagina_origem)
        
        if pathname == '/app/sucesso':
            return "", success.render_layout()
        
        if pathname == '/app/logout':
            return '', logout.render_layout()
        
        if pathname == '/app/homepage':
            return createNavBar(), homepage.render_layout(current_user.name)
    else:
        if pathname == "/app/" or pathname == "/app/login":
            return "", login.render_layout("")
        else:
            return '', login.render_layout("Usuário não logado")