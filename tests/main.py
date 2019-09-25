import subprocess
import os
import unittest

class TestCase(unittest.TestCase):
    def test_first(self):
        pass

@classmethod
def setup(testCase):
    with open(os.path.join('..', 'birdbook.sql')) as f:
        res = subprocess.run(f'mysql -u root -p{PASSWORD}'.split(), stdin=f)
        print(res) 

if __name__ == '__main__':
    unittest.main()