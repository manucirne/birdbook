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
from joinha import Joinha
from busca import Busca

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
    email: str
    username: str
    idCidade: int

class cidadeObj(BaseModel):
    cidade: str
    estado: str
    
class joinhaObj(BaseModel):
    user_id: str
    post_id: int
    reacao: int

class joinhaUpdateObj(BaseModel):
    user_id: str
    post_id: int
    
class postObj(BaseModel):
    user_id: str
    titulo: str
    texto: str
    url_foto: str

class postUpdateObj(BaseModel):
    titulo: str
    texto: str
    url_foto: str


@app.get("/")
def read_root():
    return {"hello":"World"}


@app.get("/passaro")
def get_passaro():
    pas = Passaro(connection)
    passaros = pas.lista()
    if passaros:
        return [ {"tag": p[0], "especie": p[1], "nome_pop": p[2]} for p in passaros]
    return {}

@app.post("/passaro")
def post_passaro(item: passaroObj):
    pas = Passaro(connection)
    try:
        pas.adiciona(item.tag.lower(), item.especie, item.nome_pop)
    except Exception as e:
        return {"error": "Não foi possivel adicionar passaro"}
    return {}

@app.put("/passaro")
def put_passaro(item: passaroObj):
    pas = Passaro(connection)
    try:
        pas.atualiza(item.tag.lower(), item.especie, item.nome_pop)
    except Exception as e:
        return {"error": "Não foi possivel adicionar passaro"}
    return {}

@app.get("/passaro/{passaro_id}")
def get_passaro(passaro_id: str):
    pas = Passaro(connection)
    try:
        p = pas.acha(passaro_id.lower())
        return {"tag": p[0], "especie": p[1], "nome_pop": p[2]}
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
    usuarios = usr.lista()
    try:
        if usuarios:
            return [ {"username": p[0], "email": p[1], "nome": p[2], "idCidade": p[3]} for p in usuarios]
    except Exception as e:
        print(e)
        return {"error": "Não foi possivel listar usuário"}
    return {}


@app.post("/usuario")
def post_usuario(item: usuarioObj):
    usr = Usuario(connection)
    try:
        usr.adiciona(item.username, item.email, item.nome, item.idCidade)
    except Exception as e:
        print(e)
        return {"error": "Não foi possivel adicionar usuário"}
    return {}

@app.put("/usuario")
def put_usuario(item: usuarioObj):
    usr = Usuario(connection)
    try:
        if(item.nome):
            usr.muda_nome(item.username, item.nome)
        if(item.email):
            usr.muda_email(item.username, item.email)
        if(item.idCidade):
            usr.muda_cidade(item.username, item.idCidade)
    
    except Exception as e:
        return {"error": "Não foi possivel atualizar usuário"}
    return {}

@app.get("/usuario/{usuario_id}")
def get_id_usuario(usuario_id: str):
    usr = Usuario(connection)
    try:
        u = usr.acha(usuario_id)
        return {"username": u[0], "email": u[1], "nome": u[2], "idCidade": u[3]}
    except Exception as e:
        return {"error": "Não foi possivel listar usuarios"}

@app.delete("/usuario/{usuario_id}")
def delete_usuario(usuario_id: str):
    usr = Usuario(connection)
    try:
        usr.remove(usuario_id)
        return {}
    except Exception as e:
        return {"error": f"Não foi possivel delerar o usuário {usuario_id} passaro"}



@app.post("/cidade")
def add_cidade(item: cidadeObj):
    cidade = Cidade(connection)
    try:
        cidade.adiciona(item.cidade, item.estado)
    except Exception as e:
        return {"error": "Não foi possivel adicionar cidade"}
    return {}


@app.get("/cidade")
def get_cidades():
    cidade = Cidade(connection)
    try:
        cidades = cidade.lista()
        if cidades:
            return [{"idCidade": c[0], "cidade":c[1], "estado":c[2]} for c in cidades]
    except Exception as e:
        return {"error": "Não foi possivel listar cidades"}


@app.delete("/cidade/{cidade_id}")
def delete_cidade(cidade_id: str):
    cidade = Cidade(connection)
    try:
        cidades = cidade.remove_id(cidade_id)
        return {}
    except Exception as e:
        return {"error": "Não foi possivel listar cidades"}

@app.post("/post")
def add_post(item: postObj):
    post = Post(connection)
    try:
        id = post.adiciona(item.user_id, item.titulo, item.texto, item.url_foto)
        dici_tags = post.parser_post(item.texto)
        post.cria_tags(dici_tags, id)
        return {}
    except Exception as e:
        print(e)
        return {"error": "Não foi possivel adicionar post"}

@app.get("/post")
def get_posts():
    post = Post(connection)
    try:
        posts = post.lista()
        if posts:
            return [{"idPost": c[0], "titulo":c[1], "texto":c[2], "url_foto":c[3]} for c in posts]
    except Exception as e:
        return {"error": "Não foi possivel listar posts"}

@app.delete("/post/{post_id}")
def delete_posts(post_id:str):
    post = Post(connection)
    try:
        posts = post.remove(post_id)
    except Exception as e:
        return {"error": f"Não foi possivel deletar post {post_id}"}
    return {}

@app.put("/post/{post_id}")
def update_posts(post_id:str, item: postUpdateObj):
    post = Post(connection)
    try:
        if item.titulo:
            post.muda_titulo(post_id, item.titulo)
        if item.texto:
            dici_tags = post.parser_post(item.texto)
            post.muda_texto(post_id, item.texto)
            post.cria_tags(dici_tags, post_id)
        if item.url_foto:
            post.muda_foto(post_id, item.url_foto)
    except Exception as e:
        return {"error": "Não foi possivel realizar update posts"}
    return {}

@app.get("/post/{post_id}")
def get_posts_id(post_id:str):
    post = Post(connection)
    try:
        p = post.acha_por_id(post_id)
        if p:
            return {"idPost": p[0], "titulo":p[1], "texto":p[2], "url_foto":p[3]} 
    except Exception as e:
        print(e)
        return {"error": "Não foi possivel encontrar posts"}
    return {}

@app.post("/joinha")
def add_joinha(item: joinhaObj):
    joinha = Joinha(connection)
    try:
        joinha.adiciona(item.user_id, item.post_id, item.reacao)
        return {}
    except Exception as e:
        print(e)
        return {"error": "Não foi possivel adicionar joinha"}

@app.put("/joinha")
def update_joinha(item: joinhaObj):
    joinha = Joinha(connection)
    try:
        joinha.muda_reacao(item.user_id, item.post_id, item.reacao)
        return {}
    except Exception as e:
        return {"error": "Não foi possivel adicionar joinha"}

@app.delete("/joinha")
def delete_joinha(item: joinhaUpdateObj):
    joinha = Joinha(connection)
    try:
        joinha.remove(item.user_id, item.post_id)
        return {}
    except Exception as e:
        return {"error": "Não foi possivel remover joinha"}




@app.get("/user/{user_id}/posts")
def get_posts_usuario(user_id: str):
    busca = Busca(connection)
    try:
        return busca.cron_rev(user_id)
    except Exception as e:
        print(e)
        return {"error": "Não foi possivel encontrar posts"}

@app.get("/cidade/pop")
def get_pop_cidade():
    busca = Busca(connection)
    try:
        return busca.pop_cidade()
    except Exception as e:
        print(e)
        return {"error": "Não foi possivel encontrar o mais popular de cada cidade"}

@app.get("/user/{user_id}/ref")
def get_posts_usuario(user_id: str):
    busca = Busca(connection)
    try:
        return busca.ref_usuario(user_id)
    except Exception as e:
        print(e)
        return {"error": f"Não foi possivel encontrar usuarios que referenciam o usuário: {user_id}"}

@app.get("/acesso")
def get_posts_usuario():
    busca = Busca(connection)
    try:
        return busca.tabela_cruz()
    except Exception as e:
        print(e)
        return {"error": f"Não foi possivel encontrar a tabela cruzada"}


@app.get("/passaro/tag/url")
def get_url_passaros():
    busca = Busca(connection)
    try:
        return busca.url_passaro()
    except Exception as e:
        print(e)
        return {"error": f"Não foi possivel encontrar url a partir das tags"}

@app.get("/visualizador/post")
def get_url_passaros():
    busca = Busca(connection)
    try:
        return busca.mais_visualizador()
    except Exception as e:
        print(e)
        return {"error": f"Não foi possivel encontrar o usuário que mais visualiza"}


