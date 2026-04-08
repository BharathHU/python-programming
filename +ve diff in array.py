def intarray():
    l1 = []
    while True:
        try:
            n = int(input("Enter a number: "))
            l1.append(n)
        except:
            return l1
arr = intarray()
def finddiff(arr):
    prod = 1
    total_sum = 0
    for i in range(len(arr)):
        total_sum += arr[i]
        prod *= arr[i]
    diff = prod - total_sum
    if diff < 0:
        diff = -diff
    return diff
result = finddiff(arr)
print("Array:", arr)
print("Absolute Difference (Product - Sum):", result)