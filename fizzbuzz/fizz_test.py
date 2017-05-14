import unittest
from fizz import fizz

class TestFIZZ(unittest.TestCase):
    def test_fizz3(self):
        self.assertEqual(fizz(3), 'fizz')
    
    def test_fizz4(self):
        self.assertEqual(fizz(4), 4)
    
    def test_fizz5(self):
        self.assertEqual(fizz(5), 'buzz')
        
    def test_fizz15(self):
        self.assertEqual(fizz(15), 'fizzbuzz')
    

if __name__ == '__main__':
    unittest.main()