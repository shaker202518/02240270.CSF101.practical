print("Hello!!!!")
print("This is my first script!")

pi = 3.14
pi2 = int(pi)
print(pi)
print(pi2)

pi3 = "3.14"
print(type(pi3))
pi4 = float(pi3)
print(type(pi4))

print(0<1)
print(1>0)
bool(0)
bool(1)
bool("Hello")

x = None
print(x)

# Basics data Types: string manupulation
print("Hello!!!!")
print("This is my first script!")
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# String functions
print(len(a))
print(a.upper())
print(a.lower())
print(a.count('i'))
print(a.find('d'))
print(a.split())

# String Concatenation
b = "Hello"
c = "Hello"
d = b + "!!" + c + "??"
print(d)

# String replication
print("Alice" * 5)

# String formatting
name = "Karma"
print(f"Hello {name}")
print("Greeting to you, {}".format(name))
Number = 2
print("There are %d %s in the class" %(Number, name))

# Basic data structure
# List
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))
print(thislist.index("banana"))
thislist.remove("banana")
thislist.insert(1, "strawberry")
print(thislist)

# Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))
print(type(thistuple))

# Set
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
print(len(thisset))
print(type(thisset))

# Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])

# Student Exercise
# Q1.
first_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(first_list)
inverse_list = []

index = 9  # Start from the last index
while index >= 0:   # While index is still valid
    inverse_list.append(first_list.pop())  # Pop from first_list and append to inverse_list
    index -= 1  # Decrease the index

print(inverse_list)
# Q2
def reverse_array(first_list):
    inverse_list = []
    index = len(first_list) - 1  # Start from the last index
    while index >= 0:
        inverse_list.append(first_list.pop())
        index -= 1
    return inverse_list

# Example usage:
first_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = reverse_array(first_list)
print(result)

