student =[
    {"name":"Maruf", "goal": "Don't know", "current_level": "Undergrade"},
    {"name":"Sajid", "goal": "Biye", "current_level": "Undergrade"},
    {"name":"Shohag", "goal": "Prem", "current_level": "Undergrade"}
]

for i in student:
    print(i["name"],"'s goal is ",i["goal"],"and current level is", i["current_level"])
print() 
print()

for i in student:
    print(f"{i['name']}'s goal is {i['goal']} and current level is {i['current_level']}")