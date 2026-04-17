#WAP to check whether the given two strings are anagrams or not
# anagrams:
## given two strings are said to be anagrams if and only if both the strings are consists of the same numbers of occurences,
# ignoring the casing,special symbols,chr digits and speces.

#Example 1:
#s1="A31Bc,#D"-->"abcd"
#s2="5Db c1A"-->"dbca"
#anagrams
#=========================================================================
#Example 2:
#s1="xezyy" -->"xezyy"
#s2="YeZYx"--> "yezyx"
#Anagrams
#=========================================================================
#Example 3:
#s1="e r a" --> "era"
#s2="^6 e e E" --> "eee"
#not a anagrams
#=========================================================================
#Example 4:
#s1="app" --> "app"
#s2="paa" --> "paa"
#not an anagrams
def strFilter(str):
    newstr=""
    for i in range(0,len(str)):
        if "A" <= str[i] <="Z":
            newstr=newstr+chr(ord(str[i])+32)
        elif "a"<= str[i] <= "z" or "0" <= str[i] <= "9":
            newstr=newstr+str[i]
    return newstr
def anagram(s1,s2):
    s1=strFilter(s1)
    s2=strFilter(s2)
    if len(s1) !=len(s2):
        return False
    else:
        dict={}
        for i in range(0,len(s1)):
            if s1[i] in dict:
                dict[s1[i]]+=1
            else:
                dict[s1[i]]=1
            if s2[i] in dict:
                dict[s2[i]] -=1
            else:
                dict[s2[i]]=-1
        for key,value in dict.items():
            if value!=0:
                return False
        return True
s1=input("Enter a string:")
s2=input("Enter a string:")
flag=anagram(s1,s2)
if flag:
    print("Anagram")
else:
    print("Not a Anagram")