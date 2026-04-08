def intArr():
    arr=[]
    while True:
        try:
            n=int(input("Enter a Array Element:"))
            arr.append(n)
        except Exception as e:
            return arr
def findMaxEle(arr):
    maxEle,maxEleInd=-2**32,-1
    for i in range(0,len(arr)):
        if arr[i]>maxEle:
            maxEle=arr[i]
            maxEleInd=i
    return maxEle,maxEleInd
arr=intArr()
print("Original array is",arr)
resMax,resMaxInd=findMaxEle(arr)
print(f"the max element in array is {resMax} at index of {resMaxInd}")