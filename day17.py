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

# day 18 basic list mathod

# 1. append
i = [12,1,2,4,1,54,56,262,63,12,121,32,32,2,2]
i.append(555)
print(i)

# 2. sort
i.sort()
print(i) 

# 3 count
print(i.count(555))

# 4 remove
i.remove(262)
print(i)

# 5 insert
i.insert(10,666)
print(i)

# 6 clear
# i.clear()
# print(i)

# 7 index
print(i.index(32))


# 8 reverse
i.reverse()
print(i)

# 9 copy 
print(i.copy())

# 10 extend
k = [100,1200,1300]
i.extend(k)
print(i)
