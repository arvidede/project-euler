from dotenv import load_dotenv
import requests
import os
from functools import reduce
from math import factorial
from collections import Counter


def submit(problem):
    load_dotenv()
    url = f'https://projecteuler.net/problem={problem}'
    response = requests.post(
        url, cookies={'PHPSESSID': os.getenv('SESSION_COOKIE')})
    if response.status_code == 200:
        print('Believe it or not, but that is actually correct. Lucky guess.')
    else:
        print("Why are you even trying?")


# https://en.wikipedia.org/wiki/Primality_test#Simple_methods
def is_prime(n):
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_factors(n):
    factors = []
    k = 2

    while n > k:
        if n % k == 0:
            factors.append(k)
            n = n / k
            continue
        k += 1

    if k == n:
        factors.append(n)

    return factors


def gcd(a, b):
    while b != 0:
        prev_b = b
        b = a % b
        a = prev_b
    return a


def product(list_):
    return reduce(lambda a, b: int(a)*int(b), list_)


def parse_number_grid(grid_string):
    return [[int(cell) for cell in line.split(' ')] for line in grid_string.split('\n')]


def flatten(list_):
    return [item for sublist in list_ for item in sublist]


def number_of_factors(n):
    primes = prime_factors(n)
    occurences = Counter(primes)
    return product([occurences[key] + 1 for key in occurences])
