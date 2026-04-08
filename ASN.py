def is_asn(n):
    temp = n
    print("before n =", n)
    if n < 0:
        n = -n
        print("after n =", n)
    count = len(str(n))
    asn_value = 0
    t = n
    while t > 0:
        digit = t % 10
        asn_value += digit ** count
        t //= 10
    print("ASN value =", asn_value)
    return asn_value == temp
n = int(input("Enter number: "))
flag = is_asn(n)
if flag:
    print(f"{n} is an ASN number")
else:
    print(f"{n} is NOT an ASN number")