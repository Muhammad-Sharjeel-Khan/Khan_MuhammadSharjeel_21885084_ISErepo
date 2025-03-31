def sum_digits(n):
    return sum(int(d) for d in str(n))

def reduce_to_single_or_master(n):
    while n > 9 and n not in (11, 22, 33):
        n = sum_digits(n)
    return n

def calculate_life_path_number(day, month, year):
    total = sum_digits(day) + sum_digits(month) + sum_digits(year)
    return reduce_to_single_or_master(total)
