import os
from collections import Counter
from functools import reduce
from typing import Generator

import requests
from dotenv import load_dotenv


def submit(problem, answer):
    load_dotenv()
    url = f"https://projecteuler.net/problem={problem}"
    response = requests.post(
        url, json={"answer": answer}, cookies={"PHPSESSID": os.getenv("SESSION_COOKIE")}
    )
    if response.status_code == 200:
        return "Believe it or not, but that is actually correct. Lucky guess."
    else:
        return "Why are you even trying?"


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


def check_primality():
    cache = {}

    def check_primality_(n):
        if n in cache:
            return cache.get(n)
        n_is_prime = is_prime(n)
        cache[n] = n_is_prime
        return n_is_prime
    return check_primality_


def generate_primes(n: int) -> list[int]:
    """
    Sieve of Eratosthenes: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    Source: https://stackoverflow.com/a/3035188
    """
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def prime_factors(n: int) -> list[int]:
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


def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b)


def product(list_: list) -> int:
    return reduce(lambda a, b: int(a) * int(b), list_, 1)


def parse_number_grid(grid_string):
    return [[int(cell) for cell in line.split(" ")] for line in grid_string.split("\n")]


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


def divisors(n: int) -> list[int]:
    return [k for k in range(1, n) if n % k == 0]


# https://code.activestate.com/recipes/252178/
def permutations(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        yield nums
    else:
        for perm in permutations(nums[1:]):
            for i in range(len(perm) + 1):
                yield perm[:i] + nums[0:1] + perm[i:]


def fibonacci(n):
    f_n_1, f_n = 0, 1
    for i in range(n):
        yield f_n
        f_n_1, f_n = f_n, f_n_1 + f_n


def ints_to_int(ints: list[int]) -> int:
    return int("".join([str(n) for n in ints]))


def rotations(num: int) -> list[int]:
    num = str(num)
    for i in range(len(num)):
        yield int(num[i:] + num[:i])


def argmax(nums: list[int]) -> int:
    def f(i): return nums[i]
    return max(range(len(nums)), key=f)


def is_pandigital(n: int) -> bool:
    n_str = str(n)
    n_set = set(n_str)
    return "0" not in n_set \
        and len(n_set) == len(n_str) \
        and len(n_set) == int(max(n_set))
