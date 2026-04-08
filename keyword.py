import keyword
n=input("enter the keywod :")
if n in keyword.kwlist:
    print("key word is :",n)
else:
    print(n ,":is not keyword")
