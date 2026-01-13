# instant and class variables
class employee:
    compney = "samsung"
    noofemployee = 0
    def __init__(self,name):
        self.name = name
        self.raise_amount =  0.2
        self.noofemployee +=1
        
    def details(self):
        print(f"name of employee {self.name} and the raise amount in {self.noofemployee} sized {self.compney} is {self.raise_amount}")
        
emp1 = employee("ravi")
emp1.raise_amount = 0.3
emp1.compney = "apple"
emp1.details()
employee.compney = "Google"
print(employee.compney)
emp2 = employee("tony")
emp2.details()