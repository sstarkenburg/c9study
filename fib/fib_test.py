import unittest
from fib import fib

class TestFIB(unittest.TestCase):
    def test_fib0(self):
        self.assertEqual(fib(0), 0)
    
    def test_fib4(self):
        self.assertEqual(fib(4), 3)
    
    def test_fib6(self):
        self.assertEqual(fib(6), 8)
    
    def test_fib8(self):
        self.assertEqual(fib(8), 21)
    
    def test_fib10(self):
        self.assertEqual(fib(10), 55)
    
    def test_fib12(self):
        self.assertEqual(fib(12), 144)

if __name__ == '__main__':
    unittest.main()