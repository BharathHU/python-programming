# WAp to segrigate between duplicate and non duplicate and unique present in an array
arr=[1,2,2,1,3,1,4]
for i in range(len(arr)):
    if arr[i] in arr[:i]+arr[i+1:]:
        print(f"{arr[i]} is duplicate")
    else:
        print(f"{arr[i]} is unique")
    