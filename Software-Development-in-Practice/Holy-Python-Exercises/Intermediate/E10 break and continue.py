# Place a break statement in the for loop so that it prints from 0 to 7 only (including 7).

for i in range(100):
    print(i)
    if i == 7:
        break

# Add an if statement and a continue statement to the loop so that it skips when iterator equals "sun".

weather = ["snow", "rain", "sun", "clouds"]
for i in weather:
    if i == "sun":
        continue
    else:
        print(i)
        