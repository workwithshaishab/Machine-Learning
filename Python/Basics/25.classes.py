class Rectangle:
    def __init__(self, length , breadth):  #self is a reference to the instance of the class.
        self.length=length
        self.breadth=breadth
    
    def display(self):
        print("The area of rectangle is:", self.length*self.breadth)
    
r= Rectangle(20,12)
r.display()