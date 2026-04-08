def ispalindrome(n):
    temp=n
    rev=0
    rem=n%10
    rev=(rev*10)+n
    n=n//10
n=int(input("enter the value:"))
res=ispalindrome(n)
if res:
    print(f"it is palindrome :{n}")
else:
    print("not palindrome")
    
    