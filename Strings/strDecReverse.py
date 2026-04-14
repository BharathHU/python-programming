def strDecreRev(s):
    nstr=""
    for i in range(len(s)-1,(0-1),-1):
        nstr=nstr+s[i]
    return nstr
n=input("Enter a String:")
print("The original String:",n)
res=strDecreRev(n)
print("The reversed String:",res)