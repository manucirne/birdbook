from fastapi import FastAPI
from pydantic import BaseModel

import sys
import os
import pymysql
import json 

modules_path = os.path.join(os.getcwd(), '..', 'modules')
sys.path.append(modules_path)
from passaro import Passaro
from post import Post
from usuario import Usuario
from cidade import Cidade
from visualizacao import Visualizacao
from acesso import Acesso

sys.path.append(os.getcwd())

with open(os.path.join(os.getcwd(), '..', 'config', 'config_tests.json'), 'r') as f:
    config = json.load(f)

connection = pymysql.connect(
    host=config['HOST'],
    user=config['USER'],
    password=config['PASS'],
    database='birdbook')

app = FastAPI()

class passaroObj(BaseModel):
    tag: str
    especie: str
    nome_pop: str
class usuarioObj(BaseModel):
    nome: str
    especie: str
    nome_pop: str
    
class joinhaObj(BaseModel):
    user_id: str
    post_id: str
    reacao: str
    
class postObj(BaseModel):
    user_id: str
    post_id: str
    reacao: str

@app.get("/")
def read_root():
    return {"hello":"World"}


@app.get("/passaro")
def get_passaro():
    pas = Passaro(connection)
    passaros = pas.lista()
    if passaros:
        return [ {"tag": p[0], "especie": p[1], "nome_pop": p[2]} for p in passaros]
    return []

@app.post("/passaro")
def post_passaro(item: passaroObj):
    pas = Passaro(connection)
    try:
        pas.adiciona(item.tag.lower(), item.especie, item.nome_pop)
        connection.commit()
    except Exception as e:
        return {"error": "Não foi possivel adicionar passaro"}
    return []

@app.put("/passaro")
def put_passaro(item: passaroObj):
    pas = Passaro(connection)
    try:
        pas.atualiza(item.tag.lower(), item.especie, item.nome_pop)
    except Exception as e:
        return {"error": "Não foi possivel adicionar passaro"}
    return []

@app.get("/passaro/{passaro_id}")
def get_passaro(passaro_id: str):
    pas = Passaro(connection)
    try:
        passaros = pas.acha(passaro_id.lower())
        return passaros
    except Exception as e:
        return {"error": "Não foi possivel adicionar passaro"}

@app.delete("/passaro/{passaro_id}")
def delete_passaro(passaro_id: str):
    pas = Passaro(connection)
    try:
        pas.remove(passaro_id.lower())
        return {}
    except Exception as e:
        return {"error": "Não foi possivel adicionar passaro"}

# User 
@app.get("/usuario")
def read_usuario():
    usr = Usuario(connection)
    usuario = usr.lista()
    if usuario:
        return [ {"tag": p[0], "especie": p[1], "nome_pop": p[2]} for p in passaros]
    return []

@app.post("/usuario")
def post_usuario(item: passaroObj):
    pas = Passaro(connection)
    try:
        pas.adiciona(item.tag.lower(), item.especie, item.nome_pop)
        connection.commit()
    except Exception as e:
        return {"error": "Não foi possivel adicionar passaro"}
    return []

@app.put("/usuario")
def put_usuario(item: passaroObj):
    pas = Passaro(connection)
    try:
        pas.atualiza(item.tag.lower(), item.especie, item.nome_pop)
    except Exception as e:
        return {"error": "Não foi possivel adicionar passaro"}
    return []

@app.get("/usuario/{usuario_id}")
def get_id_usuario(usuario_id: str):
    pas = Passaro(connection)
    try:
        passaros = pas.acha(passaro_id.lower())
        return passaros
    except Exception as e:
        return {"error": "Não foi possivel adicionar passaro"}

@app.delete("/usuario/{usuario_id}")
def delete_usuario(usuario_id: str):
    pas = Passaro(connection)
    try:
        pas.remove(passaro_id.lower())
        return {}
    except Exception as e:
        return {"error": "Não foi possivel adicionar passaro"}



@app.post("/joinha")
def add_joinha(user_id: str):
    pas = Passaro(connection)
    try:
        pas.remove(passaro_id.lower())
        return {}
    except Exception as e:
        return {"error": "Não foi possivel adicionar passaro"}

@app.post("/post")
def add_post(user_id: str):
    pas = Passaro(connection)
    try:
        pas.remove(passaro_id.lower())
        return {}
    except Exception as e:
        return {"error": "Não foi possivel adicionar passaro"}


@app.delete("/post")
def add_post(user_id: str):
    pas = Passaro(connection)
    try:
        pas.remove(passaro_id.lower())
        return {}
    except Exception as e:
        return {"error": "Não foi possivel adicionar passaro"}