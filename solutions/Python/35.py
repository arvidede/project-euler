from utils import is_prime, rotations

MAX_N = int(1e6)
circular_primes = set()
prime_cache = {}


def check_prime(n):
    if n in prime_cache:
        return prime_cache.get(n)
    n_is_prime = is_prime(n)
    prime_cache[n] = n_is_prime
    return n_is_prime


for n in range(MAX_N):
    circular_primes.add(n)
    for rotation in rotations(n):
        if not check_prime(rotation):
            circular_primes.remove(n)
            break

print(len(circular_primes))
