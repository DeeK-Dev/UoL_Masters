"""Compare the performance of recursive versus iterative comparison"""

import time
from data import data_set_1

# Import functions
from floyd_warshall_recursive import solve_paths
from floyd_warshall_iterative import floyd_warshall


def performance_comparison():
    """Calculate the execution time of recursive and
    iterative functions """

    started_at = time.time()
    for x in range(1000):
        solve_paths(data_set_1)
    elapsed_recursive_time = time.time() - started_at

    started_at = time.time()
    for x in range(1000):
        floyd_warshall(data_set_1)
    elapsed_iterative_time = time.time() - started_at

    return elapsed_recursive_time, elapsed_iterative_time


if __name__ == '__main__':
    elapsed_recursive, elapsed_iterative = performance_comparison()

    # Print the comparison between both versions in seconds
    print('Recursive: ', round(elapsed_recursive, 2), 'seconds')
    print('Iterative: ', round(elapsed_iterative, 2), 'seconds')
