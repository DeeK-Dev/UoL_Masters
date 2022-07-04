# Create a range from 0 to 50, excluding 50.

rng = range(0,50)
print(rng)

# Create a range from 0 to 10 with steps of 2.
rng = range(0,10,2)
print(list(rng))

# Create a range from 100 to 160 with steps of 10. Then print it as a list.
rng = range(100,160,10)
print(list(rng))

# Can you you create a list from 1300 to 700 with descending steps of 100? Is your stop value included in the list?

rng = range(1300, 700, -100)
print(list(rng))

# Can you you create a list from 1300 to 700 with descending steps of 100, this time including 700?
rng = range(1300, 699, -100)
print(list(rng))