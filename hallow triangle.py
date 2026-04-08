n = int(input("Enter a n:")) # number of rows

print("\nTriangle")
for i in range(1, n + 1):
    # Spaces for alignment
    for k in range(n, i, -1):
        print(" ", end=" ")
    # Star printing
    for j in range(1, i + 1):
        if i == n or j == 1 or j == i:
            print("*", end="  ")
        else:
            print(" ", end="  ")
    print()