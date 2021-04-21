n = 1000
i = 0
multiples = set()
while i < n:
    if i % 3 == 0:
        multiples.add(i)
    elif i % 5 == 0:
        multiples.add(i)
    i += 1

print('Sum:', sum(multiples))

# Also
print('Sum:', sum([i if (i % 3 == 0) or (
    i % 5 == 0) else 0 for i in range(n)]))
