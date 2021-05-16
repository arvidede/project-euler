from utils import is_prime

# Ape strong


def quadratic(n, a, b):
    return n * (n + a) + b


max_coef = [0, 0, 0]

for a in range(-1000, 1000):
    for b in range(-1000, 1001):
        n = 0
        while is_prime(quadratic(n, a, b)):
            if n >= max_coef[0]:
                max_coef = [n, a, b]
            n += 1

print(max_coef, max_coef[1] * max_coef[2])
