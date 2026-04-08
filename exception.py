n=input("Enter a n:")
print(type(n))
print(n)
print("====================================")

try:
    n=int(input("Enter n:"))
    print(type(n))
    print(n)
except Exception as e:
    print(e)