MAX_N = int(1e6)


def is_palindromic(string: str) -> bool:
    return string == string.lstrip('0')[::-1]


palindromic = [n for n in range(MAX_N) if is_palindromic(
    str(n)) and is_palindromic(bin(n)[2:])]

print(sum(palindromic))
