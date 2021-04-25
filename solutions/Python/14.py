def collatz_sequence(n, cache):
    def next(x): return int(n / 2) if n % 2 == 0 else 3 * n + 1
    length = 1
    while n > 1:
        if n in cache:
            return length + cache[n]
        n = next(n)
        length += 1
    return length


cache = dict()

for i in range(int(1e6)):
    cache[i] = collatz_sequence(i, cache)

max_key = max(cache, key=cache.get)

print(f"{max_key}: {cache[max_key]}")
