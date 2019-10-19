import pymysql


class Visualizacao():
    def __init__(self, conn):
        self.conn = conn

    def adiciona(self, idACESSO, idPOST, username):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'INSERT INTO VISUALIZACAO (idACESSO,idPOST,username) VALUES (%s,%s,%s);', (idACESSO, idPOST, username))

            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Não posso inserir nova visualização')

    def acha(self, idACESSO, idPOST, username):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'SELECT idACESSO, idPOST, username, stamp FROM VISUALIZACAO WHERE idACESSO=%s and idPOST=%s and username=%s;', (idACESSO, idPOST, username))
                res = cursor.fetchall()
                if res:
                    return res

            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso encontrar {idACESSO}, {idPOST}, {username} na tabela passaro')

            return None

    def lista(self):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'SELECT * FROM VISUALIZACAO;')
                res = cursor.fetchall()
                if res:
                    return res
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso listar a tabela passaro')
            return None

    # Uma vizualização não pode ser alterada

    def remove(self, idACESSO, idPOST, username):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'DELETE FROM VISUALIZACAO WHERE idACESSO=%s and idPOST=%s and username=%s;', (idACESSO, idPOST, username))

            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso encontrar {idACESSO}, {idPOST}, {username} na tabela passaro')
