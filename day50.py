#class method;

class Employee:
    company = "samsung"
    def show (self):
        print(f"the name is {self.name} and company name {self.company}")
        
    @classmethod
    def chgcompany(cls, newcompany):
        cls.company = newcompany
    
A1 = Employee()
A1.name = "ravi"
A1.show()
A1.chgcompany("Apple")
A1.show()
print(Employee.company)