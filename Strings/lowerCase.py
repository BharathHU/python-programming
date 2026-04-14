def toLowerCase(s):
    nstr=""
    for i in range(0,len(s)):
        if "A" <=s[i]<="Z":
            nstr=nstr+chr(ord(s[i])+32)
        else:
            nstr=nstr+s[i]
    return nstr
s= input("enter a strings:")
print("original string:",s)
res=toLowerCase(s)
print("Upper to lower :",res)
