print("left angle triangle")
for i in range(1,n+1):
    for j in range(1,i+1):
        if i ==n or j==1 or i==j:
            print("*",end=" ")
        else:
            print(' ',end=" ")
    print()