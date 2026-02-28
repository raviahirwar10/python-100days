# single inheritance
class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def make_sound(self):
        print("the animal makes a sound")
    
class Dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self,name,species="Dog")
        self.breed=breed
        
    def make_sound(self):
        print("woof!")

d = Dog("Buddy","Labrador")
d.make_sound()  # Output: woof!
a = animal("Dog","og")
a.make_sound()