# method overriding
class shape:
    def __init__(self,x,y):
        self.x = x 
        self.y = y
    def area(self):
        return self.x * self.y
    
class circle(shape):
    def __init__(self,redious):
        self.redious = redious
        super().__init__(redious,redious)
    def area (self):
        return 3.14 * super().area()
    
c = circle(5)
print(c.area())
        