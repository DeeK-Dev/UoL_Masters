# Write a map function that adds plus 5 to each item in the list.
lst1 = [10, 20, 30, 40, 50, 60]
lst2 = list(map(lambda x: x+5, lst1))

print(lst2)

# Write a map function that returns the squares of the items in the list.
lst1 = [10, 20, 30, 40, 50, 60]
lst2 = list(map(lambda x: x**2, lst1))

print(lst2)

# Write a map function that adds "Hello, " in front of each item in the list.
lst1 = ["Jane", "Lee", "Will", "Brie"]
lst2 = list(map(lambda x: "Hello, " + x, lst1))

print(lst2)

# Using map() function and len() function create a list that's consisted of lengths of each element in the first list.
lst1 = ["Alpine", "Avalanche", "Powder", "Snowflake", "Summit"]
lst2 = list(map(lambda x: len(x), lst1))
print(lst2)

# Using map() function and lambda add each elements of two lists together. Use a lambda with two arguments.
lst1 = [100, 200, 300, 400, 500]
lst2 = [1, 10, 100, 1000, 10000]
lst3 = list(map(lambda x, y: x + y, lst1, lst2))
print(lst3)

# Using map() function and lambda and count() function create a list
# which consists of the number of occurence of letter: a.
lst1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
lst2 = list(map(lambda x: x.count("a"), lst1))
print(lst2)

# Using map() function and lambda and count() function create a list
# consisted of the number of occurence of both letters: A and a.
lst1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
lst2 = list(map(lambda x: x.lower().count("a"), lst1))

print(lst2)

# Using map() function, first return a new list with absolute values of existing list.
# Then for ans_1, find the total sum of the new list's elements.
lst = [99.3890, -3.5, 5, -0.7123, -9, -0.003]
new_lst = list(map(lambda x: abs(x), lst))
ans_1 = sum(new_lst)

print(ans_1)#