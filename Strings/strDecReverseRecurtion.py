def strReverDecreRecur(s,nstr,i):
    if i<=0:
        return nstr
    nstr+=s[i]
    return strReverDecreRecur(s,nstr,i-1)
s=input("Enter a string:")
print("The original String:",s)
res=strReverDecreRecur(s,"",len(s)-1)
print("The Reversed String is:",res)