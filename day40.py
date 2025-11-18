
def cube(x):
    return x*x*x
print(cube(2))

# map
l = [1,2,4,5,5,7]
new1 = list(map(lambda x: x*x*x,l))
print(new1)

# filter
def filter_function(a):
    return a>4
new11 = list(filter(filter_function,l))
print(new11)

# reduce
from functools import reduce
number = [2,3,4,5,6]
sum = reduce(lambda x,y: x+y,number)
print(sum)

