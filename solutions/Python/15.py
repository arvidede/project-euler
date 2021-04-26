from math import comb


def lattice_paths(a, b):
    # number of paths from (0, 0) to (a, b) ~ a + b choose a
    return comb(a + b, a)


print(lattice_paths(20, 20))
