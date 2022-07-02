# Write a for loop so that every item in the list is printed.

lst = ["koala", "cat", "fox", "panda", "chipmunk", "sloth", "penguin", "dolphin"]
for i in lst:
    print(i)

# Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Sam"
lst = ["Sam", "Lisa", "Micha", "Dave", "Wyatt", "Emma", "Sage"]
for i in lst:
    print(f"Hello {i}")

# Write a for loop that iterates through a string and prints every letter.
str = "Antarctica"
for i in range(len(str)):
    print(str[i])

# Type a code inside the for loop so that counter variable named c is increased by one each time loop iterates.
# Can you guess how many times it will add 1?.
str = "Civilization"
c = 0
for i in str:
    c += 1

print(c)

# Using a for loop and .append() method append each item with a Dr. prefix to the lst.
lst1 = ["Phil", "Oz", "Seuss", "Dre"]
lst2 = []
for i in lst1:
    lst2.append("Dr. " + i)

print(lst2)

# Write a for loop which appends the square of each number to the new list.
lst1 = [3, 7, 6, 8, 9, 11, 15, 25]
lst2 = []
for i in lst1:
    lst2.append(i**2)


print(lst2)

# Write a for loop using an if statement, that appends each number to the new list if it's positive.
lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
lst2 = []
for i in lst1:
    if i > 0:
        lst2.append(i)


print(lst2)

# Using for loop and if statement,
# append the value minus 1000 for each key to the new list if the value is above 1000.
# i.e.: if the value is 1500, 500 should be added to the new list.

dict = {"z1":900, "t1": 1100, "p1": 2300, "r1": 1050, "k1": 3200, "g1": 400}
lst = []
for i in dict:
    if dict[i] > 1000:
        lst.append(dict[i]-1000)

print(lst)

# Write a for loop which appends the type of each element in the first list to the second list.
lst1 = [3.14, 66, "Teddy Bear", True, [], {}]
lst2 = []
for i in lst1:
    lst2.append(type(i))

print(lst2)