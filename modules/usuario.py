import pymysql


class Usuario():
    def __init__(self, conn):
        self.conn = conn

    def adiciona(self, username, email,  nome, idCIDADE):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'INSERT INTO USUARIO (username, email, nome, idCIDADE) VALUES (%s, %s, %s, %s)', (username, email, nome, idCIDADE))
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso inserir {username}, {email}, {nome} e {idCIDADE} na tabela USUARIO')

    def acha(self, username):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'SELECT * FROM USUARIO WHERE username =%s', (username))

                res = cursor.fetchone()
                if res:
                    return res
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Usuário com username = {username} não encontrado na tabela usuário')
            return None

    def lista(self):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute('SELECT * FROM USUARIO')

                res = cursor.fetchall()
                if res:
                    return res
            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Usuários não podem ser mostrados')

            return None

    def muda_nome(self, username, novo_nome):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'UPDATE USUARIO SET nome=%s where username=%s', (novo_nome, username))
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Usuário com username = {username} não encontrado para ser modificado')

    def muda_email(self, username, novo_email):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'UPDATE USUARIO SET email=%s where username=%s', (novo_email, username))
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Usuário com username = {username} não encontrado para ser modificado')

    def muda_cidade(self, username, nova_cidade):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'UPDATE USUARIO SET idCIDADE=%s where username=%s', (nova_cidade, username))
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Usuário com username = {username} não encontrado para ser modificado')

    def remove(self, username):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'DELETE FROM USUARIO WHERE username = %s;', (username))
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso deletar o usuário com username = {username} na tabela usuário')

    def adiciona_pref(self, username, passaro):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'INSERT INTO USUARIO_PREFERE_PASSARO (username, tag_PASSARO) VALUES (%s, %s)', (username, passaro))
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso inserir preferência do usuário: {username} na tabela USUARIO_PREFERE_PASSARO')

    def remove_pref(self, username, passaro):

        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'DELETE USUARIO_PREFERE_PASSARO WHERE username = %s AND tag_PASSARO=%s;', (username, passaro))
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso deletar preferência do usuário: {username} na tabela USUARIO_PREFERE_PASSARO')

    def lista_pref(self, username):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'SELECT username, tag_PASSARO FROM USUARIO_PREFERE_PASSARO WHERE userName=%s;', (username))
                res = cursor.fetchall()
                if res:
                    return res
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso inserir preferência do usuário: {username} na tabela USUARIO_PREFERE_PASSARO')
            return None
