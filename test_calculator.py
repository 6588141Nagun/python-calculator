import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)  
        self.assertEqual(self.calc.divide(9, 3), 3) 

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1) 
        self.assertEqual(self.calc.modulo(14, 5), 4)  

if __name__ == '__main__':
    unittest.main()