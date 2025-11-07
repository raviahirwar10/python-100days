#this is a normal function 
# def sum(a, b):
#     return a + b
# print( sum(5, 10))

#this is a lambda function
sum = lambda a,b: a+b
print(sum(5, 10))
cube = lambda x: x*x*x
print(cube(3))
average = lambda a,b,c,d: (a+b+c+d)/4
print(average(10,20,30,40))