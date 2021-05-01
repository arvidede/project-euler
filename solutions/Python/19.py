from itertools import accumulate


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def year(x): return int(x[:4])


def num_days(year):
    return [
        31, 29 if is_leap_year(year) else 28,
        31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    ]


start_date = '1901-01-01'
end_date = '2000-12-31'

days_per_month_since_1900 = [d for y in range(1900, year(end_date)+1)
                             for d in num_days(y)]

days_since_1900_first_of_month = list(accumulate(days_per_month_since_1900))
days_since_start_first_of_month = days_since_1900_first_of_month[11:]
sundays_since_start = sum([(d + 1) % 7 == 0
                           for d in days_since_start_first_of_month])

print(sundays_since_start)
