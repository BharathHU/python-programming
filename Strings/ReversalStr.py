def strIncreRev(s):
    nstr=""
    for i in range(0,len(s)):
        nstr=s[i]+nstr
    return nstr
s=input("Enter a String:")
print("The original String is:",s)
res=strIncreRev(s)
print("The reversal String is:",res)

#Tracing
#