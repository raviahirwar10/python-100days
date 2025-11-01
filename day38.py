#seek() function
with open('day38rel.txt','r') as f:
    #move to the 5bite in the file 
    print(type(f))
    f.seek(5)
    #tell() function: save the current position
    print(f.tell())
    data = f.read(5)
    print(data)