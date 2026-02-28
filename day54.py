# magic oreating methods

class Employee:
    def __init__(self,name,post):
        self.name = name 
        self.post = post
    def __len__(self):
        return len(self.name) + len(self.post)
    
    def __str__(self):
        return f"Employee name is {self.name} and post is {self.post}"
    
    def __repr__(self):
        return f"Employee('{self.name}','{self.post}')"
    
    # def __add__(self, partner):
    #     return f"{self.name} is working with {partner.name}"
    
emp1 = Employee("Rakhi","web developer")
print(emp1.name,emp1.post,len(emp1))
print(emp1)
print(repr(emp1))
# emp2 = Employee("Ajay", "Ahirwar","Python developer")
# print(emp1 + emp2)