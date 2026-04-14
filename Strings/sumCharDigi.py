def sumCharDigits(s):
    res="" 
    sumCharDig=0
    # sum up all the character digits amd collect rest of the char
    for i in range(0,len(s)):
        if "0" <=s[i]<="9":
            sumCharDig=sumCharDig+(ord(s[i])-48)
        else:
            res=res+s[i]
    # covertion of integer to string 
    num=""
    while sumCharDig>0:
        rem=sumCharDig%10
        num=chr(rem+48)+num
        sumCharDig=sumCharDig//10
    return(res+num)


s=input("enter a strings:")
print("original string ",s)
res=sumCharDigits(s)
print("the summed string :",res)
