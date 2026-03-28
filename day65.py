#function caching 
from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(3)
    return n*2
print(fx(20))
print("Done for 20")
print(fx(10))
print("Done for 10")
print(fx(25))
print("Done for 25")

print(fx(20))
print("Done for 20")
print(fx(10))
print("Done for 10")
print(fx(25))
print("Done for 25")
print(fx(29))
print("Done for 29")
