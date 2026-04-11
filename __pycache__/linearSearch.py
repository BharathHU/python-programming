def createIntArray():
    print("Enter the ele's into the array to be created")
    l1=[]
    while True:
        try:
            n=int(input("Enter num:"))
            l1.append(n)
        except Exception as e:
            return l1
def linearSearch(arr,target):
    for i in range(0,len(arr)):
       if target==arr[i]:
           return True,i
    return False,-1
arr=createIntArray()
target=int(input("enter a target:"))
flag,index=linearSearch(arr,target)
print("The original array:",arr)
if flag:
    print(f"the {target} found at index {index}")
else:
    print("the target element not in list")