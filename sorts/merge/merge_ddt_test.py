import unittest
from merge import sort

try:
    from ddt import ddt, data, unpack
except ImportError:
    print "Install DDT in order to run this test"
    exit(1)
    

@ddt
class TestName(unittest.TestCase):
        @unpack
        @data((
                # kinda randomized numbers, as well as an odd number of elements
                [4, 1, 6, 5, 7, 8, 13, 12, 10, 11, 2, 3, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
                ),
                (
                    # completely backwards list
                    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                ),
                (
                    # repeated elements
                    [5, 5, 5, 5, 5],
                    [5, 5, 5, 5, 5]
                ),
                (
                    # just a single element
                    [1],
                    [1]
                ),
                (
                    # no elements
                    [],
                    []
                )
                )
        def test_sorted(self, first_value, second_value):
            self.assertEqual(sort(first_value), second_value)

            
if __name__ == '__main__':
    unittest.main()