def createStrArray():
    print("Enter the ele's into the array to be created")
    l1=[]
    while True:
        n=input("Enter num:")
        if n=="":
            return l1
        l1.append(n)
arr=createStrArray()
print("The original array",arr)