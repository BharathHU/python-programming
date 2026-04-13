def ascmergeArray(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    i = 0
    j = 0
    res = []
    for k in range(0, n1 + n2):
        if i < n1 and j < n2:
            if arr1[i] <= arr2[j]:
                res.append(arr1[i])
                i = i + 1
            else:
                res.append(arr2[j])
                j = j + 1
        else:
            if i < n1:
                res.append(arr1[i])
                i = i + 1
            elif j < n2:
                res.append(arr2[j])
                j = j + 1
    return res
# Input
arr1 = list(map(int, input("Enter array 1: ").split()))
arr2 = list(map(int, input("Enter array 2: ").split()))
# Output
print("Initial Array:")
print("array1:", arr1)
print("array2:", arr2)
res = ascmergeArray(arr1, arr2)
print("ASC Merge Array:", res)