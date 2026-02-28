# inheritance
class employee():
    def __init__(self,Name,ID,):
        self.Name = Name 
        self.ID = ID
        
        
        if 1 <= ID <=1000:
            self.post = "employee"
            print("🎉 Congratulations! You are in the position of Employee")
        elif 1001 <= ID <=2000:
            self.post = "manager"
            print("🎉 Congratulations! You are in the position of Manager.")
        else:
            self.post = "unknown"
            print("⚠️ Sorry! Your ID does not match any valid position.")
    def showDetails(self):
        print(f"the name of employee : {self.Name} and Id {self.ID}, and you are : {self.post}")
        
name1 = input("Enter your name: ")
Id = int(input("Enter your ID no. : "))

a1 = employee(name1,Id,)
a1.showDetails()