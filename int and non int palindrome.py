# WAP to print all the integer and non-integer palindromes present in a user-defined range separately.
def ispalindrome(n):
    temp = n
    if n < 0:
        n = -n
    rev = 0
    while n > 0:
        rem = n % 10
        rev = (rev * 10) + rem
        n //= 10
    if temp < 0:
        rev = -rev
    return rev == temp
sr = int(input("Enter the start range: "))
er = int(input("Enter the end range: "))

if sr > er:
    print("Invalid input!!")
else:
    print("\nInteger Palindromes:")
    for n in range(sr, er + 1):
        if ispalindrome(n):
            print(n, end=" ")

    print("\n\nNon-Integer Palindromes:")
    for n in range(sr, er + 1):
        if not ispalindrome(n):
            print(n, end=" ")
