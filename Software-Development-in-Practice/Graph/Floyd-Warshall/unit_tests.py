import unittest
from floyd_warshall_recursive import solve_paths
from floyd_warshall_iterative import floyd_warshall
from data import (data_set_1, data_set_2, data_set_3,
                  result_1, result_2, result_3)


class TestSolve(unittest.TestCase):
    def test_list(self):
        """
        Test that data output is correct
        """
        result = solve_paths(data_set_1)
        self.assertEqual(result, result_1, "Not correct")

        result = floyd_warshall(data_set_1)
        self.assertEqual(result, result_1, "Not correct")

        result = solve_paths(data_set_2)
        self.assertEqual(result, result_2, "Not correct")

        result = floyd_warshall(data_set_2)
        self.assertEqual(result, result_2, "Not correct")

        result = solve_paths(data_set_3)
        self.assertEqual(result, result_3, "Not correct")


if __name__ == '__main__':
    unittest.main()
