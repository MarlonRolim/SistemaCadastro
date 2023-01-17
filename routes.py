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
    
    if (pathname == "/login" or pathname == "/"):
        if current_user.is_authenticated:
            return  createNavBar(), homepage.render_layout(current_user.name)
        else:
            return '',login.render_layout(login_state)

    if pathname == "/register":
        
        if current_user.is_authenticated:
            if current_user.user_type == 1:
                return createNavBar(),register.render_layout(register_state)
            else:
                return createNavBar(), homepage.render_layout(current_user.name)
        else:
            return '',login.render_layout(login_state)
        
    if pathname == "/cadastro":
        if current_user.is_authenticated:
            return createNavBar(), cadastro.render_layout()
        else:
            return '',login.render_layout("")
        
        #return createNavBar(), cadastro.render_layout()
    
    if pathname == "/cadastrospendentes":
        if current_user.is_authenticated:
            return createNavBar(), cadastrospendentes.render_layout()
        else:
            return '',login.render_layout("")
        
        #return createNavBar(), cadastrospendentes.render_layout()
    
    if  "/alteracadastro" in pathname:
        if current_user.is_authenticated:
            pagina_origem = pathname.split('/')[1]
            id = pathname.split('/')[3]
            return createNavBar(), alteracadastro.render_layout(id,pagina_origem)
        else:
            return '',login.render_layout("")
        #pagina_origem = pathname.split('/')[1]
        #id = pathname.split('/')[3]
        #return createNavBar(), alteracadastro.render_layout(id,pagina_origem)
    
    if  "/visualizar" in pathname:
        if current_user.is_authenticated:
            pagina_origem = pathname.split('/')[1]
            id = pathname.split('/')[3]
            return createNavBar(), visualizarcadastro.render_layout(id,pagina_origem)
        else:
            return '',login.render_layout("")
        
        #pagina_origem = pathname.split('/')[1]
        #id = pathname.split('/')[3]
        #return createNavBar(), visualizarcadastro.render_layout(id,pagina_origem)
    
    if pathname == "/pesquisacadastro":
        if current_user.is_authenticated:
            return createNavBar(), pesquisacadastro.render_layout()
        else:
            return '',login.render_layout("")
        
        #return createNavBar(), pesquisacadastro.render_layout()
    
    
    if pathname == "/cadpendaprovacao":
        if current_user.is_authenticated:
            return createNavBar(), cadpendaprovacao.render_layout()
        else:
            return '',login.render_layout("")
        
        #return createNavBar(), cadpendaprovacao.render_layout()
    
    if  "/aprovarcadastro" in pathname:
        if current_user.is_authenticated:
            pagina_origem = pathname.split('/')[1]
            id = pathname.split('/')[3]
            return createNavBar(), aprovarcadastro.render_layout(id,pagina_origem)
        else:
            return '',login.render_layout("")
        
        #pagina_origem = pathname.split('/')[1]
        #id = pathname.split('/')[3]
        #return createNavBar(), aprovarcadastro.render_layout(id,pagina_origem)
    
    if pathname == '/sucesso':
        if current_user.is_authenticated:
            return createNavBar(), success.render_layout()
        else:
            return '',login.render_layout("")
        
        #return '', success.render_layout()
    
    if pathname == '/logout':
        return '', logout.render_layout()
    
    if pathname == '/homepage':
        if current_user.is_authenticated:
            
            return createNavBar(), homepage.render_layout(current_user.name)
        else:
            return '', login.render_layout("Usuário não logado  ")
        #return createNavBar(), homepage.render_layout("Marlon Rolim")