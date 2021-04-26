words = {
    "0": "",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
    "2x": "twenty",
    "3x": "thirty",
    "4x": "forty",
    "5x": "fifty",
    "6x": "sixty",
    "7x": "seventy",
    "8x": "eighty",
    "9x": "ninety",
    "xxx": "hundred",
    "xxxx": "thousand",
    " ": "and"
}

word_count = 0

for i in range(1001, 2001):
    d = ('1' if i > 1999 else '0') + str(i)[1:]
    thousands = words[d[0]] + (words['xxxx'] if int(d[0]) > 0 else '')
    hundreds = words[d[1]] + (words['xxx'] if int(d[1]) > 0 else '')
    tens = words[d[2] + 'x'] if int(d[2:4]) > 19 else (
        words[d[2:4]] if int(d[2:4]) > 9 else '')
    ones = words[d[3]] if int(d[2:4]) < 10 or int(d[2:4]) > 19 else ''
    ands = words[" "] if int(d) > 99 and int(d) % 100 != 0 else ''

    number = (thousands + hundreds + ands + tens + ones)
    word_count += len(number)

print(word_count)
