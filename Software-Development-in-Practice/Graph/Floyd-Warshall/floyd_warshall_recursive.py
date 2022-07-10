"""
Recursive version of the Floyd-Warshall algorithm that finds the shortest path between "i" and "j"
with "k" as the intermediary
"""

from itertools import product


def shortest_path(i, j, k, w):
    """
    Recursive call to shortest_path function
    """

    if k == 0:
        if i == j:
            return 0
        return w[i][j]
    # Recursive call to the function
    return min(shortest_path(i, j, k - 1, w),
               shortest_path(i, k, k - 1, w)
               + shortest_path(k, j, k - 1, w))


def solve_paths(graph):
    """
    Function to convert all values within list "graph" to their corresponding shortest paths and store in "dist"
    """
    # Create new data structure "dist" to store shortest paths, avoid mutating original data structure "graph"
    dist = list(map(lambda p: list(map(lambda q: q, p)), graph))

    for start, end, inter in product(range(len(graph)), repeat=3):
        # Calls the "shortest_path" function for each combination of "start" and "end"
        dist[start][end] = shortest_path(start, end, inter, graph)
    return dist
