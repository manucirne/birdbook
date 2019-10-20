import pymysql


class Post():
    def __init__(self, conn):
        self.conn = conn

    def parser_post(self, texto):
        lista_texto = texto.split(' ')
        lista_passaros = []
        lista_citados = []
        for item in lista_texto:
            if item[0] == '#':
                lista_passaros.append(item[1:])
            if item[0] == '@':
                lista_citados.append(item[1:])
        return {"#": lista_passaros, "@": lista_citados}

    def adiciona(self, username, titulo, texto, URL_foto):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'INSERT INTO POST (titulo, texto, URL_foto, username) VALUES ( %s,%s, %s, %s);', (titulo, texto, URL_foto, username))

                cursor.execute('SELECT LAST_INSERT_ID()')
                res = cursor.fetchone()
                if res:
                    return res
                #self.conn.commit()
                
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso inserir {titulo}, {texto} e {URL_foto} na tabela POST;')
            return None
    def acha_por_id(self, idPOST):
        with self.conn.cursor() as cursor:
            try:
                res = cursor.execute(
                    'SELECT idPOST, titulo, texto, URL_foto, username FROM POST WHERE idPOST = (%s) AND deleta = False;', (idPOST))

                res = cursor.fetchone()
                if res:
                    return res

            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Post não encontrado')
            return None

    def lista(self):
        with self.conn.cursor() as cursor:
            try:
                res = cursor.execute(
                    'SELECT idPOST, titulo, texto, URL_foto, username FROM POST WHERE deleta = False;')

                res = cursor.fetchall()
                if res:
                    return res
            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Posts não podem ser mostrados')
            return None

    def muda_titulo(self, idPOST, novo_titulo):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'UPDATE POST SET titulo=%s where idPOST=%s', (novo_titulo, idPOST))
                #self.conn.commit()
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Post com idPOST = {idPOST} não encontrado para ser modificado')

    def muda_texto(self, idPOST, novo_texto):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'UPDATE POST SET texto=%s where idPOST=%s', (novo_texto, idPOST))
                #self.conn.commit()
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'POST com idPOST = {idPOST} não encontrado para ser modificado')

    def muda_foto(self, idPOST, nova_foto):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'UPDATE POST SET URL_foto=%s where idPOST=%s', (nova_foto, idPOST))
                #self.conn.commit()
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'POST com idPOST = {idPOST} não encontrado para ser modificado')

    def remove(self, idPOST):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    'UPDATE POST SET deleta=1 where idPOST=(%s)', (idPOST))
                #self.conn.commit()
            except pymysql.err.IntegrityError as e:
                raise ValueError(
                    f'Não posso deletar o post com idPOST = {idPOST} na tabela POST')

    def cria_tags(self, dici_tags, id_post):
        resp = {}
        resp_pes = {}
        with self.conn.cursor() as cursor:
            try:
                if '#' in dici_tags:
                    for item in dici_tags["#"]:
                        resp[item] = 0
                    for item in dici_tags["#"]:
                        print(item)
                        cursor.execute('''
                            SELECT COUNT(tag_PASSARO) FROM PASSARO
                            WHERE tag_PASSARO = %s; 
                        ''', (item))
                        resp[item] += cursor.fetchone()[0]
                    for pas in resp:
                        if resp[pas] > 0:
                            cursor.execute('''
                            INSERT INTO TAG_PASSARO_POST (idPost,tag_PASSARO)
                            VALUES(%s,%s)
                            ''', (id_post, pas))

                if '@' in dici_tags:
                    for item in dici_tags["@"]:
                        resp_pes[item] = 0
                    for item in dici_tags["@"]:
                        print(item)
                        cursor.execute('''
                            SELECT COUNT(username) FROM USUARIO
                            WHERE username = %s; 
                        ''', (item))
                        resp_pes[item] += cursor.fetchone()[0]
                    for usu in resp_pes:
                        if resp_pes[usu] > 0:
                            cursor.execute('''
                            INSERT INTO TAG_USUARIO_POST (idPost,username)
                            VALUES(%s,%s)
                            ''', (id_post, usu))
                #self.conn.commit()
            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Não foi possível criar as tags')

    def lista_tags_passaro(self):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute('''
                        SELECT tag_PASSARO FROM TAG_PASSARO_POST;''')
                res = cursor.fetchall()
                if res:
                    return res
            except:
                raise ValueError(
                    f'Não foi possível listar as tags de TAG_PASSARO_POST')
            return None

    def lista_tags_usuario(self):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute('''
                        SELECT username FROM TAG_USUARIO_POST;''')
                res = cursor.fetchall()
                if res:
                    return res
            except:
                raise ValueError(
                    f'Não foi possível listar as tags de TAG_USUARIO_POST')
            return None

    def acha_tags_por_PK_passaro(self, idPOST):
        with self.conn.cursor() as cursor:
            try:
                res = cursor.execute(
                    'SELECT tagPASSARO FROM TAG_PASSARO_POST WHERE idPOST = (%s);', (idPOST))

                res = cursor.fetchone()
                if res:
                    return res

            except pymysql.err.IntegrityError as e:
                raise ValueError(f'tag não encontrada')
            return None

    def acha_tags_por_PK_usuario(self, idPOST):
        with self.conn.cursor() as cursor:
            try:
                res = cursor.execute(
                    'SELECT username FROM TAG_USUARIO_POST WHERE idPOST = (%s);', (idPOST))

                res = cursor.fetchone()
                if res:
                    return res

            except pymysql.err.IntegrityError as e:
                raise ValueError(f'tag não encontrada')
            return None
