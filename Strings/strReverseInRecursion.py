def strReverseRecurtion(s,nstr,i):
    if i>= len(s):
        return nstr
    nstr=s[i]+nstr
    return strReverseRecurtion(s,nstr,(i+1))
s=input("Enter a String:")
print("The original String:")
res=strReverseRecurtion(s,"",0)
print("The reversed String By Using Recurstion is:",res)