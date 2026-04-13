arr=list(map(int,input("Enter a array:").split()))
print("Orginal array:",arr)
def orderAgnosticBinarySearch(arr,target):
    start = 0
    end = len(arr) - 1
    flag="asc"
    if arr[start]>arr[end]:
        flag="desc"
    while start <= end:
        mid = (start + end) // 2
        if arr[mid]==target:
            return mid
        if flag=="asc":
            if target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target < arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
    return -1
target = int(input("Enter the target Element to be search :"))
orderAgnosticBinarySearch(arr,target)
index=orderAgnosticBinarySearch(arr,target)
if index == -1:
    print(f"Element not found: {index}")
else:
    print(f"Element found at index :{index}")