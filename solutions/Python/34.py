from utils import factorials

factorials = list(factorials(9))
curious_numbers = []

for n in range(3, 9999999):
    if n == sum([factorials[int(x)] for x in str(n)]):
        curious_numbers.append(n)

print(sum(curious_numbers))
