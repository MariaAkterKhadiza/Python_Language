class Shape:
    def __init__(self, name):
        self.name = name

class Circle(Shape):
    def __init__(self, name, radius):
        Shape.__init__(self, name)
        self.radius = radius

circle = Circle("Circle", 20)
print(circle.name)
print(circle.radius)