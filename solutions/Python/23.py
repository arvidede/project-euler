from utils import divisors

# Naive approach, for future reference:
# 1. Find all abundant numbers up to 28123
# 2. Find all sums of abundant numbers:
#       - Given: Above 28123 can be written as sum of two abundant numbers
#       - Add all sums lte 28123 to set
# 3. Create set of all numbers up to 28123 not in 2s set

n = 28123

abundant_numbers = [i for i in range(1, n+1) if sum(divisors(i)) > i]
sums_of_abundant_numbers = set()

for upper in reversed(range(0, len(abundant_numbers))):
    for lower in range(upper+1):
        sum_ = abundant_numbers[upper] + abundant_numbers[lower]
        if sum_ > n:
            continue
        sums_of_abundant_numbers.add(sum_)

print(sum([i for i in range(n+1) if i not in sums_of_abundant_numbers]))
