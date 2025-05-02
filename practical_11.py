from pyclbr import Class


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("Shaker", 20)
print(p1) 

# Implementation of instnace method with stter method
class Person:
  def __int__(self, name, age):
    self.name = name
    self.age = age 
    
  def hello(self):
    print("Hello my name is" + self.name + "my age is " + str(self.age))
  @property
  def age (self):
    return self.__age
  
  @age.setter
  def age(self, newage):
    self._age = newage
    
  def __str__(self):
    return f"{self.name}({self.age})"
  
  p1 = Person("shaker", 20)
  print(p1)
  
#Implentation of Subclass 
class Dancer():
  def __init__(self, name, age, genre):
    super().__init__(name, age)
    self.genre = genre
    
  def dance(self):
    print("my name is " + self.name + " my favourite dance is" + self.genre)
    
  def __str__(self):
    return f"{self.name}({self.age}) does {self.genre}"
d1 = Dancer("Hritik Roshan", 45, "Moon walk" )
print(d1)