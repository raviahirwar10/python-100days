def factorial(num):
    if num==0:
        
      return 1
    return num*factorial(num-1)
ans = int(input("Enter Number of find factorial"))
print(f"the factorial of {ans} is {factorial(ans)}")