fruits = ["Apple", "Banana", "Gauva", "Graps","Orange", "Cocunut"]    #Ordered, changeabel, value are changeable

print(fruits)
print()

print(fruits[0])
print()

print(fruits [0:3])
print()

print(fruits [::2])   #every second
print()

print(fruits[::-1])   #Reverse
print()

print(fruits.index("Apple"))

#Details:
print("Number of fruits: ",len(fruits))
print("Existance:","Apple" in fruits) 

fruits[0]= "Dragon"     #Re-assign value
print(fruits)     
print(len(fruits))

fruits.append("Pineapple")    #Adding end of the list
print(fruits)

fruits.remove("Pineapple")     #Remove element
print(fruits)

fruits.insert(0,"Jack-Fruit")    #Inserting value
print(fruits)

fruits.sort()     #Sorted in alphabetical order
print(fruits)

fruits.reverse()     #Sorted in revere alphabetical order
print(fruits)

fruits.clear()    #cleae all
print(fruits)

fruits = ["Apple", "Banana", "Gauva", "Graps","Orange", "Banana"]

print("BANANA: ",fruits.count("Banana"))
