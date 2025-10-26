#global and local variable
a = 20 #global variable

def num_number():
    a = 30 #this will change the value of the global variable a
    b =30 #local variable
    print(b)
    print(a)
num_number()
