# Assign the string below to the variable in the exercise.
# "It's always darkest before dawn."

string = "It's always darkest before dawn."
print(string)

# By using first, second and last characters of the string, create a new string.
ans = string[0] + string[1] + string[-1]
print(ans)

# Replace the (.) with (!)
string = string.replace(".", "!")
print(string)

# Reassign str so that, all its characters are lowercase.
print(string.lower())

# Now make everything uppercase.
print(string.upper())

# Make the string so that everything is properly and first letter is capital with one function.
str = "there are no traffic JamS Along The extra mile."
new_str = str.lower().capitalize()
print(new_str)

# Does the string start with an A?
# Assign a boolean answer to the ans_1 variable.
str = "There are no traffic jams along the extra mile."
answer = str.startswith("A")
print(answer)

# Does it end with a fullstop (.) ?
answer = str.endswith(".")
print(answer)

# Using .index() method, identify the index of character: (v).
str = "The best revenge is massive success."
answer = str.index("v")
print(answer)

# Using .find() method, identify the index of character: (m).
answer = str.find("m")
print(answer)

# Try to see what results you get looking for character: (X). First with .find() method and then with .index() method.
answer_find = str.find("X")
print(answer_find)
try:
    answer_index = str.index("X")
    print(answer_index)
except(ValueError):
    print("error")

str = "People often say that motivation doesn't last. Well, neither does bathing.  That's why we recommend it daily."
ans_1 = str.count("a")
ans_2 = str.count("o")
print("count of a is: ", ans_1, " count of o is: ", ans_2)

# Print the types of two given variables with the print function.
v_1 = "1"
v_2 = 1

ans_1 = type(v_1)
ans_2 = type(v_2)
print(ans_1)
print(ans_2)

# What is the length of the given string?
str="1.975.000"

ans_1 = len(str)
print(ans_1)

