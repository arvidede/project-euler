digits = open('./inputs/13.txt', 'r').read().split('\n')

# Column-wise addition. Ape strong

n = len(digits)
length = len(digits[0])
sum_ = ""
memory = 0
columns = [0] * length


for i in reversed(range(length)):
    col_sum = str(memory + sum([int(digit[i]) for digit in digits]))
    memory = int(col_sum[:-1])
    columns[i] = col_sum[-1]

columns.insert(0, str(memory))

print("".join(columns)[:10])
