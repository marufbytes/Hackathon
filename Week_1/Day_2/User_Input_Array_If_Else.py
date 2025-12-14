num = list(map(int, input("Enter the digits:").split()))

positive = []
negavive = []
zero =[]

for i in num:
    if i>0:
        positive.append(i)

    elif i<0:
        negavive.append(i)

    else:
        zero.append(i)

print("Positive numbers:", positive)
print("Negative numbers:", negavive)
print("Zeros:", zero)
