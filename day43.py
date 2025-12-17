# class and objects

class persion:
    name = "ravi"
    age = "19"
    occupation = "data analyst"
    def desc(self):
        print("my name is",self.name,"and i m",self.age,"years old","and im a",self.occupation)

a = persion()
b = persion()
name1=input("Enter your name :")
a.name=(name1)
age1 = int(input("enter your age :"))
a.age=(age1)
occ1=input("Enter your occupation :")
a.occupation=(occ1)
# b.desc()
a.desc()
# obj1=persion()
# obj1.desc()
    

    
 