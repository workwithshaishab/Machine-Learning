
class Animal:
    def __init__(self,name):
        self.name=name

    def display(self):
        print("Animal makes the sound....")

class Dog(Animal):
    def display(self):
        print(f"{self.name} does How How How")

class Cat(Animal):
    def display(self):
        print(f"{self.name} does Meow Meow")


d= Dog("Lucy")
d.display()
c= Cat("Tommy")
c.display()

"""
Uses of self:

1. Refers to the current instance.
2. Lets you access and modify attributes of that instance.
3. Automatically passed when calling methods.
4. Used in inheritance to access parent attributes.
5. Differentiates between object attributes and local variables.
"""