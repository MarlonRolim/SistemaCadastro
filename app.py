import dash
from dash import html, dcc, Input, Output, State, ClientsideFunction, ALL, callback_context
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from sqlalchemy import Table, create_engine
from sqlalchemy.sql import select
from pages.styles import *
from pywebpush import webpush, WebPushException 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, current_user,login_user,logout_user
import logging
import json, os
import pandas as pd
import datetime
from flask import request, Response, render_template, jsonify, Flask, redirect
import os
from werkzeug.security import generate_password_hash, check_password_hash
# import configparser
import re
import requests
from models import *
VAPID_PRIVATE_KEY = "hTYyfptvH-frKuVg8sRqw7m8CXzyqSN9Kzhqbae2iRQ"
VAPID_PUBLIC_KEY = "BGUHeKkyN5nd5BFTKzG9cgaX10oCGRk6pNXIyuUittBtRl_p8VUs33FCoqcUUlf-h5L436ioZ4GgAgH5RdRalOo"

VAPID_CLAIMS = {
"sub": "mailto: <marlon.rolim@resinasbrasil.com.br>",
}


def send_web_push(subscription_information, message_body):
    return webpush(
        subscription_info=subscription_information,
        data=message_body,
        vapid_private_key=VAPID_PRIVATE_KEY,
        vapid_claims=VAPID_CLAIMS
    )

def id_notificacao(id):
    dados = json.loads(requests.get(f'https://appcadastro-rb-default-rtdb.firebaseio.com/notification_keys/.json?orderBy="/id_user"&equalTo={int(id)}').text)
    if dados == {}:
        return "Não Cadastrado"
    else:
        for i in dados.keys(): token_id = i
        id_notification = dados[token_id]['key']
    return id_notification

def enviar_notificacao(token, mensagem):
    if token == "Não Cadastrado":
        print(token)
    else:
        try:
            send_web_push(token, mensagem)
            
        except Exception as e:
            print("error",e)
        

estilos = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css", "https://fonts.googleapis.com/icon?family=Material+Icons", dbc.themes.MINTY]
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"



server = Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=estilos + [dbc_css], 
                assets_folder='static',
                server=server,
                meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}],
                
                routes_pathname_prefix="/app/",
                title='Cadastros RB')
                
app._favicon = ("favicon.ico")

app.config.suppress_callback_exceptions = True

server.config.update(
    SECRET_KEY=os.urandom(12),
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://admin:FjO7XSMMxr0uNzN9hPQQis7OVAwxcqSz@dpg-cevbqmp4reb4eat12feg-a.oregon-postgres.render.com/db_cadastros',
    SQLALCHEMY_TRACK_MODIFICATIONS=False)

db.init_app(server)

class Users(UserMixin, Users):
    pass

# Setup the LoginManager for the server
