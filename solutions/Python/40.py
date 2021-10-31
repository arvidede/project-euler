from utils import product

exponents = range(7)
nums = "".join(map(str, range(10 ** max(exponents))))
print(product([int(nums[10**t]) for t in exponents]))
