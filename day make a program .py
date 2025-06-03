def voter_eligibility_check ():
    try:
        name = input("enter your name:")
        age = int(input("Enter your age:"))
        if age >= 18:
           print(f"\n {name},if you are eligible for vote!")
        else:
          print(f"\n sorry {name}, if you are not eligible for vote. you must be at least 18 years old")
    except ValueError:
    
        print("\n please enter a valid number of age.")
        
# run a function
voter_eligibility_check() 