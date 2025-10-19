#How importing in python works

import math
doc=math.factorial(9)
print(doc)

#from keyword

from math import sqrt,pi
result = sqrt(9)
print(result)

print(pi)

#importing everything

from math import *
result = sqrt(4)
print(result)

print(pi)


#The "as" keyword

import math as m
fic= m.sqrt(10)
print(fic)
print(m.pi)

