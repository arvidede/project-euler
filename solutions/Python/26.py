from utils import is_prime


# Decimal expansion
def reciprocal_cycle(d):
    a, i = 1, 0
    while True:
        a = a * 10 % d
        if a == 1:
            return i
        i += 1


# To avoid infinite loops
primes = [p for p in range(1000) if is_prime(p)][3:]
max_d = (0, 0)

for d in primes:
    cycle_len = reciprocal_cycle(d)
    if cycle_len > max_d[1]:
        max_d = (d, cycle_len)

print(max_d)
