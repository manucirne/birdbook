import pymysql


class Joinha():
    def __init__(self, conn):
        self.conn = conn

    def adiciona(self, username, idPOST, reacao):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'INSERT INTO JOINHA (username, idPOST, reacao) VALUES ( %s,%s, %s);', (username, idPOST, reacao))

            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso inserir {reacao} do usuario {username} em post {idPOST} na tabela JOINHA;')

    def acha_reacao(self, username, idPOST):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'SELECT reacao FROM JOINHA WHERE  idPOST=%s AND username=%s;', (idPOST, username))
                res = cursor.fetchall()
                if res:
                    return res
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso pegar reação do usuario {username} em post {idPOST} da tabela JOINHA;')
            return None

    def muda_reacao(self, username, idPOST, reacao):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'UPDATE JOINHA SET reacao=%s where idPOST=%s AND username=%s', (reacao, idPOST, username))
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Post com idPOST = {idPOST} não pôde ter a reação aterada pelo usuário {username}')

    def remove(self, idPOST, username):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'DELETE FROM JOINHA WHERE username=%s AND idPOST=(%s)', (username, idPOST))
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso deletar a reação com idPOST = {idPOST} e username={username} na tabela JOINHA')
