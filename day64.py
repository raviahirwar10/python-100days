# generatars
def my_generatar():
    for i in range (100):
        yield i
gen = my_generatar()

# print(next(gen))
# print(next(gen))
for j in gen:
    print(j)