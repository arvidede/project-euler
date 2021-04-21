def prime_factors(n):
    factors = []
    k = 2

    while n >= k:
        if n % k == 0:
            factors.append(k)
            n = n / k
            continue
        k += 1

    return factors


print('Prime factor:', max(prime_factors(600851475143)))
