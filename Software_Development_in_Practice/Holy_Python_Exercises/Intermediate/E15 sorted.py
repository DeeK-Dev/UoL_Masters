# Using sorted() function, sort the list in ascending order.
lst1 = [500, 1000, 400, 40000, 999, 2, 0.5, 17]
lst2 = sorted(lst1)

print(lst2)

# Using sorted() function, sort the list from a to z.
lst1 = ["zebra", "bird", "ant", "porcupine", "giraffe"]
lst2 = sorted(lst1)

print(lst2)

# Using sorted() function sort the list from z to a.
lst1 = ["zebra", "bird", "ant", "porcupine", "giraffe"]
lst2 = sorted(lst1, reverse=True)

print(lst2)

# Using sorted() function sort the list in descending order.
lst1 = [500, 1000, 400, 40000, 999, 2, 0.5, 17]
lst2 = sorted(lst1, reverse=True)

print(lst2)

# Using len function and sorted() function, sort the list based on the length of the strings (In ascending order).

lakes1 = ["Malawi", "Medicine", "Tahoe", "Moraine", "Upper Arrow", "Plitvice", "Edith", "Emerald"]
lakes2 = sorted(lakes1, key=len)

print(lakes2)

# Using len function and sorted() function, sort the list based on the length of the strings
# this time in descending order.
lakes1 = ["Malawi", "Medicine", "Tahoe", "Moraine", "Upper Arrow", "Plitvice", "Edith", "Emerald"]
lakes2 = sorted(lakes1, key=len, reverse=True)

print(lakes2)

# Using lambda and sorted() function, sort the list based on last characters of the items from z to a.
lakes1 = ["Malawi", "Medicine", "Tahoe", "Moraine", "Upper Arrow", "Plitvice", "Edith", "Emerald"]
lakes2 = sorted(lakes1, key=lambda x: x[-1], reverse=True)

print(lakes2)

# Using lambda and sorted() function, sort the list based on the remainder from dividing each element
# to 5 (From greater to smaller).

lst1 = [1000, 50, 66, 101, 333, 9999, 19, 300, 200, 250]
lst2 = sorted(lst1, key=lambda x: x % 5, reverse=True)

print(lst2)
