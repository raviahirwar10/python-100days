#reading a python file
f = open('day37.py','r')
py= f.read()
print(py)
print(type(py))
f.close()

#writing a python file
#f.write("#hallo world!")
#f.close()

with open('day37.py','r') as f: 
   py= f.read()
   print(py)
   print(type(py))