def sumCharcterDigits(s):
    res=""
    sumCharDig = 0

    # sum up all the character digits and collect rest of the char
    for i in range(0,len(s)):
        if "0" <= s[i] <= "9":
            sumCharDig = sumCharDig + (ord(s[i]) - 48)
        else:
            res = res + s[i]

#( logic 1)
    # conversion of intger to string 
    # num=""
    # while sumCharDig > 0:
    #     rem = sumCharDig % 10
    #     num = chr(rem + 48) + num
    #     sumCharDig = sumCharDig // 10
    # return (res + num)

#( logic 2)
    # eassy method to convert integer to string 
    num = str(sumCharDig)
    return (res + num)


s = input("enter the string")
print("the original string is: ", s)
res = sumCharcterDigits(s)
print(" The summed str is: ", res)-