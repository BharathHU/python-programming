n=int(input("Enter n:"))
count=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if count%2!=0:
            print(chr(64+count),end=" ")
        else:
            print(chr(96+count),end=" ")
        count+=1
    print()