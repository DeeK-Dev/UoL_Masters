# Write a lambda function that takes x as parameter and returns x+2. Then assign it to a variable named L.
i = 6

L = lambda x: x + 2

print(L(i))

# Write a lambda function which takes z as a parameter and returns z*11
# Assign it to variable named: f.

i = 9
f = lambda z: z * 11
print(f(i))

# Write a function which takes two arguments: a and b and returns the multiplication of them:
# a*b. Assign it to a variable named: f.

i, j = 5, 10
f = lambda a, b: a * b

print(f(i, j))

# Using .sort() method, create a lambda function that sorts the list in descending order.
# Refrain from using the reverse parameter.
# (Hint: lambda will be passed to sort method's key parameter as argument)

lst = [100, 10, 10000, 1, 9, 999, 99]
lst.sort(key=lambda x: 100 / x)

print(lst)

# This time use the sorted() function to sort the list in ascending order with lambda.
lst = [100, 10, 10000, 1, 9, 999, 99]
lst = sorted(lst, key=lambda x: x)

print(lst)

# Using sorted() function and lambda sort the words in the list based on their second letter from a to z.
lst = ["otter", "whale", "goose", "chipmunk", "fox", "sheep", "rabbit", "marten"]

lst = sorted(lst, key=lambda x: x[1])
print(lst)

# Using sorted() function and lambda sort the tuples in the list based on the second items.
lst = [(19542209, "New York"), (4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"),
       (1805832, "West Virginia"), (39865590, "California")]
lst = sorted(lst, key=lambda x: x[-1])
print(lst)

# Using sorted() function and lambda sort the tuples in the list based on the last character of the second items.
lst = sorted(lst, key=lambda x: x[1][-1])
print(lst)

# Using sorted() function, reverse parameter and lambda sort the tuples in the list based on the
# last character of the second items in reverse order.
lst = sorted(lst, key=lambda x: x[1][-1], reverse=True)
print(lst)
