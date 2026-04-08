def ispalindrome(num):
    temp = num
    n = abs(num)
    rev = 0
    while n > 0:
        rem = n % 10
        rev = (rev * 10) + rem
        n //= 10
    if temp < 0:
        rev = -rev
    return rev == temp
count = int(input("Enter how many palindromes you want: "))
num = 1
found = 0
while found < count:
    if ispalindrome(num):
        print(num, end=" ")
        found += 1
    num += 1