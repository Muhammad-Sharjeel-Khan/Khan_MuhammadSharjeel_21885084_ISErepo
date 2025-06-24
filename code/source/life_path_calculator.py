# Life path number calculation module
# This calculates numerology life path number

def calculate_life_path_number(day, month, year):
    # Master numbers that we don't reduce
    master_numbers = [11, 22, 33]
    
    # Add up all digits in a number
    def add_digits(number):
        total = 0
        for digit in str(number):
            total = total + int(digit)
        return total
    
    # Reduce number to single digit unless master number
    def reduce_number(number):
        if number <= 9:
            return number
        if number in master_numbers:
            return number
        # Keep reducing until single digit
        new_number = add_digits(number)
        return reduce_number(new_number)
    
    # Reduce each part separately but keep master numbers
    if day in master_numbers:
        day_sum = day
    else:
        day_sum = reduce_number(day)
    
    if month in master_numbers:
        month_sum = month
    else:
        month_sum = reduce_number(month)
    
    if year in master_numbers:
        year_sum = year
    else:
        year_sum = reduce_number(year)
    
    # Add them up
    total_sum = day_sum + month_sum + year_sum
    
    # Check if total is master number
    if total_sum in master_numbers:
        return total_sum
    
    # Reduce to single digit if needed
    if total_sum > 9:
        final_number = reduce_number(total_sum)
        return final_number
    
    return total_sum