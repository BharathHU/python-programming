def gcd(num1,num2):
    lower=num1
    if num2<num1:
        lower=num2
    gcd=1
    for i in range(2,lower+1):
        if num1%i==0 and num2%i==0:
            gcd=i
    return gcd
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
res=gcd(num1,num2)
print(f"GCD of {num1} and {num2} is:{res}")