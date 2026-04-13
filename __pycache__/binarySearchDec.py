def intArr():
    l1 = []
    while True:
        try:
            n = int(input("Enter a number: "))
            l1.append(n)
        except:
            return l1
arr = intArr()
# 🔽 Sort first (MANDATORY)
# def sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] < arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

# sort(arr)
# print("Sorted (Descending):", arr)

# 🔍 Binary Search (Descending)
def binarySearchDsc(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1
target = int(input("Enter target: "))
index = binarySearchDsc(arr, target)
if index == -1:
    print("Element not found")
else:
    print("Element found at index:", index)