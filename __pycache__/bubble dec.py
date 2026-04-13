def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter value of n:"))
            l1.append(n)
        except Exception as e:
            return l1
arr=intArr()
print("The original array:",arr)    
def bubbleSortDec(arr):
    
    n=len(arr)
    for i in range(len(arr)):
        for j in range(0,n-i-1):
            if arr[j] <arr[j+1]:
                (arr[j],arr[j+1])=(arr[j+1],arr[j])
bubbleSortDec(arr)
print(f"The sorted bubble sort is: {arr}")