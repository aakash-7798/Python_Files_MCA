
# Written by Aakash Nadupalli

# 5. Create a class Rectangle. The constructor for this class should take two numeric
# arguments, which are the length and breadth. Add methods to compute the area and
# perimeter of the rectangle, as well as methods that simply return the length and
# breadth. Add a method isSquare that returns a Boolean value if the Rectangle is a
# Square.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def Area(self):
        return  self.length*self.breadth

    def Perimeter(self):
        return  2*(self.length+self.breadth)

    def isSquare(self):
        if self.length == self.breadth:
            return True
        else:
            return False


rt = Rectangle(10,20)
rt1 = Rectangle(4,4)
print("Area of Rectangle = ",rt.Area())
print("Perimeter of Rectangle = ",rt.Perimeter())
print("Checking Whether is Rectangle a Square  -> ",rt.isSquare())
print("Checking Whether is Rectangle a Square  -> ",rt1.isSquare())






