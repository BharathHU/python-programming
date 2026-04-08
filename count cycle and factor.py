def count_cycles_and_factors(n):
    count_fact = 0
    count_cycle = 0
    print(f"The factors of {n} are:", end=" ")
    for i in range(1, n+1):
        count_cycle += 1
        if n % i == 0:
            print(i, end=" ")
            count_fact += 1
    print()  # newline after printing factors
    return count_fact, count_cycle

num = int(input("Enter a number: "))
fact_count, cycle_count = count_cycles_and_factors(num)
print(f"Number of factors = {fact_count}")
print(f"Number of cycles (iterations) = {cycle_count}")