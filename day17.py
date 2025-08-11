# list

coler = ["red","green","pink","black"]
print(coler)

# list index

coler1 = ["red","green","pink","black"]
print (coler1[0])
print (coler1[2])
print (coler1[3])

# negative index

fruit = ["mango","banana","orange","grapes"]
print(fruit[-2])
print(fruit[-1])
print(fruit[-3])

# Check whether an item in present in the list?

fruit1 = ["mango","banana","orange","grapes"]
if "orange" in fruit1:
    print("Yes")
else:
    print("No")


# jum index

num = [i*2 for i in range (20)]
print (num)
num2 = [i for i in range (50)if i%2==0]
print(num2)
