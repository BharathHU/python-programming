def isprimenum(n):
    if n < 2:
        return False
    countfactor = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            countfactor += 1
            if i != (n // i):
                countfactor += 1
        i += 1
    return countfactor == 2
sr = int(input("Enter the Start range: "))
er = int(input("Enter the End range: "))

if sr > er:
    print("Invalid Range")
flog=isprimenum(n)
print(f"\n Prime numbers are:")
for n in range(sr,er+1):
    if isprimenum(n):
        print(n,end=" ")
print(f"\n Non palindromes are:")
for n in range(sr,er+1):
    if not isprimenum(n):
        print(n,end=" ")