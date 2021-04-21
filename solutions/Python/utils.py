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
