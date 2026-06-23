"""
Week 1: Python Basics
----------------------
Practice script covering variables, data types, lists, dictionaries,
loops, and functions. Based on the Week 1 video lecture (up to Chapter 8,
excluding recursion) and the Ultimate Python Handbook.
"""

# ----------------------------
# 1. Variables & Data Types
# ----------------------------
name = "Alex"          # str
age = 21                # int
height = 5.9            # float
is_student = True       # bool

print("--- Variables & Data Types ---")
print(f"Name: {name} ({type(name).__name__})")
print(f"Age: {age} ({type(age).__name__})")
print(f"Height: {height} ({type(height).__name__})")
print(f"Is student: {is_student} ({type(is_student).__name__})")

# Type casting
age_str = str(age)
height_int = int(height)
print(f"Age as string: '{age_str}', Height as int: {height_int}\n")


# ----------------------------
# 2. Lists
# ----------------------------
print("--- Lists ---")
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

fruits.append("mango")          # add an item
fruits.remove("banana")         # remove an item
fruits.sort()                   # sort alphabetically

print("Updated list:", fruits)
print("First item:", fruits[0])
print("Last item:", fruits[-1])
print("Sliced list (first two):", fruits[:2])
print()


# ----------------------------
# 3. Dictionaries
# ----------------------------
print("--- Dictionaries ---")
student = {
    "name": "Alex",
    "age": 21,
    "courses": ["Python", "Machine Learning"]
}

print("Student info:", student)
print("Name:", student["name"])

student["age"] = 22  # update a value
student["grade"] = "A"  # add a new key

print("Updated student info:", student)

print("Looping through dictionary:")
for key, value in student.items():
    print(f"  {key}: {value}")
print()


# ----------------------------
# 4. Loops
# ----------------------------
print("--- Loops ---")

# for loop
print("For loop (counting 1 to 5):")
for i in range(1, 6):
    print(i, end=" ")
print()

# while loop
print("While loop (countdown from 5):")
count = 5
while count > 0:
    print(count, end=" ")
    count -= 1
print()

# loop with break and continue
print("Loop with break/continue (skip 3, stop at 7):")
for i in range(1, 10):
    if i == 3:
        continue
    if i == 7:
        break
    print(i, end=" ")
print("\n")


# ----------------------------
# 5. Functions
# ----------------------------
print("--- Functions ---")

def greet(person_name, greeting="Hello"):
    """Returns a greeting message for a given name."""
    return f"{greeting}, {person_name}!"

print(greet("Alex"))
print(greet("Sam", greeting="Hey"))


def calculate_average(numbers):
    """Returns the average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

scores = [85, 90, 78, 92]
print(f"Average score: {calculate_average(scores)}")


def is_even(number):
    """Returns True if the number is even, False otherwise."""
    return number % 2 == 0

for n in range(1, 6):
    status = "even" if is_even(n) else "odd"
    print(f"{n} is {status}")


