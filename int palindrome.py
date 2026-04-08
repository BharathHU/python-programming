def isrev(n,rev,temp):
     if n<=0:
         return rev==temp
     rem=n%10
     rev=(rev*10)+rem
     n=n//10
     return isrev(n,rev,temp)
num=int(input("Enter the num:"))
flag=isrev(num,0,num)
if flag:
    print(f" {num} Int pali")
else:
    print(f"{num} Not an Int pali")