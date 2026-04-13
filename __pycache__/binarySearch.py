def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter a n:"))
            l1.append(n)
        except Exception as e:
            return l1
arr=intArr()
# def sort(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j] >arr[j+1]:
#                 (arr[j],arr[j+1])=(arr[j+1],arr[j])
# sort(arr)
# print(arr)
def binarySearchAsc(arr,target):
    start=0
    end=len(arr)-1
    while start <= end:
        mid=(start+end)//2
        if target == arr[mid]:
            return mid
        if target < arr[mid]:
            end=mid-1
        else:
            start=mid+1
    return -1
target=int(input("Enter a target:"))
binarySearchAsc(arr,target)
index=binarySearchAsc(arr,target)
if index== -1:
    print(f"index not found : {index}")
else:
    print(f"Element found at index of {index}")