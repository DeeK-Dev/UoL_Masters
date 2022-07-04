# Write an if statement that asks for the user's name via input() function.
# If the name is "Bond" make it print "Welcome on board 007."
# Otherwise make it print "Good morning NAME". (Replace Name with user's name)
name = input("Enter name: ")
if name.lower() == "bond":
    print("Welcome on board 007.")
else:
    print(f"Good morning, {name}")


# Write a function named "evens" which returns True if a number is even and otherwise returns False.

def evens(i):
    if i % 2 == 0:
        return True
    else:
        return False


print(evens(99))
print(evens(98))


# Write a function named "thedecimal" which returns the decimal part of a number.
# If decimal part is zero function should return this string: "INTEGER".

def the_decimal(number):
    if number - int(number) != 0:
        return number - int(number)
    else:
        return "INTEGER"


print(the_decimal(99.09))
print(the_decimal(99.00))

# treepersqkm is a dictionary showing the tree number of countries per square kilometer
# for random countries with sizeable population numbers.
# Write a function named "moretrees" that returns a list of country names with
# more than 20.000 trees per square kilometer.

treepersqkm = {
    "Finland": 90652, "Taiwan": 69593, "Japan": 49894,
    "Russia": 41396, "Brazil": 39542, "Canada": 36388,
    "Bulgaria": 24987, "France": 24436, "Greece": 24323,
    "United States": 23513, "Turkey": 11126, "India": 11109,
    "Denmark": 6129, "Syria": 534, "Saudi Arabia": 1
}


def moretrees(dict):
    tree_list = []
    for i in dict:
        if dict[i] > 20000:
            tree_list.append(dict[i])
    return tree_list


print(moretrees(treepersqkm))

# Write a function named "count_l" that counts the number of words that contain the letter: "l" in a given string.
str = "Oranges and lemons, Say the bells of St. Clement's. You owe me three farthings, Say the bells of St. Martin's"


def count_l(a):
    count = 0
    for i in a.split():
        if "l" in i:
            count += 1
    return count


print(count_l(str))

# Write a similar function to 7-e which returns the number of words that start with letter "A" in a string.
# (Make sure it counts lower case a's as well.).

str = "Oranges and lemons, Say the bells of St. Clement's. You owe me three farthings, Say the bells of St. Martin's"


def count_a(a):
    count = 0
    for i in str.split():
        print(i, i[0])
        if "a" in i[0].lower():
            count += 1
    return count


print(count_a(str))
