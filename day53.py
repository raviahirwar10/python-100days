# super keyword in python

class perent:
    def __init__(self,name):
        self.name = name 
    
class child(perent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age 
    
obj1 = child("Ajay",22)
print(obj1.name,obj1.age)


# anthor type
class employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id 
    
class programer(employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id) #Calling employe __init__
        self.lang = lang
        
A1 = employee('Ajay','990')
B1 = programer('Ajay Ahirwar','890','Java')
print(A1.name)
print(B1.name, B1.id, B1.lang)
        