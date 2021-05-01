from dotenv import load_dotenv
import requests
import os
from functools import reduce
from math import factorial
from collections import Counter
from typing import Generator


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
def is_prime(n: int) -> bool:
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


def prime_factors(n: int) -> list:
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


def gcd(a: int, b: int) -> int:
    while b != 0:
        prev_b = b
        b = a % b
        a = prev_b
    return a


def product(list_: list) -> int:
    return reduce(lambda a, b: int(a)*int(b), list_, 1)


def parse_number_grid(grid_string):
    return [[int(cell) for cell in line.split(' ')] for line in grid_string.split('\n')]


def flatten(list_) -> list:
    return [item for sublist in list_ for item in sublist]


def number_of_factors(n):
    primes = prime_factors(n)
    occurences = Counter(primes)
    return product([occurences[key] + 1 for key in occurences])


def factorials(n: int) -> Generator[int, None, None]:
    i, prev = 0, 1
    while i <= n:
        yield prev
        i, prev = i + 1, prev * (i + 1)


def factorial(n: int) -> Generator[int, None, None]:
    i, prev = 0, 1
    while i < n:
        i, prev = i + 1, prev * (i + 1)
    yield prev
