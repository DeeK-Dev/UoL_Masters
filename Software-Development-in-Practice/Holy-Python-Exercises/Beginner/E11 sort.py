# Sort the list in ascending order with .sort() method.

lst = [11, 100, 99, 1000, 999]
lst.sort()
print(lst)

# This time sort the countries in alphabetic order.

lst = ["Ukraine", "Japan", "Canada", "Kazakhstan", "Taiwan", "India", "Belize"]

lst.sort()
print(lst)

# Now sort the list in descending order with .sort() method.

lst.sort(reverse=True)
print(lst)

# Can you sort the gift list in reverse alphabetic order?

gift_list = ['socks', '4K drone', 'wine', 'jam']
gift_list.sort(reverse=True)
print(gift_list)

# Sort the list below in reverse alphabetic order and then assign the last element to the answer_1 variable.
NFL = ["Panthers", "Bears", "Dolphins" "Patriots", "Saints", "Giants"]
NFL.sort(reverse=True)
answer_1 = NFL[-1]
print(answer_1)

# Sort the cities from z to a.
muni = ["Melbourne", "Shanghai", "Delhi", "Atlanta", "Moscow", "Montreal"]
muni.sort()
print(muni)

# Sort the keys of the dictionary from a to z.
dict = {"tiramisu": 5, "chocolate": 2, "pudding": 3, "cheesecake": 4}
key_list = list(dict.keys())
print(key_list)
