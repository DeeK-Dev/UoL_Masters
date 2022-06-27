# Recursive Python function to solve tower of hanoi
import timeit
mycode = '''
def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    tower_of_hanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    tower_of_hanoi(n - 1, aux_rod, to_rod, from_rod)

n = 20
tower_of_hanoi(n, "A", "B", "C")
# A, C, B are the name of rods
'''

print(timeit.timeit(stmt=mycode,
                    number=1)
      )

