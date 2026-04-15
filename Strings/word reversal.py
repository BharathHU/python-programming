def wordReverswe(s):
    s=s+" "
    newsen=""
    newword=""
    for i in range(0,len(s)):
            if s[i]!=" ":
                 newword=s[i]+newword
            elif newword !="":
                if newsen == "":
                      newsen+=newword
                else:
                    newsen=newsen+" "+newword
                newword=""
    return newsen
s=input("Enter a string:") 
print("The oroginal String is:",s)
res=wordReverswe(s)
print("The reversed String is:",res)




        