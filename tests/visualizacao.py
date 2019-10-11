import pymysql


class Visualizacao():
    def __init__(self, conn):
        self.conn = conn

    def adiciona(self, idACESSO, idPOST, username):
        with self.conn.cursor() as cursor:
            visuid = None
            try:
                cursor.execute('INSERT INTO VISUALIZACAO (idACESSO,idPOST,username) VALUES (%s,%s,%s);', (idACESSO, idPOST, username))
                cursor.execute('''
                        SELECT LAST_INSERT_ID()
                            FROM VISUALIZACAO;
                    ''')
                visuid =  cursor.fetchone()[0]

            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Não posso inserir nova visualização')

        return visuid

    def lista_cidade(self):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute('SELECT * FROM CIDADE')
            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Cidades não podem ser mostradas')
            return cursor.fetchmany(100)

    def muda_cidade(self, cidade, nova_cidade):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute('UPDATE CIDADE SET cidade=%s where cidade=%s', (nova_cidade, cidade))
            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Cidade com nome = {cidade} não encontrado para ser modificado')

    def remove(self, cidade):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute('DELETE FROM CIDADE WHERE cidade = (%s)', (cidade))
            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Não posso deletar o cidade com nome = {cidade} na tabela POST')
