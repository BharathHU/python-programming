def createIntArray():
    print("Enter the ele's into the array to be created:")
    l1 = []
    while True:
        try:
            n = int(input())
            l1.append(n)
        except:
            return l1


def mergeSortMerging(arr, start, mid, end):
    i, j = start, mid + 1
    res = []

    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            res.append(arr[i])
            i += 1
        else:
            res.append(arr[j])
            j += 1

    # remaining elements
    while i <= mid:
        res.append(arr[i])
        i += 1

    while j <= end:
        res.append(arr[j])
        j += 1

    # update original array
    for k in range(len(res)):
        arr[start + k] = res[k]


def mergeSort(arr, start, end):
    if start >= end:
        return

    mid = (start + end) // 2
    mergeSort(arr, start, mid)
    mergeSort(arr, mid + 1, end)
    mergeSortMerging(arr, start, mid, end)


# main
arr = createIntArray()
print("Original Array:", arr)

mergeSort(arr, 0, len(arr) - 1)

print("Asc Sorted Array:", arr)