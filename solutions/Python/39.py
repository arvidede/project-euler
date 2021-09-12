# p = a + b + c
# a <= b <= c
# a <= p/3, b <= 2p/3
# c = sqrt(a^2 + b^2)

from math import ceil, floor

from utils import argmax

MAX_P = 1000


combinations = []

for p in range(MAX_P + 1):
    num_right_angles = 0
    for a in range(1, ceil(p / 3)):
        for b in range(floor(p / 3), ceil(2 * p / 3)):
            num_right_angles += a ** 2 + b ** 2 == (p - a - b) ** 2
    combinations.append(num_right_angles)


print(argmax(combinations))
