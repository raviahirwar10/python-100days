#Exception handling 
#a = input("Enter the number ")
#print(f"multiplay table of {a} is: ")
#try:
 #   for i in range(1,11):
#      print(f"{int(a)} X {i} = {int(a)*i}")
##   print("invaled input")

try:
    num = int(input("enter an integer:"))
    a = [6,4]
    print(a[num])
except ValueError:
    print("invaled integer")
except IndexError:
    print('index error')