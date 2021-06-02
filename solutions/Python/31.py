# coins = [100, 50, 20, 10, 5, 2, 1]
# combinations = [[200]]

# for base_coin in coins:
#     for i, _ in enumerate(coins):
#         combination = [base_coin]
#         rest = 200 - base_coin
#         for coin in coins[i:]:
#             while rest >= coin:
#                 combination.append(coin)
#                 rest -= coin
#         combinations.append(combination)


# print(len(set(tuple(sorted(c)) for c in combinations)))

# Didn't work, let's go full ape mode

TOTAL = 200


def polynomial(a, b, c, d, e, f, g):
    return 100 * a + 50 * b + 20 * c + 10 * d + 5 * e + 2 * f + g


def nrange(n):
    return range(0, (TOTAL // n) + 1)


combinations = []

# Ape strong
# 1 280 000 000
for a in nrange(100):
    for b in nrange(50):
        for c in nrange(20):
            for d in nrange(10):
                for e in nrange(5):
                    for f in nrange(2):
                        for g in nrange(1):
                            if polynomial(a, b, c, d, e, f, g) == TOTAL:
                                combinations.append((a, b, c, d, e, f, g))


print(len(set(combinations)) + 1)  # 200
