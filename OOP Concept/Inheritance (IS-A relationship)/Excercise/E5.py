class shape:
    pass
class rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle1 = circle(5)
print("Area of circle:", circle1.area())  # Output: Area of circle: 78.5
rec1 = rectangle(4, 6)
print("Area of rectangle:", rec1.area())  # Output: Area of rectangle: 24