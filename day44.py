#costructor 
class student:
    def __init__(self,name,age,):
        self.name = name 
        self.age = age 
    def info(self):
        print("hey. my name is",self.name,"and im",self.age,"year old")
name1 = input("Enter your name:")
age1 = int(input("Enter your age:"))
a = student(name1,age1)
a.info()