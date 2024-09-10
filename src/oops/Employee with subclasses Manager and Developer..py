class Employee:
    def __init__(self,name,employeeid):
        self.name = name
        self.employeeid = employeeid

    def info(self):
        return ("sublass wiil return the details")

class Manager(Employee):
    def __init__(self,name,employeeid,dept):
        super().__init__(name,employeeid)
        self.dept = dept

    def info(self):
        return f"employee is {self.name} { self.employeeid} and {self.dept}"


class Developer(Employee):
    def __init__(self, name, employeeid, programming):
        super().__init__(name, employeeid)
        self.programming = programming

    def info(self):
        return f"employee is {self.name} {self.employeeid} and {self.programming}"


m1 = Manager("keer","123","hr")
print(m1.info())
print(issubclass(Developer,Employee))



