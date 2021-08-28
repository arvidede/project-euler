from utils import product, gcd, lcm
non_trivial_fractions = set()
MAX_N = 4
denominator = 11

while len(non_trivial_fractions) < MAX_N:
    numerator = 10
    while numerator < denominator:
        num_str = str(numerator)
        den_str = str(denominator)
        common_nums = set(num_str).intersection(set(den_str))
        common_nums.discard("0")
        if len(common_nums) > 0:
            for common in common_nums:
                num = int(num_str.replace(common, '', 1))
                den = int(den_str.replace(common, '', 1))
                if num and den and num / den == numerator / denominator:
                    non_trivial_fractions.add((numerator, denominator))
        numerator += 1
    denominator += 1

numerators, denominators = list(
    map(product, zip(*list(non_trivial_fractions))))

print(denominators / gcd(numerators, denominators))
