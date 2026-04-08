n=int(input("Enter a n:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1:
            print(chr(64+4),end=" ")
        elif j==3:
            print(chr(64+2),end=" ")
        elif j==2:
            print(chr(96+3),end=" ")
        else:
            print(chr(96+1),end=" ")
    print()