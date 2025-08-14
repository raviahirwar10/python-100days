# import time
# timestamp = time.strftime("%H,%M,%S")
# print(timestamp)

# timestamp = int(time.strftime("%H"))
# print(timestamp)
# # timestamp = int(time.strftime("%M"))
# # print(timestamp)
# # timestamp = int(time.strftime("%S"))
# # print(timestamp)

    
# if 6<= timestamp <12:
#     print("good morning")
# elif 12<= timestamp <16:
#     print("good afternnon")
# elif 16<=timestamp <20:
#     print("good evening")
# elif 20<=timestamp <24:
#     print("good night")



from datetime import datetime, date
dob = input("Enter Your date of Biarth (YYYY-MM-DD): ")
birthdate = datetime.strptime(dob, "%Y-%m-%d").date()
today = date.today()

days = (today-birthdate).days

years = days // 365
days = days % 365
months = days // 30
days_left =  (days % 365) % 30

print(f"you are {years}years,{months}months, and {days_left} Days old")