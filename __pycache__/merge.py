def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter val:"))
            l1.append(n)
        except Exception as e:
            return l1
def mergeAlternative(arr1,arr2):
    res=[]
    n1,n2=len(arr1),len(arr2)
    i,j=0,0
    #the imaginary cursor on res
    for k in range(0,(n1+n2)):
        if i<n1 and k%2==0:
            res.append(arr1[i])
            i+=1
        elif j<n2 and k%2!=0:
            res.append(arr2[j])
            j+=1
        else:
            if i<n1:
                res.append(arr1[i])
                i+=1
            else:
                if j<n2:
                    res.append(arr2[j])
                    j+=1
    return res                  
arr1=intArr()
print("Array1:",arr1)
arr2=intArr()
print("Array2:",arr2)
res=mergeAlternative(arr1,arr2)
print("The marged sort is:",res)               