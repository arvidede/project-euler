def fibonacci_index(max_len):
    f_n_1, f_n, i = 0, 1, 1
    while len(str(f_n)) < max_len:
        f_n_1, f_n, i = f_n, f_n_1 + f_n, i + 1
    return i


print(fibonacci_index(1000))
