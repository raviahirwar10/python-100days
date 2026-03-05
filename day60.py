# hierarchical inheritance
class Animal:
    def eat(self):
        print("Eating..")
    
class Dog(Animal):
    def bark(self):
        print("barking...")
        
class Cat(Animal):
    def meow(self):
        print("meow...")

d = Dog()
d.eat()
d.bark()

# hybrid Inheritance

class A:
    def showA(self):
        print("class A")
class B:
    def showB(self):
        print("class B")
class C:
    def showC(self):
        print("class C")
class D (B,C):
    def showD(self):
        print("class D")
        
d = D()
d.showB()
d.showC()
d.showD()