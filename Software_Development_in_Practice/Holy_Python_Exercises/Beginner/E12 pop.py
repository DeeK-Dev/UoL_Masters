# Pop the last item of the list below.

lst = [11, 100, 99, 1000, 999]
popped_item = lst.pop()
print(popped_item)
print(lst)

# Remove "broccoli" from the list using .pop and .index methods.

lst=["milk", "banana", "eggs", "bread", "broccoli", "lemons"]

index_to_pop = lst.index("broccoli")
item = lst.pop(index_to_pop)
print(lst, item)

# Save Italy's GDP in a separate variable and remove it from the dictionary.
GDP_2018={"US": 21, "China": 16, "Japan": 5, "Germany": 4, "India": 3, "France": 3, "UK": 3, "Italy": 2}


italy_gdp = GDP_2018.pop("Italy")
print(GDP_2018)
print(italy_gdp, "trillion USD")