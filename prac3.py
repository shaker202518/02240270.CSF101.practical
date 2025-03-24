asdfad
my_name_array = ["pema", False, 12, 1.22, True]
firstArrayLength = len(my_name_array)  # Get initial length

print(my_name_array)  # Print initial array

my_name_array.append("nima")  # Append new element
secondArrayLength = len(my_name_array)  # Get new length

print(firstArrayLength - secondArrayLength)  # Print the difference (should be -1)


# #For Loop
nameOfAnimals =["dog","cat","monkeys","gorrila"]
nameOfAnimals.append("elephant")
arrayLength = len(nameOfAnimals)
for index in range(arrayLength):
    print(nameOfAnimals)


while Loop 
name_Of_Animals = ["dogs", "cats", "monkeys", "elephnats" ]
arrayLength = len(name_Of_Animals)

index = 0

while index < arrayLength:
    print(name_Of_Animals[index])
    index = index + 1

generated_number = [0,1,2,3,4,5,6,7,8,9]
newstack = []
index = 9

while index > -1:
    newstack.append(generated_number[index])
    index = index - 1

print(newstack)