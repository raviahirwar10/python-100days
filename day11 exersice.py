import time
timestamp = time.strftime("%H:%M:%S")
print (timestamp)
A = input("enter your name :")
print ("sir")

B = int(time.strftime("%H"))

if 4<= B <12 :
    print('good morning',A,"sir")
elif 12<= B <16:
    print('good afternon',A,"Sir")
elif 16<= B <20:
    print('good evening',A,"sir")
elif 20 <= B <4:
    print("good night", A, "sir")


