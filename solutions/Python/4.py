# Hmm

N = 1000
largest = 0
factors = []

for n1 in reversed(range(100, N)):
    for n2 in reversed(range(100, n1)):
        product = n1 * n2
        if product > largest:
            product = str(product)
            if product == product[::-1]:
                largest = int(product)
                factors = [n1, n2]

print(largest, factors)
