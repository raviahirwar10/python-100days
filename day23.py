#sets 

# info = {"carla",12,56,"hap",55,12}
# print(info)

#sets method

#union
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)

#intersection 
citie = {"Tokyo", "Madrid", "Berlin", "Delhi"}
citie = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities = citie.intersection()
print(cities)

#symmetric_difference 
citi = {"Tokyo", "Madrid", "Berlin", "Delhi"}
citi2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
citi3 = citi.symmetric_difference(citi2)
print(citi3)


#isdisjoin
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))


print("etc......")