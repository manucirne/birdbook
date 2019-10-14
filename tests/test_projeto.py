import io
import json
import logging
import os
import os.path
import re
import subprocess
import unittest
import pymysql

from passaro import Passaro
from post import Post
from usuario import Usuario
from cidade import Cidade
from visualizacao import Visualizacao


class TestProjeto(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global config
        cls.connection = pymysql.connect(
            host=config['HOST'],
            user=config['USER'],
            password=config['PASS'],
            database='birdbook'
        )

    @classmethod
    def tearDownClass(cls):
        cls.connection.close()

    def setUp(self):
        conn = self.__class__.connection
        with conn.cursor() as cursor:
            cursor.execute('START TRANSACTION')

    def tearDown(self):
        conn = self.__class__.connection
        with conn.cursor() as cursor:
            cursor.execute('ROLLBACK')

    def test_adiciona_passaro(self):
        oldPas = ('Bentivinus Bolotoide',  'Bem-te-vi', 'Passarinho')
        conn = self.__class__.connection
        pas = Passaro(conn)

        pas.adiciona(*oldPas)

        # tenta adicionar duas vezes o passaro
        try:
            pas.adiciona(*oldPas)
            self.fail(
                'Nao deveria ter adicionado o mesmo passaro duas vezes.')
        except ValueError as e:
            pass

        id = pas.acha(oldPas[0])
        self.assertIsNotNone(id)

        # Tenta achar um perigo inexistente.
        id = pas.acha('Bentivinus NonExistum')
        self.assertIsNone(id)

    def test_remove_passaro(self):
        oldPas = ('Bentivinus Bolotoide',  'Bem-te-vi', 'Passarinho')
        conn = self.__class__.connection
        pas = Passaro(conn)

        pas.adiciona(*oldPas)

        id = pas.acha(oldPas[0])

        res = pas.lista()
        self.assertCountEqual(res, (id,))

        pas.remove(oldPas[0])

        res = pas.lista()
        self.assertFalse(res)

    def test_update_passaro(self):
        newPas = ('Bentivinus Bolotoide',  'Bem-não-te-viu', 'Passarinho')
        oldPas = ('Bentivinus Bolotoide',  'Bem-te-vi', 'Passarinho')
        conn = self.__class__.connection
        pas = Passaro(conn)

        pas.adiciona(*oldPas)
        pas.atualiza(*newPas)
        res = pas.lista()

        self.assertSequenceEqual(res, (newPas,))

        pas.remove('Bentivinus Bolotoide')

        res = pas.lista()
        self.assertFalse(res)

    # @unittest.skip('Em desenvolvimento.')
    def test_lista_passaros(self):
        conn = self.__class__.connection
        pas = Passaro(conn)
        allPas = [
            ('Bentivinus Bolotoide',  'Bem-não-te-viu', 'Passarinho'),
            ('Quero Queroides',  'QueroQuerQuero', 'Monstrinho')
        ]
        # Verifica que ainda não tem pássaros no sistema.
        res = pas.lista()
        self.assertFalse(res)

        # Adiciona alguns perigos.
        passaros_id = []
        for p in allPas:
            pas.adiciona(*p)
            passaros_id.append(pas.acha(p[0]))

        # Verifica se os perigos foram adicionados corretamente.
        res = pas.lista()
        self.assertCountEqual(res, passaros_id)

        # Remove os perigos.
        for p in passaros_id:
            pas.remove(p[0])

        # Verifica que todos os perigos foram removidos.
        res = pas.lista()
        self.assertFalse(res)

    def test_adiciona_usuario(self):

        conn = self.__class__.connection
        cid = Cidade(conn)
        user = Usuario(conn)

        # Pega todas as cidades
        cids = cid.lista()
        oldUser = ('david', "david@passaros.com",
                   "David Fogelman", cids[0][0])

        user.adiciona(*oldUser)

        # tenta adicionar duas vezes o passaro
        try:
            user.adiciona(*oldUser)
            self.fail(
                'Nao deveria ter adicionado o mesmo passaro duas vezes.')
        except ValueError as e:
            pass

        id = user.acha(oldUser[0])
        self.assertIsNotNone(id)

        # Tenta achar um perigo inexistente.
        id = user.acha('Usuarium NonExistum')
        self.assertIsNone(id)

    def test_remove_usuario(self):

        conn = self.__class__.connection
        cid = Cidade(conn)
        user = Usuario(conn)

        # Pega todas as cidades
        cids = cid.lista()
        oldUser = ('david', "david@passaros.com",
                   "David Fogelman", cids[0][0])

        user.adiciona(*oldUser)

        id = user.acha(oldUser[0])
        self.assertIsNotNone(id)

        # Tenta achar um perigo inexistente.
        res = user.lista()
        self.assertCountEqual(res, (id,))

        user.remove(oldUser[0])

        res = user.lista()
        self.assertFalse(res)

    def test_update_usuario(self):

        conn = self.__class__.connection
        cid = Cidade(conn)
        user = Usuario(conn)

        # Pega todas as cidades
        cids = cid.lista()
        oldUser = ('david', "david@passaros.com",
                   "David Fogelman", cids[0][0])
        newUser = ('david', "david@passaros.com",
                   "David Pasaro", cids[0][0])

        user.adiciona(*oldUser)
        user.muda_email(newUser[0], newUser[1])
        user.muda_nome(newUser[0], newUser[2])
        user.muda_cidade(newUser[0], newUser[3])
        res = user.lista()

        self.assertSequenceEqual(res, (newUser,))

        user.remove(newUser[0])

        res = user.lista()
        self.assertFalse(res)

    # @unittest.skip('Em desenvolvimento.')
    def test_lista_usuarios(self):
        conn = self.__class__.connection
        cid = Cidade(conn)
        user = Usuario(conn)
        # Pega todas as cidades
        cids = cid.lista()

        allUsers = [('david', "david@passaros.com",
                     "David Fogelman", cids[0][0]),
                    ('david alias', "david@passaritos.com",
                     "David Pasaro", cids[0][0])
                    ]
        # Verifica que ainda não tem pássaros no sistema.
        res = user.lista()
        self.assertFalse(res)

        # Adiciona alguns perigos.
        users_id = []
        for u in allUsers:
            user.adiciona(*u)
            users_id.append(user.acha(u[0]))

        # Verifica se os perigos foram adicionados corretamente.
        res = user.lista()
        self.assertCountEqual(res, (users_id))

        # Remove os perigos.
        for u in users_id:
            user.remove(u[0])

        # Verifica que todos os perigos foram removidos.
        res = user.lista()
        self.assertFalse(res)

    # @unittest.skip('Em desenvolvimento.')
    def test_usuario_prefe_passaro(self):
        conn = self.__class__.connection
        pas = Passaro(conn)
        cid = Cidade(conn)
        user = Usuario(conn)

        # Pega todas as cidades
        cids = cid.lista()
        oldPas = ('Bentivinus Bolotoide',  'Bem-te-vi', 'Passarinho')
        oldUser = ('david', "david@passaros.com",
                   "David Fogelman", cids[0][0])

        oldPref = (oldUser[0], oldPas[0])

        user.adiciona(*oldUser)
        res = user.acha(oldUser[0])
        self.assertSequenceEqual(res, oldUser)

        pas.adiciona(*oldPas)
        res = pas.lista()
        self.assertCountEqual(res, (oldPas,))

        res = user.lista_pref(oldUser[0])
        self.assertFalse(res)

        user.adiciona_pref(*oldPref)
        res = user.lista_pref(oldUser[0])
        self.assertIsNotNone(res)
        self.assertSequenceEqual(res, (oldPref,))

    def test_usuario_remove_preferencia_passaro(self):
        conn = self.__class__.connection
        pas = Passaro(conn)
        cid = Cidade(conn)
        user = Usuario(conn)

        # Pega todas as cidades
        cids = cid.lista()
        oldPas = ('Bentivinus Bolotoide',  'Bem-te-vi', 'Passarinho')
        oldUser = ('david', "david@passaros.com",
                   "David Fogelman", cids[0][0])

        oldPref = (oldUser[0], oldPas[0])

        user.adiciona(*oldUser)
        res = user.acha(oldUser[0])
        self.assertSequenceEqual(res, oldUser)

        pas.adiciona(*oldPas)
        res = pas.lista()
        self.assertCountEqual(res, (oldPas,))

        res = user.lista_pref(oldUser[0])
        self.assertFalse(res)

        user.adiciona_pref(*oldPref)
        res = user.lista_pref(oldUser[0])
        self.assertIsNotNone(res)
        self.assertSequenceEqual(res, (oldPref,))

    def test_adiciona_post(self):
        conn = self.__class__.connection
        pst = Post(conn)
        pas = Passaro(conn)
        cid = Cidade(conn)
        user = Usuario(conn)

        # Pega todas as cidades
        cids = cid.lista()

        oldPst = ('Um novo passaro',
                  'Encontrei um passaro novo na minha caminhada', 'https://passarito.com')
        oldUser = ('david', "david@passaros.com",
                   "David Fogelman", cids[0][0])

        user.adiciona(*oldUser)
        res = user.acha(oldUser[0])
        self.assertSequenceEqual(res, oldUser)

        id = res[0]
        pst.adiciona(id, *oldPst)

        psts = pst.lista()
        self.assertTrue(any(elem in psts[0] for elem in oldPst))

        res = pst.acha_por_id(psts[0][0])
        self.assertSequenceEqual(res, psts[0])

        idPost = psts[0][0]

        pst.remove(idPost)
        res = pst.lista()
        self.assertFalse(res)

    def test_remove_post(self):
        conn = self.__class__.connection
        pst = Post(conn)
        cid = Cidade(conn)
        user = Usuario(conn)

        # Pega todas as cidades
        cids = cid.lista()

        oldPst = ('Um novo passaro',
                  'Encontrei um passaro novo na minha caminhada', 'https://passarito.com')
        oldUser = ('david', "david@passaros.com",
                   "David Fogelman", cids[0][0])

        user.adiciona(*oldUser)
        res = user.acha(oldUser[0])

        id = res[0]
        pst.adiciona(id, *oldPst)

        res = pst.lista()
        idPost = res[0][0]

        pst.remove(idPost)
        res = pst.lista()
        self.assertIsNone(res)

    def test_update_post(self):
        conn = self.__class__.connection
        pst = Post(conn)
        cid = Cidade(conn)
        user = Usuario(conn)

        # Pega todas as cidades
        cids = cid.lista()

        oldPst = ('Um novo passaro',
                  'Encontrei um passaro novo na minha caminhada', 'https://passarito.com')

        newPst = ('Um novo passaro inédito',
                  'Encontrei um pássaro inédito no meu cooper matinal', 'https://pterodactilo.com')
        oldUser = ('david', "david@passaros.com",
                   "David Fogelman", cids[0][0])

        user.adiciona(*oldUser)
        res = user.acha(oldUser[0])

        id = res[0]
        pst.adiciona(id, *oldPst)

        psts = pst.lista()
        idPost = psts[0][0]

        pst.muda_titulo(idPost, newPst[0])
        pst.muda_texto(idPost, newPst[1])
        pst.muda_foto(idPost, newPst[2])

        res = pst.acha_por_id(idPost)

        self.assertTrue(any(elem in res for elem in newPst))

        res = pst.lista()

        pst.remove(idPost)
        res = pst.lista()
        self.assertIsNone(res)

    def test_lista_posts(self):
        conn = self.__class__.connection
        pst = Post(conn)
        cid = Cidade(conn)
        user = Usuario(conn)

        # Pega todas as cidades
        cids = cid.lista()

        psts = [('Um novo passaro',
                 'Encontrei um passaro novo na minha caminhada', 'https://passarito.com'),
                ('Um novo passaro inédito',
                 'Encontrei um pássaro inédito no meu cooper matinal', 'https://pterodactilo.com')]
        oldUser = ('david', "david@passaros.com",
                   "David Fogelman", cids[0][0])

        user.adiciona(*oldUser)
        res = user.acha(oldUser[0])
        id = res[0]
        for p in psts:
            pst.adiciona(id, *p)

        res = pst.lista()
        posts_id = [p[0] for p in res]

        self.assertEqual(len(posts_id), len(psts))

        for p in posts_id:
            pst.remove(p)

        # Verifica que todos os perigos foram removidos.
        res = pst.lista()
        self.assertFalse(res)


def run_sql_script(filename):
    global config
    with open(filename, 'rb') as f:
        subprocess.run(
            [
                config['MYSQL'],
                '-u', config['USER'],
                '-p' + config['PASS'],
                '-h', config['HOST']
            ],
            stdin=f
        )


def setUpModule():
    filenames = [entry for entry in os.listdir()
                 if os.path.isfile(entry) and re.match(r'.*_\d{3}\.sql', entry)]
    for filename in filenames:
        run_sql_script(filename)


def tearDownModule():
    run_sql_script('tear_down.sql')


if __name__ == '__main__':
    global config
    with open('config_tests.json', 'r') as f:
        config = json.load(f)
    logging.basicConfig(filename=config['LOGFILE'], level=logging.DEBUG)
    unittest.main(verbosity=2)
