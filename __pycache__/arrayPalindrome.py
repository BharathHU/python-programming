def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter a n:"))
            l1.append(n)
        except Exception as e:
            return l1
arr=intArr()
print("The original arr is:",arr)
def palindromearray(arr):
    i,j=0,len(arr)-1
    while i<j:
        if arr[i]!=arr[j]:
            return False
        i += 1
        j -= 1
    return True
flag=palindromearray(arr)
if flag:
    print("Array is Palindrome")
else:
    print("Array is Not Palindrome")