# walrus Operators

#  while loop using walrus opr
number = [1,2,3,4,5]
while (n:= len(number))>0:
    print(number.pop())
    
# if statements using walrus opr
names = ("jhon","jake","fin")
if (name := input("Enter your name:")) in names:
    print(f"hello,{name}")
else:
    print("Name no found")
    
# Exampale
foods = list()
while (food := input("Enter Food do you like: ")) !="quit":
    foods.append(food)
    

    
