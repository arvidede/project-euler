# Let n denote layer n
# The clockwise step length between diagonal elements can then
# be described by 2n, such that for the
# 1st layer: 1 + 2 = 3, 3 + 2 = 5, 5 + 2 = 7, 7 + 2 = 9
# 2nd layer: 9 + 4 = 13, 13 + 4 = 17, 17 + 4 = 21, 21 + 4 = 25
# Thus, the sum of each layer n > 1 is determined by
# a + 2n + a + 2 * 2n + a + 3 * 2n + a + 4 * 2n = 4a + 20n
# where a is the highest element in the previous layer
#
# n | 1,   2,   3,   4,   5
# a | 1^2, 3^2, 5^2, 7^2, 9^2
#
# => a = (2n-1)^2 = 4n^2 - 4n + 1
# I.E: Sum(n) = 4 * (4n^2 - 4n + 1) + 20n = 4(4n^2 + n + 1)

# l(0) = 1, l(1) = 3, l(2) = 5, l(3) = 7
# l(l) = 2l + 1 = 1001 <=> l = 500

def sum_of_layer(n):
    if n == 0:
        return 1
    return 4 * (4 * n * n + n + 1)


def width_to_layer(w): return int((w - 1) / 2)


l = width_to_layer(1001)
layer_sums = [sum_of_layer(n) for n in range(l + 1)]

print(sum(layer_sums))
