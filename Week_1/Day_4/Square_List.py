def Square_List(arr):

    for i in arr:
        result = i*i

        print (i, "=",result)

array = list(map(int,input("Enter the array: ").split()))
Square_List(array)
