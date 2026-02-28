# multiple inheritance
class employee:
    def __init__(self, name,):
        self.name = name
    def show(self):
        print(f"Employee Name: {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance
    def show(self):
        print(f"the dance is: {self.dance}")
        
    
class DancerEmployee(employee, Dancer):
    def __init__(self, name, dance):
        self.name = name
        self.dance = dance
        
d = DancerEmployee("John", "Salsa")
print(d.name)
print(d.dance)
d.show()
print(DancerEmployee.__mro__)