# Print 5 by accessing the nested data.
nested_lst = [[1,2,3], [4,5,6], [7,8,9]]
ans_1 = nested_lst[1][1]
print(ans_1)

# Print "Z" from the nested data.
nested_lst = [["Hat", "Glove", "Goggle"], ["Button", "Zipper", "Hook"]]
ans_1 = nested_lst[1][1][0]
print(ans_1)

# What color is the violet?
nested_lst = [{"orange": "orange"}, {"rose": "red"}, {"violet": "blue"}]
ans_1 = nested_lst[2]["violet"]
print(ans_1)

# Print the values of the "roads" key from the nested dictionary.
nested_dict = {"Dakar":{"weather":"sunny", "roads":"dry"}}
ans_1 = nested_dict["Dakar"]["roads"]
print(ans_1)

# Print the first element of the weather for Tokyo.
nested_dict = {"Tokyo": {"weather":["sunny", "cloudy"], "roads":"dry"}, "Dakar": {"weather":["foggy","windy"], "roads": "sandy"}}
ans_1 = nested_dict["Tokyo"]["weather"][0]
print(ans_1)