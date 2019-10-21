import pymysql


class Busca():
    def __init__(self, conn):
        self.conn = conn

    def cron_rev(self, username):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'CALL ordena_post_usuario(%s)', (username))
                res = cursor.fetchall()
                if res:
                    return res
            except pymysql.err.IntegrityError as e:
                print(e)
                raise ValueError(
                    f'Não posso encontrar posts do usuário')
        return None


    def pop_cidade(self):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'CALL mais_pop()')
                res = cursor.fetchall()
                if res:
                    return res
            except pymysql.err.IntegrityError as e:
                print(e)
                raise ValueError(
                    f'Não posso encontrar o mais popular da cidade')
        return None
    
    def ref_usuario(self, username):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'CALL referenciam_usu(%s)', (username))
                res = cursor.fetchall()
                if res:
                    return res
            except pymysql.err.IntegrityError as e:
                print(e)
                raise ValueError(
                    f'Não posso encontrar usuários que referenciam ele')
        return None

    def tabela_cruz(self):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'SELECT * FROM aparelho_browser;')
                res = cursor.fetchall()
                if res:
                    return res
            except pymysql.err.IntegrityError as e:
                print(e)
                raise ValueError(
                    f'Não posso encontrar uma tabela cruzada')
        return None

    def url_passaro(self):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'CALL foto_passaro();')
                res = cursor.fetchall()
                if res:
                    return res
            except pymysql.err.IntegrityError as e:
                print(e)
                raise ValueError(
                    f'Não posso encontrar url de fotos de passaros')
        return None

    def mais_visualizador(self):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'CALL mais_visualizador();')
                res = cursor.fetchone()
                if res:
                    return res
            except pymysql.err.IntegrityError as e:
                print(e)
                raise ValueError(
                    f'Não posso encontrar o usuário que mais visualiza')
            return None
    


