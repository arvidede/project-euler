from utils import is_prime

cache = {}
truncatable_primes = set()


def is_truncatable_prime(num, direction=1):
    num_str = str(num)
    while len(num_str) > 0:
        if int(num_str) in truncatable_primes:
            break

        if cache.get(num_str, None) == False or not is_prime(int(num_str)):
            if not num_str in cache:
                cache[num_str] = False
            return False

        cache[num_str] = True
        num_str = num_str[::direction][1:][::direction]

    return True if direction == -1 else is_truncatable_prime(int(str(num)[:-1]), -1)


MAX_NUM_PRIMES = 11
i = 11

while len(truncatable_primes) < MAX_NUM_PRIMES:
    if is_truncatable_prime(i):
        truncatable_primes.add(i)
    i += 1


print(sum(truncatable_primes), truncatable_primes)
