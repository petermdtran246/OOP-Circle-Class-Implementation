import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2*(math.pi)* self.radius

radius = float(input('Input the radius: '))
c1 = Circle(radius)
print(f'Area: {c1.area():.2f}')
print(f'Perimeter: {c1.perimeter():.2f}')
 
