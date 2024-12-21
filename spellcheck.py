# 1. Print Statement
print("Hello, World!")

# 2. Variables and Data Types
name = "Alice"
age = 25
height = 5.6
is_student = True

# 3. Conditional Statements
if age > 18:
    print(f"{name} is an adult.")
else:
    print(f"{name} is a minor.")

# 4. Loops
for i in range(5):
    print(f"Number: {i}")

# 5. Functions
def greet(person):
    return f"Hello, {person}!"

print(greet(name))

# 6. Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(f"Fruits: {fruits}")

# 7. Dictionaries
person = {"name": "Alice", "age": 25, "city": "New York"}
print(f"Person's city: {person['city']}")

# 8. Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# 9. File Handling
with open("example.txt", "w") as file:
    file.write("Hello, file!")

# 10. Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

person = Person("Alice", 25)
print(person.introduce())
