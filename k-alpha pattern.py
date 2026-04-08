n=int(input("Enter n:"))
noc=1
for i in range(1,n*2):
    for j in range(noc,n+1):
        print(chr(96+noc),end=" ")
    if i<n:
        noc+=1
    else:
        noc-=1
    print()