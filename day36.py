#reading a python file
f = open('day36code.py','r')
py= f.read()
print(py)
print(type(py))
f.close()

#writing a python file
#f.write("#hallo world!")
#f.close()

with open('day36code.py','r') as f: 
   py= f.read()
   print(py)
   print(type(py))