#classmethod as alternative constructars
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls, string):
        name, age = string.split(",")
        return cls(name, int(age))
    
person1 = Person("gulshan", 22)
print(person1.name,person1.age)

