# if,else,elif 
a = int(input("inter your age :"))
print("your age is",a)

# conditionl opratore
# > , < , >= , <= , == !=
# print(a>18)
# print(a<18)
# print(a>=18)
# print(a<=18)
# print(a==18)

if (a>18):
    print("you can drive")
elif (a >15 and a <= 18):
    print ("you can applay for learning licenc")
else :
    print("you cannot drive")
    