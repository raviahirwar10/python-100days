#multithreading

import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
def main():
 time1 = time.perf_counter()
 #simple code 
 # func(6)
 # func(3)
 # func(1)

 #same code using threads

 t1 = threading.Thread(target=func, args=[6])
 t2 = threading.Thread(target=func, args=[4])
 t3 = threading.Thread(target=func, args=[2])
 t1.start()
 t2.start()
 t3.start()
 
 t1.join()
 t2.join()
 t3.join()
 
 time2 = time.perf_counter()
 print(time2-time1)

# threadpool executor 
def poolingdemo():
    with ThreadPoolExecutor() as executor:
     future1 = executor.submit(func,3)
     future2 = executor.submit(func,5)
     future3 = executor.submit(func,1)
     print(future1.result())
     print(future2.result())
     print(future3.result())
    
poolingdemo()