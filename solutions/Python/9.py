# a < b < c
# a^2 + b^2 = c^2
# a + b + c = 1000
# Euclid: a = k(m^2 - n^2), b = 2mnk, c = k(m^2 + n^2)
# K(2m^2 + 2mn) = 1000 <=> km(m + n) = 500
# m, n, k > 0, m > n, gcd(m, n) = 1, (m+n) % 2 = 1
# 500 % (m | n | k) = 0
# abc = k^3 * 2m * (m^4 - n^4)

from utils import prime_factors, multiply, gcd
from itertools import combinations
from collections import namedtuple


def euclid_pythagorean_triple():
    return_type = namedtuple('Data', 'abc a b c')
    primes = prime_factors(500)
    all_combinations = set([1])  # Not returned as a prime

    for i in range(1, len(primes) + 1):
        all_combinations.update([multiply(tuple_)
                                 for tuple_ in combinations(primes, i)])

    valid_set = sorted(all_combinations)

    for k in valid_set:
        for n, i in enumerate(valid_set):
            for m in valid_set[i:]:
                if gcd(m, n) == 1 and k * m * (m + n) == 500:
                    return return_type(k ** 3 * 2 * m * (m ** 4 - n ** 4),
                                       k * (m ** 2 - n ** 2),
                                       2 * m * n * k,
                                       k * (m ** 2 + n ** 2))


print(euclid_pythagorean_triple())
