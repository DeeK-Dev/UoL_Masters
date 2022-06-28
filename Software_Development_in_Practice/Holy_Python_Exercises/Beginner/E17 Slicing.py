wrd = "Toscana"

# Slice the word until first "a". (Tosc)
ans = wrd[:4]
print(ans)

# Slice the word so that you get "cana".
ans = wrd[3:]
print(ans)

# Now try to get "can" only.
ans = wrd[3:6]
print(ans)

# Can you slice the word from beginning to the end with steps of 2 (including the last character.)?
ans = wrd[::2]
print(ans)

# Now slice the word with steps of 2, excluding first and last characters.
ans = wrd[1:-1:2]
print(ans)

# Can you slice the list so that it's reversed without using the .reverse() method?
ans = wrd[::-1]
print(ans)


lst=[0,1,2,3,4]
# Slice the list so that only last 2 elements are included.
ans = lst[-2:]
print(ans)

# Slice the second and third elements (50 and 20) in the list.
ans = lst[1:3]
print(ans)