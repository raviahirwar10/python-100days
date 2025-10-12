# custem error
a = int(input("Enter a number for 10 to 15: "))
if a < 10 or a > 15:
    raise ValueError("The number is not in the range of 10 to 15")
print("You entered:", a)