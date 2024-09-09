class Polygon:
    def __init__(self, sides):
        self.sides = sides


class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__(3)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Rectangle(Polygon):


    def __init__(self, width, rec_height):
        super().__init__(4)
        self.width = width
        self.rec_height = rec_height


    def area(self):
        return self.width * self.rec_height

def print_area(polygon):
    print(f"the area of the polygon is : {polygon.area()}")


mytriangle = Triangle(10,2)
myreactangle = Rectangle(5,4)

print_area(mytriangle)
print_area(myreactangle)
