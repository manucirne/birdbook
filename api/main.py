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
    

@app.get("/")
def read_root():
    return {"hello":"World"}


@app.get("/passaro")
def read_passaro():
    pas = Passaro(connection)
    passaros = pas.lista()
    if passaros:
        return [ {"tag": p[0], "especie": p[1], "nome_pop": p[2]} for p in passaros]
    return []

@app.post("/passaro")
def read_passaro(item: passaroObj):
    pas = Passaro(connection)
    try:
        passaros = pas.adiciona(item.tag.lower(), item.especie, item.nome_pop)
    except Exception as e:
        return {"error": "Não foi possivel adicionar passaro"}
    return 

# @app.put("/passaro")
# def read_passaro(item: passaroObj):
#     pas = Passaro(connection)
#     print(item)
#     passaros = pas.adiciona(item.tag, item.especie, item.nome_pop)
#     # if passaros:
#     #     return [ {nome: p[0]} for p in passaros]
#     return []