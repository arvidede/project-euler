from utils import prime_factors, is_prime

N = 2000000
primes = []

for n in range(N, 1, -1):
    if is_prime(n):
        primes.append(n)

### Slower ###
# N = 2000000
# primes = set()

# for n in range(N, 1, -1):
#     if n % 2 == 0 or n % 3 == 0 or n in primes:
#         continue

#     factors = prime_factors(n)
#     if len(factors) > 1:
#         primes.update(factors)
#         continue
#     primes.add(factors[0])


print(sum(primes))
