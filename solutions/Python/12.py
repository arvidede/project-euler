from utils import prime_factors, product, number_of_factors
from collections import Counter

# Factor formula: N = (a+1)(b+1)(c+1)...
# where n = alpha^a * beta^b + gamma^c...

num_factors = 0
i = 2
ith_triangle_number = 1
while num_factors < 500:
    ith_triangle_number += i
    num_factors = number_of_factors(ith_triangle_number)
    i += 1

print(i, ith_triangle_number, num_factors)
