import pymysql


class Post():
    def __init__(self, conn):
        self.conn = conn

    def parser_post(self,texto):
        lista_texto = texto.split(' ')
        lista_passaros = []
        lista_citados = []
        for item in lista_texto:
            if item[0] == '#':
                lista_passaros.append(item[1:])
            if item[0] == '@':
                lista_citados.append(item[1:])
        return {"#": lista_passaros, "@": lista_citados}
        
    def adiciona(self, titulo, texto, URL_foto):
        with self.conn.cursor() as cursor:
            idPOST = None
            try:
                cursor.execute('INSERT INTO POST (titulo, texto, URL_foto) VALUES (%s, %s, %s, %s);', (titulo, texto, URL_foto))
                cursor.execute('''
                        SELECT LAST_INSERT_ID()
                            FROM POST;
                    ''')
                idPOST =  cursor.fetchone()[0]

            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Não posso inserir {titulo}, {texto} e {URL_foto} na tabela POST')

            return idPOST

    def acha_por_id(self, idPOST):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute('SELECT titulo, texto, URL_foto FROM POST WHERE idPOST = (%s) AND deleta = False', (idPOST))
            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Post não encontrado')

    def lista_usuarios(self):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute('SELECT * FROM USUARIO')
            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Usuários não podem ser mostrados')

    def muda_nome(self, username, novo_nome):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute('UPDATE USUARIO SET nome=%s where username=%s', (novo_nome, username))
            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Usuário com username = {username} não encontrado para ser modificado')

    def muda_email(self, username, novo_email):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute('UPDATE USUARIO SET email=%s where username=%s', (novo_email, username))
            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Usuário com username = {username} não encontrado para ser modificado')

    def muda_cidade(self, username, nova_cidade):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute('UPDATE USUARIO SET idCIDADE=%s where username=%s', (nova_cidade, username))
            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Usuário com username = {username} não encontrado para ser modificado')

    
    def remove(self, username):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute('DELETE FROM USUARIO WHERE username = (%s)', (username))
            except pymysql.err.IntegrityError as e:
                raise ValueError(f'Não posso deletar o usuário com username = {username} na tabela usuário')

    def cria_tags(self,dici_tags, id_post):
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
                        ''',(item))
                        resp[item] += cursor.fetchone()[0]
                    for pas in resp:
                        if resp[pas] > 0:
                            cursor.execute('''
                            INSERT INTO TAG_PASSARO_POST (idPost,tag_PASSARO)
                            VALUES(%s,%s)
                            ''',(id_post,pas))
                            
                if '@' in dici_tags:
                    for item in dici_tags["@"]:
                        resp_pes[item] = 0
                    for item in dici_tags["@"]:
                        print(item)
                        cursor.execute('''
                            SELECT COUNT(username) FROM USUARIO
                            WHERE username = %s; 
                        ''',(item))
                        resp_pes[item] += cursor.fetchone()[0]
                    for usu in resp_pes:
                        if resp_pes[usu] > 0:
                            cursor.execute('''
                            INSERT INTO TAG_USUARIO_POST (idPost,username)
                            VALUES(%s,%s)
                            ''',(id_post,usu))
            except pymysql.err.IntegrityError as e:  
                raise ValueError(f'Não foi possível criar as tags')     