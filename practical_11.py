class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("Shaker", 20)
print(p1) 

# Implementation of instnace method
class Person:
  def __int__(self, name, age):
    self.name = name
    self.age = age 
    
  def hello(self):
    print("Hello my name is" + self.name + "my age is " + str(self.age))
  p1 = Person("shaker", 20)