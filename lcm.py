def Lcm(n1,n2):
    lcm=n1
    if n2>n1:
        lcm=n2
        while lcm<=(n1*n2):
            if lcm%n1==0 and lcm%n2==0:
                return lcm
            i+=1
num1=int(input("enter the num1 value:"))
num2=int(input("enter the num2 value:"))
res=Lcm(num1,num2)
print(res)