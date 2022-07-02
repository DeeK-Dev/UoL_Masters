# Write a while loop that adds all the numbers up to 100 (inclusive).

counter = 0
total = 0
while counter <= 100:
    total += counter
    counter += 1

print(total)

# Using while loop, if statement and str() function;
# iterate through the list and if there is a 100, print it with its index number.
# i.e.: "There is a 100 at index no: 5"

lst = [10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
counter = 0
while counter < len(lst):
    if lst[counter] == 100:
        print(f"There is a 100 at {counter}")
    counter += 1

# Using while loop and an if statement write a function named name_adder
# which appends all the elements in a list to a new list unless the element is an empty string: "".

lst1 = ["Joe", "Sarah", "Mike", "Jess", "", "Matt", "", "Greg"]


def name_adder(list):
    new_list = []
    counter = 0
    while counter < len(list):
        if list[counter] != "":
            new_list.append(list[counter])
        counter += 1
    return new_list


print(name_adder(lst1))

# This time inside a function named name_adder_2,
# write a while loop that stops appending items to the new list as soon as it encounters an empty string: "".
# And prints "There is an empty string and returns the new list."

lst1 = ["Sam", "", "Ben", "Olivia", "Alicia"]


def name_adder_2(list):
    counter = 0
    new_list = []
    while counter < len(lst1):
        if list[counter] != "":
            new_list.append(list[counter])
        else:
            break
        counter += 1
    return new_list

print(name_adder_2(lst1))

