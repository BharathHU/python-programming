def is_even(n):
    return n % 2 == 0

sr = int(input("Enter your start range: "))
er = int(input("Enter your end range: "))

if er < sr:
    print("Invalid range! End range should be greater than or equal to start range.")
else:
    print("Even numbers:")
    for i in range(sr, er + 1):
        if is_even(i):
            print(i, end=" ")

    print("\nOdd numbers:")
    for i in range(sr, er + 1):
        if not is_even(i):
            print(i, end=" ")
