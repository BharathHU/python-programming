def is_non_integer_palindrome(x):
    s = str(x)
    return '.' in s and s == s[::-1]  
count = int(input("Enter how many non-integer palindromes you want: "))
num = 0.1
found = 0
while found < count:
    s = f"{num:.3f}".rstrip('0').rstrip('.')
    if is_non_integer_palindrome(s):
        print(s, end=" ")
        found += 1
    num += 0.1
    num = round(num, 3)