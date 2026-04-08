def sum_of_digits(n):
    if n<0:
      n =n*-1  
    sum = 0
    while n > 0:
        rem = n % 10
        sum += rem
        n //= 10
    return sum
num = int(input("Enter a number: "))
result = sum_of_digits(num)
print("Sum of digits =", result)
