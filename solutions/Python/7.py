from utils import prime_factors

# I'm an ape
primes = set()
n = 10001
i = 1
while len(primes) < n:
    primes = primes.union(set(prime_factors(i)))
    i += 1


sorted_primes = sorted(list(primes))
print(sorted_primes[n-1])
