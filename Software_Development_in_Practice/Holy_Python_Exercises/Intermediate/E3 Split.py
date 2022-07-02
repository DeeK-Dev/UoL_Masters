# Split the string based on space character: " ".
str = "Hello World!"
lst = str.split(" ")
print(lst)

# Split the numbers.
str = "101:102:103:201:202"
lst = str.split(":")
print(lst)

# Using the split method, split the string with semi colon (;) first. Then, print only the last element.
str = "Arsenal:0-Chelsea:1;Barcelona:2-Bayern Munich:2"
lst = str.split(";")
ans_1 = lst[-1]
print(ans_1)


