def Detect(num):

    if num>0:
        return "Positive"
    if num<0:
        return "Negative"
    else:
        return  "Zero"
    

n = float(input("Enter a number: "))
result = Detect(n)
print(result)