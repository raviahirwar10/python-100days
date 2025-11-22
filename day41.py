# 'is' vs '==' in Python
a = [2,4,6]
b = [2,4,6]
print(a==b) # true (dono value same hai)
print(a is b) # false (dono alag object hai)

c=4
d=4
print(c==d) # true 
print(c is d)  # True (small integer cache)
