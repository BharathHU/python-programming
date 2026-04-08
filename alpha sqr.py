n=int(input("Enter a n:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i%2!=0:
            print(chr(96+j),end=" ")
        else:
            print(chr(64+j),end=" ")
    print()