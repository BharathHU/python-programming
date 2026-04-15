#wap to check whether the give string is palindrome or not.
#
def strFilterations(s):
    nstr=""
    for i in range(0,len(s)):
        if "A" <=s[i]<= "Z":
            nstr=nstr+chr(ord(s[i])+32)
        elif ("0" <= s[i] <="9") or ("a" <= s[i] <= "z"):
            nstr=nstr+s[i]
    return nstr
def isstringPalindrome(s):
    s=strFilterations(s)
    left,right=0,len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left +=1
        right-=1
    return True
s=input("Enter a string:")
flag=isstringPalindrome(s)
if flag:
    print("String palindrome")
else:
    print("Not a String palindrome")
