def product_of_digits(n):
    if n < 0:
        return -1   # invalid
    prod = 1
    while n > 0:
        digit = n % 10
        prod *= digit
        n //= 10
    return prod
n = int(input("Enter a number: "))
result = product_of_digits(n)
if result == -1:
    print("Invalid number")
else:
    print("Product of digits =", result)