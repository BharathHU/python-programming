def isprime(n):
    countfactor = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            countfactor += 1
            if i != (n // i):
                countfactor += 1
        i += 1
    return countfactor == 2
n = int(input("Enter the number: "))
flag = isprime(n)

if flag:
    print(f"\n{n} is prime")
else:
    print(f"\n{n} is not prime")
