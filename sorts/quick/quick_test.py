import unittest
from quick import sort

class CheckStateTest(unittest.TestCase):
    def test_sort(self):
        tests = (
            (
                (4, 1, 6, 5, 7, 8, 14, 13, 12, 10, 11, 2, 3, 9),
                (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
            ),
            (
                (10, 9, 8, 7, 6, 5, 4, 3, 2, 1),
                (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
            ),
            (
                (1),
                (1)
            )
        )
        for notSorted, nowSorted in tests:
            self.assertEqual(sort(notSorted), nowSorted)

            
if __name__ == '__main__':
    unittest.main()