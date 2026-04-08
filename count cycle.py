def countcycle(n):
    count = 0      # total number of factors
    cycle = 0      # number of loop iterations
    i = 1
    while i * i <= n:  
        cycle += 1   # counting each iteration as one cycle

        if n % i == 0:    # i is a factor
            count += 1
            print(i, end=" ")

            if i != n // i:   # avoid double counting for perfect squares
                count += 1
                print(n // i, end=" ")

        i += 1

    return count, cycle


num = int(input("Enter the value: "))
factors, cycles = countcycle(num)

print("\nNumber of factors:", factors)
print("Number of cycles:", cycles)