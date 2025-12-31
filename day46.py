#getters and setters

#gatter
class MyClass:
    def __init__(self, value):
        self._value = value
    def show(self):
        print(f"value is {self._value}")

    @property
    def value(self):
        return self._value
    
obj = MyClass(10)
print(obj._value)
obj.show()

#setters
class Mydoom:
    def __init__(self,value):
        self._vlaue = value 
        
    @property
    def ten_value(self):
        return 10*self._value
        
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10
        
obj = Mydoom(10)
obj.ten_value = 67
print(obj.ten_value)
        
