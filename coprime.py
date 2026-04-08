def iscoprime(n1, n2):
    lower = min(n1, n2)
    gcd = 1
    for i in range(2, lower + 1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    return gcd == 1  
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

if iscoprime(n1, n2):
    print("Co-prime numbers")
else:
    print("Not co-prime numbers")