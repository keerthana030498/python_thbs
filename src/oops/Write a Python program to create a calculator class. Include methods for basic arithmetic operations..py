class Calculator:
    def __init__(self):
        self.result = 0
    def add(self,x,y):
        self.result = x+y
        return  self.result

    def subtract(self,x,y):
        self.result = x-y
        return  self.result

    def multiply(self,x,y):
        self.result = x*y
        return  self.result
    def divide(self,x,y):
        self.result = x/y
        return  self.result

value1 = Calculator()
print(value1.add(10,20))
print(value1.subtract(10,20))
print(value1.multiply(10,20))
print(value1.divide(10,20))




