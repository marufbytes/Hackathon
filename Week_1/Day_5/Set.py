fruits = {"Apple", "Banana", "Gauva", "Graps","Orange", "Cocunut"}   #Unodered, no duplicate
print(fruits)

print(len(fruits))
print("Apple" in fruits)

fruits.add("Pineapple")
print(fruits)

fruits.remove("Apple")
print(fruits)

fruits.pop()      #remove usually first element, but it's random as set
print(fruits)