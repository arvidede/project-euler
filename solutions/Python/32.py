from utils import permutations, ints_to_int

numbers = list(range(1, 10))
pandigital = set()

for permutation in permutations(numbers):
    for multiplicand_delimiter in range(1, len(permutation) - 2):
        for multiplier_delimiter in range(multiplicand_delimiter + 1, len(permutation) - 1):
            multiplicand = ints_to_int(permutation[:multiplicand_delimiter])
            multiplier = ints_to_int(
                permutation[multiplicand_delimiter:multiplier_delimiter])
            product = ints_to_int(permutation[multiplier_delimiter:])
            if(multiplier * multiplicand == product):
                pandigital.add(product)

print(sum(pandigital))
