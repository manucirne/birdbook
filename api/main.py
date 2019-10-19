from fastapi import FastAPI
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

app = FastAPI()

    
with open(os.path.join(os.getcwd(), '..', 'config', 'config_tests.json'), 'r') as f:
    config = json.load(f)

connection = pymysql.connect(
    host=config['HOST'],
    user=config['USER'],
    password=config['PASS'],
    database='birdbook')

@app.get("/")
async def read_root():
    return {"hello":"World"}
