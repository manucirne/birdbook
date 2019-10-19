import pymysql


class Acesso():
    def __init__(self, conn):
        self.conn = conn

    def adiciona(self, ip, browser, aparelho):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'INSERT INTO ACESSO (IP, Browser, Aparelho) VALUES (%s,%s,%s);', (ip, browser, aparelho))

                res = cursor.execute('''
                        SELECT LAST_INSERT_ID()
                            FROM ACESSO;
                        ''')

            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso inserir {ip}, {browser}, {aparelho} na tabela ACESSO')

    def acha(self, idACESSO):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'SELECT idACESSO, IP, Browser, Aparelho FROM ACESSO WHERE idACESSO=%s;', (idACESSO))
                res = cursor.fetchone()
                if res:
                    return res

            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso encontrar {idACESSO} na tabela ACESSO')
            return None

    def acha_aparelho(self, aparelho):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'SELECT idACESSO, IP, Browser, Aparelho FROM ACESSO WHERE aparelho=%s;', (aparelho))
                res = cursor.fetchall()
                if res:
                    return res

            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso encontrar {aparelho} na tabela ACESSO')
            return None

    def acha_browser(self, browser):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'SELECT idACESSO, IP, Browser, Aparelho FROM ACESSO WHERE Browser=%s;', (browser))
                res = cursor.fetchall()
                if res:
                    return res

            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso encontrar {browser} na tabela ACESSO')
            return None

    def acha_IP(self, IP):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'SELECT idACESSO, IP, Browser, Aparelho FROM ACESSO WHERE IP=%s;', (IP))
                res = cursor.fetchall()
                if res:
                    return res

            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso encontrar {IP} na tabela ACESSO')
            return None

    def lista(self):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'SELECT idACESSO, IP, Browser, Aparelho FROM ACESSO;')
                res = cursor.fetchall()
                if res:
                    return res

            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso listar a tabela ACESSO')
            return None

    def remove(self, idacesso):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'DELETE FROM ACESSO WHERE idACESSO=%s;', (idacesso))
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso deletar {idacesso} na tabela ACESSO')
