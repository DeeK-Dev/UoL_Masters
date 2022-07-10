"""
Iterative version of the Floyd-Warshall algorithm that finds all paths between selected edges.
"""

# Number of vertices
nbr_vert = 4
inf = 999


# Algorithm
def floyd_iterative(graph):
    dist = list(map(lambda p: list(map(lambda q: q, p)), graph))

    # Adding vertices individually
    for r in range(nbr_vert):
        for p in range(nbr_vert):
            for q in range(nbr_vert):
                dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])




# Driver program to test the above program
# Let us create the following weighted graph
"""
            10
       (0)------->(3)
        |         /|\
      5 |          |
        |          | 1
       \|/         |
       (1)------->(2)
            3           
"""
