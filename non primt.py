def isnonprime(n):
    if n < 2:
        return True 
    countfactor = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            countfactor += 1
            if i != (n // i):
                countfactor += 1
        i += 1
    return countfactor != 2 
n = int(input("Enter how many non-prime numbers to print: "))
if n <= 0:
    print("Invalid input")
else:
    print(f"First {n} non-prime numbers are:")
    count = 0
    num = 0
    while count < n:
        if isnonprime(num):
            print(num, end=" ")
            count += 1
        num += 1
