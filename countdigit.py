def counting(n):
    count=0
    while n>0:
        n=n//10 #eleminate digits
        count=count + 1
    return count
n=int(input("Entrer a number :"))
res=counting(n)
print(f"The count of digits in {n} is : {res}")