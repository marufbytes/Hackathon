score = 0

result1 = input ("1. What is 1+1 ?")
if result1 == "2":
    score+=1

result2 = input("2. Name of capital city of Bangladesh : ")
if result2.lower() == "dhaka":
    score+=1

result3 = input("3. How many moon world's has? : ")
if result3 == "1":
    score+=1

result4 = input("4. When we got independence from West Pakistan? : ")
if result4 == "1971":
    score+=1

result5 = input("5. Biggest city in Bangladesh? : ")
if result5.lower()=="dhaka":
    score+=1

print("Total score : ",score,"/5")