def createIntArr():
    arr = []
    while True:
        try:
            n = int(input("Enter element: "))
            arr.append(n)
        except:
            return arr
def reverseArr(arr):
    l1=[]
    for i in range((len(arr)-1),0-1,-1):
        l1.append(arr[i])
    return l1
arr=createIntArr()
print("Original Array:",arr)
res=reverseArr(arr)
print("Reversed Array:",res)