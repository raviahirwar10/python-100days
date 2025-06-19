# string amthod 
a = "pradesh?????? up gaon"
print (len(a))
print (a.upper())
print (a.lower())
print (a.rstrip("?"))
print (a.replace("pradesh","videsh"))
print (a.split(" "))

hsss = "haey how are you"
print (hsss.capitalize())

name = " utter pradesh up"
print (len(name))
print (len(name.center(50)))
print (a.count("pradesh"))

name1 = "hey my name is kalu"
print (name1.endswith("kalu"))
print ( name1.find("is"))
print (name1.index("is"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str2 ="         "
print (str1.islower())
print (str2.isspace())
print (str1.istitle())

print (name1.swapcase())
print (str1.title())