def intarray():
    l1=[]
    while True:
        try:
            n=int(input("enter a number:"))
            l1.append(n)
        except Exception as e:
            return l1

def findmaxele(arr):
    minele,minend=2**32,-1
    for i in range (0,len(arr)):
        if arr[i]<minele:
            minele=arr[i]
            minend=i
    return minele,minend

arr=intarray()
print("Orginal Array:",arr)

resMin,resMinend=findmaxele(arr)
print(f"The max ele in the arr is: {resMin} at index :{resMinend}")