def toLowerCase(s):
    nstr=""
    for i in range(0,len(s)):
        if "A" <=s[i]<="Z":
            nstr=nstr+chr(ord(s[i])+32)
        else:
            nstr=nstr+s[i]
    return nstr
def toUpperCase(s):
    nstr=""
    for i in range(0,len(s)):
        if "a" <=s[i]<="z":
            nstr=nstr+chr(ord(s[i])-32)
        else:
            nstr=nstr+s[i]
    return nstr
def toSwap(s):
    nstr=""
    for i in range(0,len(s)):
        if "a" <=s[i]<="z":
            nstr=nstr+chr(ord(s[i])-32)
        elif "A" <=s[i]<="Z":
             nstr=nstr+chr(ord(s[i])+32)
        else:
            nstr=nstr+s[i]
    return nstr
s= input("enter a strings:")
res=toLowerCase(s)
print("Upper to lower :",res)
res=toUpperCase(s)
print("Lower to upper :",res)
res=toSwap(s)
print("swap :",res)