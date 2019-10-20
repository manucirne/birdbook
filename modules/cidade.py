import pymysql


class Cidade():
    def __init__(self, conn):
        self.conn = conn

    def adiciona(self, cidade, estado):
        with self.conn.cursor() as cursor:
            cidadeid = None
            try:
                cursor.execute(
                    'INSERT INTO CIDADE (cidade, estado) VALUES (%s, %s);', (cidade, estado))
                self.conn.commit()
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso inserir {cidade} na tabela cidade')

        return cidadeid

    def acha_cidade(self, id):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute('SELECT * FROM CIDADE WHERE idCIDADE=%s', (id))

                res = cursor.fetchAll()
                if res:
                    return res

            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Cidades não podem ser mostradas')
            return None

    def lista(self):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute('SELECT idCIDADE, cidade, estado FROM CIDADE')

                res = cursor.fetchall()
                if res:
                    return res

            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Cidades não podem ser mostradas')
            return None

    def muda_cidade(self, id, nova_cidade, novo_estado):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'UPDATE CIDADE SET cidade=%s, estado=%s WHERE idCIDADE=%s', (nova_cidade, novo_estado, id))
                self.conn.commit()
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Cidade com {id} não encontrado para ser modificado')

    def muda_id(self, id, novo_id):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'UPDATE CIDADE SET idCIDADE=%s WHERE idCIDADE=%s', (novo_id, id))
                self.conn.commit()
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'O id {id} da cidade não pode ser alterado')

    def remove_id(self, id):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'DELETE FROM CIDADE WHERE idCIDADE = (%s)', (id))
                self.conn.commit()
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso deletar o cidade com id = {id} na tabela POST')

    def remove_nome(self, cidade, estado):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'DELETE FROM CIDADE WHERE cidade = (%s) and estado = (%s)', (cidade, estado))
                self.conn.commit()
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso deletar o cidade com nome = {cidade} do estado {estado}na tabela POST')
