exp = 5
powers = [pow(i, exp) for i in range(10)]


def sum_of_powers(n):
    return sum(powers[int(i)] for i in str(n))


print(sum(n for n in range(2, 999999) if n == sum_of_powers(n)))
