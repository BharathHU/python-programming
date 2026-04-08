def sumofdigits(n):
    if n == 0:  
        return 0
    else:
        return (n % 10) + sumofdigits(n // 10) 
num = int(input("Enter a number: "))
result = sumofdigits(num)
print("Sum of digits:", result)
    