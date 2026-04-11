def createIntArray():
    print("Enter the ele's into the array to be created")
    l1=[]
    while True:
        try:
            n=int(input("Enter num:"))
            l1.append(n)
        except Exception as e:
            return l1
arr=createIntArray()
print("The original array",arr)