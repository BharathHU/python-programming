def createIntArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter a Array"))
            l1.append(n)
        except Exception as e:
            return l1
def findSecMin(arr):
    minEle,minEleInd=2**32,-1
    secMinEle,secMinEleInd=2**32,-1
    for i in range(0,len(arr)):
        if minEle>arr[i]:
            secMinEle,secMinEleInd=minEle,minEleInd
            minEle,minEleInd=arr[i],i
        elif minEle !=arr[i] and secMinEle > arr[i]:
            secMinEle,secMinEleInd = arr[i],i
    return [minEle,minEleInd,secMinEle,secMinEleInd]
arr=createIntArr()
print("The original array:")
res=findSecMin(arr)
print("The Min Ele",res[0],"at index",res[1])
print("The Sec Min",res[2],"at index",res[3])