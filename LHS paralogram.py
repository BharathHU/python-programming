n=int(input("Enter n:"))
for i in range(n,(1-1),-1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,n+1):
        print("*",end="")
    print()
   