n=int(input("Ente n:"))
countIncre=1
for i in range(1,(n+1)):
    for j in range(1,n+1):
         if i%2!=0:
            print(countIncre,end=" ")
            countDecre=countIncre
         else:
            print(countDecre,end=" ")
            countDecre-=1
         countIncre+=1
    print()
    countDecre=countDecre+n