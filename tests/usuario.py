import pymysql


class Usuario():
    def __init__(self, conn):
        self.conn = conn

    def adiciona(self, username, email,  nome, idCIDADE):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute('INSERT INTO USUARIO (username, email, nome, idCIDADE) VALUES (%s, %s, %s, %s)', (username, email, nome, idCIDADE))
            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Não posso inserir {username}, {email}, {nome} e {idCIDADE} na tabela USUARIO')

    def acha(self, username):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute('SELECT nome, idCIDADE, email FROM USUARIO WHERE username = (%s)', (username))
            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Usuário com username = {username} não encontrado na tabela usuário')

    def lista_usuarios(self):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute('SELECT * FROM USUARIO')
            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Usuários não podem ser mostrados')

    def muda_nome(self, username, novo_nome):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute('UPDATE USUARIO SET nome=%s where username=%s', (novo_nome, username))
            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Usuário com username = {username} não encontrado para ser modificado')

    def muda_email(self, username, novo_email):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute('UPDATE USUARIO SET email=%s where username=%s', (novo_email, username))
            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Usuário com username = {username} não encontrado para ser modificado')

    def muda_cidade(self, username, nova_cidade):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute('UPDATE USUARIO SET idCIDADE=%s where username=%s', (nova_cidade, username))
            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Usuário com username = {username} não encontrado para ser modificado')

    
    def remove(self, username):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute('DELETE FROM USUARIO WHERE username = (%s)', (username))
            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Não posso deletar o usuário com username = {username} na tabela usuário')