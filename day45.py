#topic dacorators.
def greet(fx):
 def mfx(*args,**kwargs):
    print("hello world")
    fx(*args,**kwargs)
    print("thankyou for using this programe ")
 return mfx
@greet
def hello():
    print("heloo world")
    
@greet
def add(a,b):
    print(a+b)
    
hello()
add(9,4)