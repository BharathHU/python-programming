def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter a n:"))
            l1.append(n)
        except Exception as e:
            return l1
arr=intArr()
print("The original arr is:",arr)
k=int(input("Enter the num of rotation"))
def reversalArray(arr,i,j):
 
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
def leftrotation(arr,k):
    n=len(arr)
    if k>=n:
        k=k%n
    reversalArray(arr,0,(k-1))
    reversalArray(arr,k,(n-1))
    reversalArray(arr,0,(n-1))
leftrotation(arr,k)
print("Rotated array is:",arr)