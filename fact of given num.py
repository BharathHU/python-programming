def countfact(n):
    count=0
    for i in range(1,(n+1)):
        if n%i==0:
            print(i,end=" ")
        count=count+1
    return count
num=int(input("Enter a number:"))
print(f" the factor of {num} is:")
result=countfact(num)
print(f"\n the num of factors {num} is:{result}")
