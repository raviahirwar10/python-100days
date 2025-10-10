#finally keybprd
def func():
    try:
      a = [2,3,45,67]
      i = int(input("Enter an index"))
      print(a[i])
      return 1
    except:
        print('some error occurred')
        return 0 
    finally:
         print("i am always executed ")
x = func()
print(x)
