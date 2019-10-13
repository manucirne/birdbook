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
