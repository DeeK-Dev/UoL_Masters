# Join the list's elements with: "+++".
lst = ["Hawaii", "Phuket", "Aruba", "Keys"]
joined = "+++".join(lst)
print(joined)

# Join the tuple's elements so that you get a proper email address.
addresses=("Mr.Hathaway", "amymail.com")
email = "@".join(addresses)
print(email)

# Join each element in the list with a space character: " "
lst=['Everything', 'has', 'beauty,', 'but', 'not', 'everyone', 'can', 'see.']
str = " ".join(lst)
print(str)

# Using .join() method join the keys in the dictionary with a comma: ",".
economic_growth={"India": 7.0, "Cambodia": 7, "Tanzania": 6.9, "Bangladesh": 6.6, "Senegal": 6.6}
str = ", ".join(economic_growth)
print(str)

# Using "\n" character and .join() method, join the sentences in the list so that it looks like a proper poem.
poem_lst=["Not enjoyment, and not sorrow,", "Is our destined end or way;", "But to act, that each tomorrow", "Find us farther than today."]
poem_str = "\n".join(poem_lst)
print(poem_str)
