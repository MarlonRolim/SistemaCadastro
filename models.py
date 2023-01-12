from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, create_engine
from sqlalchemy.sql import select
from sqlite3 import Error
import sqlite3
import psycopg2

#conn = psycopg2.connect(
#    host="dpg-cevbqmp4reb4eat12feg-a.oregon-postgres.render.com",
#    database="db_cadastros",
#    user="admin",
#    password="FjO7XSMMxr0uNzN9hPQQis7OVAwxcqSz")

db = SQLAlchemy()
#conn = sqlite3.connect('instance/data.sqlite')
#engine = create_engine('sqlite:///instance/data.sqlite')
engine = create_engine('postgresql+psycopg2://admin:FjO7XSMMxr0uNzN9hPQQis7OVAwxcqSz@dpg-cevbqmp4reb4eat12feg-a.oregon-postgres.render.com/db_cadastros')

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable = False)
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

Users_tbl = Table('users', Users.metadata)
    
class Cadastros(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.String(18))
    cpf = db.Column(db.String(14))
    ie = db.Column(db.String(20))
    razao = db.Column(db.String(50))
    endereco = db.Column(db.String(50))
    numero = db.Column(db.String(5))
    complemento = db.Column(db.String(15))
    cidade = db.Column(db.String(50))
    bairro = db.Column(db.String(50))
    estado = db.Column(db.String(2))
    cep = db.Column(db.String(9))
    nome_contato = db.Column(db.String(50))
    tel_com = db.Column(db.String(15))
    tel_cel = db.Column(db.String(15))
    email = db.Column(db.String(50))
    forma_pagamento = db.Column(db.String(8))
    banco = db.Column(db.String(15))
    n_banco = db.Column(db.String(4))
    tipo_conta = db.Column(db.String(8))
    agencia = db.Column(db.String(4))
    conta = db.Column(db.String(10))
    dig_conta = db.Column(db.String(2))
    usuario = db.Column(db.String(20))
    status_cad = db.Column(db.String(10))
    data_cad = db.Column(db.String(10))
    
Cadastros_tbl = Table('cadastros', Cadastros.metadata)

class Pendencias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_cadastro = db.Column(db.String(5), unique=True, nullable = False)
    id_item = db.Column(db.String(20), nullable = False)
    observacao = db.Column(db.String(50))
    
Pendencias_tbl = Table('pendencias', Pendencias.metadata)


def create_connection():
    db_file = 'instance/data.sqlite'
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = create_engine('postgresql+psycopg2://admin:FjO7XSMMxr0uNzN9hPQQis7OVAwxcqSz@dpg-cevbqmp4reb4eat12feg-a.oregon-postgres.render.com/db_cadastros')
    except Error as e:
        print(e)

    return conn

def data_mesAtual():
    import datetime
    import calendar
    hoje = datetime.date.today()
    primeiro = "01"
    ultimo = str(calendar.monthrange(hoje.year, hoje.month)[1])
    ano = str(hoje.year)

    if hoje.month < 10:
        mes = "0" + str(hoje.month)
    else:
        mes = str(hoje.month)
        
    #inicio = primeiro + "/" + mes + "/" + ano
    #fim = ultimo + "/" + mes + "/" + ano
    
    inicio = ano + "-" + mes + "-" + primeiro
    fim = ano + "-" + mes + "-" + ultimo
    
    #'2022-12-01'
    
    return inicio, fim