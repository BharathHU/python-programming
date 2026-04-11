def intArr():
    arr = []
    while True:
        try:
            n = int(input("Enter an Array Element: "))
            arr.append(n)
        except Exception:
            return arr
def findMinEle(arr):
    minEle, minEleInd = 2**32, -1  
    for i in range(len(arr)):
        if arr[i] < minEle:
            minEle = arr[i]
            minEleInd = i
    
    return minEle, minEleInd
arr = intArr()
print("Original array is", arr)
resMin, resMinInd = findMinEle(arr)
print(f"The minimum element in array is {resMin} at index {resMinInd}")