def isprime(n):
    if n < 2:
        return False
    countfactor = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            countfactor += 1
            if i != (n // i):
                countfactor += 1
        i += 1
    return countfactor == 2
N = int(input("Enter how many prime numbers to print: "))

if N <= 0:
    print("Invalid choice")
else:
    print("First", N, "prime numbers are:")
    count = 0
    num = 2  
    while count < N:
        if isprime(num):
            print(num, end=" ")
            count += 1
        num += 1