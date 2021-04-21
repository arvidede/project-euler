def even_fibbonaci(a, b):
    a_ = a if a % 2 == 0 else 0
    return a_ + even_fibbonaci(b, a+b) if b <= 4e6 else a_


print(even_fibbonaci(1, 2))
