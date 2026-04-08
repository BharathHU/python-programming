def Hapnum(n):
    if n==1:
        return True
    elif n==4:
        return False
    sum=0
    while n>0:
        base=n%10
        sum=sum+(base*base)
        n=n//10
    return Hapnum(sum)
num=int(input("Enter a Number:"))
res=Hapnum(num)
if res:
    print(f"The num {num} is Happy number")
else:
    print(f"The num {num} is not Happy number")
        
       
    