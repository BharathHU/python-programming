def countfactor(n):
    factor_count = 0
    cycle_count = 0
    for i in range(1, n + 1):
        cycle_count += 1
        if n % i == 0:
            factor_count += 1
    return factor_count, cycle_count
n = int(input("Enter the n value: "))
resfact, rescycle = countfactor(n)
print(f"The number of factors of {n} is: {resfact}")
print(f"The number of cycles executed is: {rescycle}")