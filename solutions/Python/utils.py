from dotenv import load_dotenv
import requests
import os


def submit(problem):
    load_dotenv()
    url = f'https://projecteuler.net/problem={problem}'
    response = requests.post(
        url, cookies={'PHPSESSID': os.getenv('SESSION_COOKIE')})
    if response.status_code == 200:
        print('Believe it or not, but that is actually correct. Lucky guess.')
    else:
        print("Why are you even trying?")


def prime_factors(n):
    factors = []
    k = 2

    while n >= k:
        if n % k == 0:
            factors.append(k)
            n = n / k
            continue
        k += 1

    return factors
