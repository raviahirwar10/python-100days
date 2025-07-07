# topic match case statment
x = int(input("enter a num :"))

match x:
    case  0:
        print("is equel to zero")
    case 10:
        print  ("x is 10")
        # if statment
    case _ if x!=100:
        print("x is not 100")
    case _ if x!=199:
        print('x is not 199')
    case __:
        print (x)
    