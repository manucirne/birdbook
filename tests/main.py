import subprocess
import os
import unittest

PASSWORD='megadados'

class Test(unittest.TestCase):


    def setUp(self):
        with open(os.path.join(os.path.dirname(__file__), '..','birdbook.sql')) as f:
            res = subprocess.run(f'mysql -u root -p{PASSWORD} -h 0.0.0.0'.split(), stdin=f)
            print(res) 
    
    
    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def tearDown(self):
        print('Terminando...')


if __name__ == '__main__':
    unittest.main()