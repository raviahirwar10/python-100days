def calculate_percentage (total_marks, kitna_marks_hai):
    return(kitna_marks_hai / total_marks)*100

def check_grade(percentage):
    if percentage>=90:
        return "A+"
    elif percentage>=75:
        return "A"
    elif percentage>=60:
        return "B"
    elif percentage>=45:
        return "C"
    elif percentage>=33:
        return "D"
    else:
        return"fail"
    
def pass_or_fall (percentage):
    if percentage>=33:
        return "Pass"
    else:
        return 'fail'
    
Name = input("Enter your name:")
total_marks = 500
kitna_marks_hai = int(input("Enter total marks kitna_marks_hai (out of 500):"))

percentage = calculate_percentage(total_marks,kitna_marks_hai)
grade = check_grade(percentage)
status = pass_or_fall(percentage)

print ("\n student report card ")
print ("----------------------")

print("name         :",Name)
print("marks        :",kitna_marks_hai, "/", total_marks)
print("percentage   :",round(percentage,2),"%")
print("grade        :",grade)
print("result       :",status)