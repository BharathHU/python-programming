def fibo1(position):
    n1=0
    n2=1
    while position > 0:
        print(n1,end="  ")
        temp=n1+n2
        n1=n2
        n2=temp
        position -=1
    return fibo1
position=int(input("enter the number:"))
res=fibo1(position)