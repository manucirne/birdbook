from fastapi import FastAPI
import sys
import os

cur_dir = os.getcwd()
modules_path = os.path.join(os.getcwd(), '..', 'modules')
sys.path.append(modules_path)

from passaro import Passaro
from post import Post
from usuario import Usuario
from cidade import Cidade
from visualizacao import Visualizacao
from acesso import Acesso

app = FastAPI()

@app.get("/")
async def read_root():
    return {"hello":"World"}