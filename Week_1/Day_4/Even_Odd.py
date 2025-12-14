def Even_Odd(num):

    if num%2 == 0 :
        return "Even"

    else:
        return "Odd"


n = int(input("Enter a number: "))
result = Even_Odd(n)
print(result)
