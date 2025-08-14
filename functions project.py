# def calculate_percentage (total_marks, kitna_marks_hai):
#     return(kitna_marks_hai / total_marks)*100

# def check_grade(percentage):
#     if percentage>=90:
#         return "A+"
#     elif percentage>=75:
#         return "A"
#     elif percentage>=60:
#         return "B"
#     elif percentage>=45:
#         return "C"
#     elif percentage>=33:
#         return "D"
#     else:
#         return"fail"
    
# def pass_or_fall (percentage):
#     if percentage>=33:
#         return "Pass"
#     else:
#         return 'fail'
    
# Name = input("Enter your name:")
# total_marks = 500
# kitna_marks_hai = int(input("Enter total marks kitna_marks_hai (out of 500):"))

# percentage = calculate_percentage(total_marks,kitna_marks_hai)
# grade = check_grade(percentage)
# status = pass_or_fall(percentage)

# print ("\n student report card ")
# print ("----------------------")

# print("name         :",Name)
# print("marks        :",kitna_marks_hai, "/", total_marks)
# print("percentage   :",round(percentage,2),"%")
# print("grade        :",grade)
# print("result       :",status)



# # topic : weight and height calculatter
# def calculate_bmi(weight, height):
#     bmi = weight / (height ** 2)
#     return bmi

# def check_bmi_category(bmi):
#     if bmi<50:
#         return "underweight"
#     elif bmi<70:
#         return "normulweight"
#     elif bmi>87:
#         return "overweight"
#     else:
#         return "saraam akr bhai"

# print("wellcome to bmi calculater")
# weight = float(input("Enter your weight in kg :"))
# height = float(input("Enter your height in maters :"))

# bmi = calculate_bmi(weight, height)
# category = check_bmi_category(bmi)

# print ("\nYour bmi is",round(bmi,2))
# print("category",category)
    
    
# create calculater 
a = 12
b = 7
ans1 = a+b
# num = int(input("enter a number"))
print("addition in",a,"and",b,"is", ans1 )
ans2= a*b
print("multiplication in",a,"and",b,"is", ans2)
ans3=a-b
print("subtraction in",a,"and",b,"is",ans3)
ans4=a/b
print("division in",a,"and",b,"is", ans4)