def seggreagation(arr):
    dup,nondup,unique=[],[],[]
    dict={}
    for i in range(0,len(arr)):
        if arr[i] in dict:
            dict[arr[i]]+=1
        else:
            dict[arr[i]]=1
    for key ,val in dict.items():
        if val>1:
            dup.append(key)
        if val>=1:
            nondup.append(key)
        if val==1:
            unique.append(key)
    return dup,nondup,unique

arr=list(map(int,input("Enter a array:").split()))
print("Orginal array:",arr)
dup,nondup,unique=seggreagation(arr)
print("Duplicates:",dup)
print("Non-Duplicates:",nondup)
print("Unique:",unique)