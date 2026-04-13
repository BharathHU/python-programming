def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter a n:"))
            l1.append(n)
        except Exception as e:
            return l1
arr=intArr()
print("The original array is",arr)
def insertionSort(arr):
    n=len(arr)
    for i in range(0,n-1):
        for j in range(i+1,0,-1):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
            else:
                break
insertionSort(arr)
print("Sorted array is",arr)