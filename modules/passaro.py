import pymysql


class Passaro():
    def __init__(self, conn):
        self.conn = conn

    def adiciona(self, tag, especie, nome_pop):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'INSERT INTO PASSARO (tag_PASSARO, especie, nome_popular) VALUES (%s,%s,%s);', (tag, especie, nome_pop))
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso inserir {tag}, {especie}, {nome_pop} na tabela passaro')

    def acha(self, tag):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'SELECT * FROM PASSARO WHERE tag_PASSARO=%s;', (tag))
                res = cursor.fetchone()
                if res:
                    return res

            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso encontrar {tag} na tabela passaro')
            return None

    def acha_especie(self, especie):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'SELECT * FROM PASSARO WHERE especie=%s;', (especie))
                res = cursor.fetchone()
                if res:
                    return res

                else:
                    return None
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso encontrar {especie} na tabela passaro')

    def acha_pop(self, nome_pop):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'SELECT * FROM PASSARO WHERE nome_popular=%s;', (nome_pop))
                res = cursor.fetchone()
                if res:
                    return res

                else:
                    return None
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso encontrar {nome_pop} na tabela passaro')

    def lista(self):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'SELECT * FROM PASSARO;')
                res = cursor.fetchall()
                if res:
                    return res

            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso listar a tabela passaro')
            return None

    def atualiza(self, tag, especie, nome_pop):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'UPDATE PASSARO SET especie=%s, nome_popular=%s WHERE tag_PASSARO=%s;', (especie, nome_pop, tag))
                res = cursor.fetchone()
                if res:
                    return res[0]
                else:
                    return None
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso encontrar {tag} na tabela passaro')

    def remove(self, tag):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'DELETE FROM PASSARO WHERE tag_PASSARO=%s;', (tag))
            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Não posso deletar {tag} na tabela passaro')
