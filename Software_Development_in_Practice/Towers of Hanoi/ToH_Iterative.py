import timeit
# Python3 program for iterative Tower of Hanoi
setup = 'import sys'
code = '''
# A structure to represent a stack
class Stack:
    # Constructor to set the data of
    # the newly created tree node
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.array = [0] * capacity


# function to create a stack of given capacity.
def create_stack(capacity):
    stack = Stack(capacity)
    return stack


# Stack is full when top is equal to the last index
def is_full(stack):
    return stack.top == (stack.capacity - 1)


# Stack is empty when top is equal to -1
def is_empty(stack):
    return stack.top == -1


# Function to add an item to stack.
# It increases top by 1
def push(stack, item):
    if is_full(stack):
        return
    stack.top += 1
    stack.array[stack.top] = item


# Function to remove an item from stack.
# It decreases top by 1
def pop(stack):
    if is_empty(stack):
        return -sys.maxsize
    top = stack.top
    stack.top -= 1
    return stack.array[top]

# Function to implement legal
# movement between two poles
def move_disks_between_two_poles(src,
                                 dest,
                                 s,
                                 d
                                 ):
    pole1_top_disk = pop(src)
    pole2_top_disk = pop(dest)

    # When pole 1 is empty
    if pole1_top_disk == -sys.maxsize:
        push(src, pole2_top_disk)
        move_disk(d, s, pole2_top_disk)

    # When pole2 pole is empty
    elif pole2_top_disk == -sys.maxsize:
        push(dest, pole1_top_disk)
        move_disk(s, d, pole1_top_disk)

    # When top disk of pole1 > top disk of pole2
    elif pole1_top_disk > pole2_top_disk:
        push(src, pole1_top_disk)
        push(src, pole2_top_disk)
        move_disk(d, s, pole2_top_disk)

    # When top disk of pole1 < top disk of pole2
    else:
        push(dest, pole2_top_disk)
        push(dest, pole1_top_disk)
        move_disk(s, d, pole1_top_disk)


# Function to show the movement of disks
def move_disk(from_peg, to_peg, disk):
    print("Move the disk", disk, "from '", from_peg, "' to '", to_peg, "'")


# Function to implement TOH puzzle
def toh_iterative(num_of_disks, src, aux, dest):
    s, d, a = 'S', 'D', 'A'

    # If number of disks is even, then interchange
    # destination pole and auxiliary pole
    if num_of_disks % 2 == 0:
        temp = d
        d = a
        a = temp
    total_num_of_moves = int(pow(2, num_of_disks) - 1)

    # Larger disks will be pushed first
    for i in range(num_of_disks, 0, -1):
        push(src, i)

    for i in range(1, total_num_of_moves + 1):
        if i % 3 == 1:
            move_disks_between_two_poles(src, dest, s, d)

        elif i % 3 == 2:
            move_disks_between_two_poles(src, aux, s, a)

        elif i % 3 == 0:
            move_disks_between_two_poles(aux, dest, a, d)


# Input: number of disks
num_of_disks = 3

# Create three stacks of size 'num_of_disks'
# to hold the disks
src = create_stack(num_of_disks)
dest = create_stack(num_of_disks)
aux = create_stack(num_of_disks)

toh_iterative(num_of_disks, src, aux, dest)

'''

print(timeit.timeit(setup=setup,
                    stmt=code,
                    number=1)
                    )