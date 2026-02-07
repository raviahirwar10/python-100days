#dir,dict and help

#dir method
x = [1,2,3]
print(dir(x))

#dict method
class person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    
p = person("Christopher Nolan", 55)
print(p.__dict__)
 
# help method
print(help(person))


