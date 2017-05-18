# http://tomlinford.com/post/table-driven-tests/
import unittest
from dictstates import orderStates, alphaStates

class CheckStateTest(unittest.TestCase):
    def test_orderStates(self):
        tests = (
            ('Alaska', 49),
            ('Delaware', 1),
            ('Washington', 42)    
        )
        for state, number in tests:
            # have to subtract one to account for 0vs1 indexing
            self.assertEqual(orderStates('states.csv')[number-1], state)
    
    def test_alphaStates(self):
        tests = (
            ('Alabama', 0),
            ('Wyoming', 49),
            ('Wyoming', -1)   
        )
        for state, number in tests:
            self.assertEqual(alphaStates('states.csv')[number], state)
            
if __name__ == '__main__':
    unittest.main()