# Assign the first element of the list to answer_1 on line 2
lst = [11, 100, 99, 1000, 999]
answer = lst[0]

print(answer)

# This time print the second element of the list directly on line 3. You should get 100.
answer_2 = lst[1]
print(answer_2)

# Print the last element of the list through variable answer_1.
answer_3 = lst[-1]
print(answer_3)

# Appending
# On line 3, add the string "pajamas" to the list with .append() method.

gift_list = ['socks', '4K drone', 'wine', 'jam']
# Type your code here.
gift_list.append("pajamas")
print(gift_list)

# Using .append() method, add a new list to the end of the list which contains strings: "Navigator" and "Suburban".
lst = ["CRV", "Outback", "XC90", "GL", "Cherokee", "Escalade"]
#  Type your code here.
lst.append(["Navigator", "Suburban"])
print(lst)

# On line 3, this time add the sub-list: ["socks", "tshirt", "pajamas"] to the end of the gift_list.
gift_list.append(["socks", "tshirt", "pajamas"])
print(gift_list)

# On line 3, this time insert "slippers" to index 3 of gift_list.

gift_list = ['socks', '4K drone', 'wine', 'jam']
gift_list.insert(3, "slippers")
print(gift_list)

# Assign the index no of 8679 to the variable answer_1.

lst = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
answer = lst.index(8679)
print(answer)

# Using .remove() method, clear the last element of the list.
lst.remove(lst[-1])
print(lst)

# Using .reverse() method, reverse the list.
lst.reverse()
print(lst)

# Using .count() method, count how many times 6 occur in the list.
answer = lst.count(6)
print(answer)

# What is the sum of all the numbers in the list?
answer = sum(lst)
print(answer)

# What is the minimum value in the list?
answer = min(lst)
print(answer)

# What is the maximum value in the list?
answer = max(lst)
print(answer)