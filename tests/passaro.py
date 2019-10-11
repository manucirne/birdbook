import pymysql


class Passaro():
    def __init__(self, conn):
        self.conn = conn

    def adiona(self, nome):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute('INSERT INTO perigo (nome) VALUES (%s)', (nome))
            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Não posso inserir {nome} na tabela perigo')

    def acha(self, tag):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute('INSERT INTO perigo (nome) VALUES (%s)', (nome))
            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Não posso inserir {nome} na tabela perigo')

    def remove(self, tag):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute('INSERT INTO perigo (nome) VALUES (%s)', (nome))
            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Não posso inserir {nome} na tabela perigo')
