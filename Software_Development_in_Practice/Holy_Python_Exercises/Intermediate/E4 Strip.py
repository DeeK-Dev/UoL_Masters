# Use strip method to strip the whitespaces on both sides of the string.
str = "     Hello World!   "
str = str.strip(" ")
print(str)

# Using .strip() method, strip the string so that, only "Babylon" remains.
str = "#$^&#@%$& Babylon #@$&@#"
str = str.strip("#$^&@% ")
print(str)

'''
Let's say you created a program that crawls websites online and it returned a string 
with a bunch of unnecessary characters on the right side. 

Using .rstrip() method, strip the characters from the right side of the string only so, 
in the end you get: "@Bloomberg"
'''

str="@Bloomberg@@@@@###"
str = str.rstrip("@#")
print(str)

# Using a combination of .split() and .lstrip() methods, get the word "Derivatives".

str="......Macroeconomics,...........Derivatives"

str = str.split(",")
print(str)
ans_1 = str[1].lstrip(".")

print(ans_1)