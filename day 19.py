# topic tuple

tub = (1,2,3,64,61,3,33,132,32) #do not change tuple
# tub[0]={55} show the error
print(type(tub),tub)

# tuple Index
color = ("red","green","white")
print(color[1])

# postive index
country = ("Spain", "Italy", "India",)
print(country[0])
print(country[1])
print(country[2])

# nagative index
day = ("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
print(len(day))
print(day[-3])
print(day[-7])
print(day[-5])

# cheak for item
country1 = ("Spain", "Italy", "India", "England", "Germany","londan")
ent = str(input("enter country name :"))
if ent in country1:
    print("yes india is persent")
else:
    print("no his not persant")
    
# Printing elements within a particular range
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     #using positive indexes
print(animals[-7:-2])   #using negative indexes