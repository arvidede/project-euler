def divisors(n):
    return [k for k in range(1, n) if n % k == 0]


def d(x): return sum(divisors(x))


amicable = []

for a in range(10000):
    b = d(a)
    if b not in amicable and a != b and d(b) == a:
        amicable.append(a)
        amicable.append(b)

print(sum(amicable))
