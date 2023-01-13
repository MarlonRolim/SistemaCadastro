import dash
import dash_bootstrap_components as dbc
from sqlalchemy import Table, create_engine
from sqlalchemy.sql import select

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
import os
# import configparser


from models import *


estilos = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css", "https://fonts.googleapis.com/icon?family=Material+Icons", dbc.themes.MINTY]
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"




app = dash.Dash(__name__, external_stylesheets=estilos + [dbc_css], meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
        
    ],title='Cadastros RB')
app._favicon = ("assets/favicon.ico")
server = app.server
app.config.suppress_callback_exceptions = True

server.config.update(
    SECRET_KEY=os.urandom(12),
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://admin:FjO7XSMMxr0uNzN9hPQQis7OVAwxcqSz@dpg-cevbqmp4reb4eat12feg-a.oregon-postgres.render.com/db_cadastros',
    SQLALCHEMY_TRACK_MODIFICATIONS=False)

db.init_app(server)

class Users(UserMixin, Users):
    pass

# Setup the LoginManager for the server
