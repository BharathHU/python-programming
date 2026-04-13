def intarr():
    l1=[]
    while True:
        try:
            n=int(input("enter a value"))
            l1.append(n)
        except:
            return l1
def reverseArr(arr):
    i,j=0,len(arr)-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
arr=intarr()
print("original array:",arr)
reverseArr(arr)
print("reversed array:",arr)