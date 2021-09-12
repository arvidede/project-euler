# Once again, ape strong


def pandigital(num, concatenated_product: str = "", multiplier=1, MAX_LEN=9):
    concatenated_product += str(num * multiplier)
    product_length = len(concatenated_product)

    if (
        "0" in concatenated_product
        or product_length > MAX_LEN
        or len(set(concatenated_product)) < product_length
        or multiplier > 9
    ):
        return None

    if multiplier > 1 and product_length == MAX_LEN:
        return int(concatenated_product)

    return pandigital(num, concatenated_product, multiplier + 1)


MAX = 0
i = 9


while i < 99999:
    if str(i).startswith("9"):
        n = pandigital(i)
        if n and n > MAX:
            MAX = n
    i += 1

print(MAX)
