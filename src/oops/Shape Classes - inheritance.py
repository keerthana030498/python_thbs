class Shape:
    def __init__(self,color):
        self.color = color

    def area(self):
        return " subclasses will be implemented"

class Circle(Shape):
    def __init__(self,radius,color):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
class Rectangle(Shape):
    def __init__(self,color,width,height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return  self.width * self.height


circle1  = Circle(10, "red")
print(circle1.area() , circle1.color)

rectangle1 = Rectangle("yellow",10,20)
print(rectangle1.area(),rectangle1.color)