# projrct calculater
num1 = float(input("Phale sankhya dala"))
num2 = float(input("dusri sankhya dala"))
opration = input("in ma sa koi ek opration chuna? (+,-,*,/)")

if opration == "+":
    result = num1 + num2
    print (f"result: {num1}+{num2} = {result}")
    
elif opration == "-":
    result = num1 - num2
    print(f"result: {num1} - {num2} = {result}")
elif opration == "*":
    result = num1 * num2
    print(f"result: {num1} * {num2} = {result}")
    
elif opration == "/":
    result = num1 / num2
    print(f"result: {num1} / {num2} = {result}")
    
    