import sqlite3
import random
import string
from generators import name_gen


# connect to the database
conn = sqlite3.connect('college.db')
c = conn.cursor()


# Generate 2 random entries for Admins table
for i in range(2):
    first_name, surname = name_gen()
    name = f"{first_name} {surname}"
    email = f"{first_name[0].lower()}.{surname.lower()}@example.com"
    password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    c.execute("INSERT INTO Admins (name, email, password) VALUES (?, ?, ?)",
              (name, email, password))

# Generate 10 random entries for Teachers table
for i in range(10):
    first_name, surname = name_gen()
    name = f"{first_name} {surname}"
    email = f"{first_name[0].lower()}.{surname.lower()}@example.com"
    password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    c.execute("INSERT INTO Teachers (name, email, password) VALUES (?, ?, ?)",
              (name, email, password))

# Generate 20 random entries for Students table
for i in range(20):
    first_name, surname = name_gen()
    name = f"{first_name} {surname}"
    email = f"{first_name[0].lower()}.{surname.lower()}@example.com"
    password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    c.execute("INSERT INTO Students (name, email, password) VALUES (?, ?, ?)",
              (name, email, password))

# Generate 10 random entries for Courses table
coures = ["Introduction to Programming", "Database Systems", "Data Structures and Algorithms", "Data Representation",
          "CPU", "Development Lifecycle", "Programming Part 2", "Programming part 3", "Networking", "AI"]
for i in range(10):
    name = courses[i]
    semester = random.randint(1,3)
    c.execute("INSERT INTO Courses (name, semester) VALUES (?, ?)",
              (name, semester))

# Commit the changes and close the connection
conn.commit()
conn.close()

