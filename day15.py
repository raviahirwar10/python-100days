# # break and cantinue 
for i in range(15):
    if (i==10):
        print("game s abaher")
        break
    print ("5 X", i,"=",5*i)
    
    
# cantinus
for i in range (1,21):
    if i%2 == 0:
        if i%4 == 0:
            continue
        print(i)