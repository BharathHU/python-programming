def strFilterations(s):
    nstr=""
    for i in range(0,len(s)):
        if "A" <= s[i] <="Z":
            nstr=nstr+chr(ord(s[i])+32)
        elif "a" <= s[i] <="z":
            nstr=nstr + s[i]
    return nstr
def isPanagram(s):
    s=strFilterations(s)
    if len(s)<26:
        return False
    else:
        dict={}
        for i in range(0,len(s)):
            if s[i] in dict:
                dict[s[i]]+dict[s[i]]+1
            else:
                dict[s[i]]=1
        return len(dict) ==26
s=input("Enter a string:")

flag=strFilterations(s)
if flag:
    print("It is panagram")
else:
    print("Not Anagram")