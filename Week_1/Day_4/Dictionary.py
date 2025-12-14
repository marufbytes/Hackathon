students = [
    {"name": "Maruf", "mark": 55},
    {"name": "Sadib", "mark": 33},
    {"name": "Shohag", "mark": 44},
    {"name": "Sajid", "mark": 66}
]

#Print name:

print ("Students name: ")
for i in students:
    print (i["name"])
print()

#Marks
print ("Student's Marks: ")
for i in students:
    print(i["mark"])

#Together:
print ("Marks: ")
for i in students:
    print( i["name"], " : ", i["mark"])