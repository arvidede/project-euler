from utils import is_pandigital, check_primality, generate_primes

MAX = 987654321
primes = generate_primes(MAX)

for p in primes[::-1]:
    if is_pandigital(p):
        print(p)
        break
