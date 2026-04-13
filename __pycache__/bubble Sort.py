def IntArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the array:"))
            l1.append(n)
        except Exception as e:
            return l1
arr=IntArr()
print("The original array:",arr)
def bubbleSort(arr):
    
    n=len(arr)
    for i in range(len(arr)):
        for j in range(0,n-i-1):
            if arr[j] >arr[j+1]:
                (arr[j],arr[j+1])=(arr[j+1],arr[j])
bubbleSort(arr)
print(f"The sorted bubble sort is: {arr}")