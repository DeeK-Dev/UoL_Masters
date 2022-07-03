# Using zip() function and list() function, create a merged list of tuples from the two lists given.

lst1 = [19542209, 4887871, 1420491, 626299, 1805832, 39865590]
lst2 = ["New York", "Alabama", "Hawaii", "Vermont", "West Virginia",  "California"]
lst3 = list(zip(lst1, lst2))
print(lst3)

# First create a range from 1 to 8. Then using zip, merge the given list
# and the range together to create a new list of tuples.

lst1 = ["Energy", "Agriculture", "Industry", "Technology", "Finance", "Forestry", "Transport"]
rng1 = range(1,8)
lst = list(zip(lst1, rng1))
print(lst)

# Using zip and dict functions create a dictionary which has its key-value pairs coming from lst1 and lst2.
lst1 = ["Netflix", "Hulu", "Sling", "Hbo"]
lst2 = [198, 166, 237, 125]
points = dict(zip(lst1, lst2))
print(points)

# Using zip, list and sorted functions create a sorted list of tuples from lst1 and lst2.
lst1 = ["Mike", "Danny", "Jim", "Annie"]
lst2 = [4, 12, 7, 19]
sorted_lst = sorted(list(zip(lst1, lst2)))
print(sorted_lst)

#