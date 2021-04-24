# [1-20] ~ [11, 20]
# 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19

nums = range(11, 21)

n = max(nums)
i = 1

while not all([n * i % num == 0 for num in nums[:-1]]):
    i += 1

print(n*i)
