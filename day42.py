#OOP (object oriented progaming)

class student:
    def __init__(self,name,age ):
        self.name = name 
        self.age = age 
    def study(self):
        print(f"name : {self.name} age : {self.age}")
#object create karna 
s1 = student("rvai\n","19\n")
s1.study()
    
