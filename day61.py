# time module 
# time.time
import time

def usinwhile():
    i =0
    while i<10000:
        i=i+1
        print(i)

def usingfor():
    for i in range(10000):
        print(i)
        
init = time.time()
usingfor()
t1 = time.time()-init
init = time.time()
usinwhile()
print(time.time()-init)
print(t1)

# time.sleep
print(10)
time.sleep(5)
print("this is printed after 5 second")

# time.localtime
t = time.localtime()
formatted_time = time.strftime("%Y-%M-%D %H:%M:%S",t)
print(formatted_time)