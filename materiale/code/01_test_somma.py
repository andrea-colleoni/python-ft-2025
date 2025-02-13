import unittest
from calcoli import somma

class TestSomma(unittest.TestCase):

    def test_somma_interi_positivi(self):
        self.assertEqual(somma(3, 6), 9)

    def test_somma_interi_negativi(self):
        self.assertEqual(somma(-3, -2), -5)

if __name__ == '__main__':
    unittest.main()