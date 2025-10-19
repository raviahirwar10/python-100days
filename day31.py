#Enumerate function



#normal 

#month = ['jan','fab','mar','apr','may','jun','jul','aug','seb','oct','nov','dec']
#index = 0
#for months in month:
#    print(months)
 #   if (index == 4):
  #      print("hello")
   # index +=1
    
#Enumerate function

month = ['jan','fab','mar','apr','may','jun','jul','aug','seb','oct','nov','dec']
for index,months in enumerate(month,start= 1):
    print(index,months)



fruits= ['apple','mango','banana','grapes']
for index,fruit in enumerate (fruits):
    print(fruit)
    if (index == 3):
        print(index,fruit)
    