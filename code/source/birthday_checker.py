# Birthday validation module
# This checks if birthday is valid and converts it to numbers

def check_birthday(birthday):
    # Split the birthday into parts
    parts = str(birthday).split()
    
    # Must have exactly 3 parts
    if len(parts) != 3:
        raise ValueError("Invalid Input!\nError: Please use format 'DD Month YYYY'!")
    
    day_part = parts[0]
    month_part = parts[1]
    year_part = parts[2]
    
    # Day must be a number
    if not day_part.isdigit():
        raise ValueError("Invalid Input!\nError: Day must be a number!")
    
    # Year must be a number
    if not year_part.isdigit():
        raise ValueError("Invalid Input!\nError: Year must be a number!")
    
    day_number = int(day_part)
    year_number = int(year_part)
    
    # Check year range 1925-2025
    if year_number < 1925 or year_number > 2025:
        raise ValueError("Invalid Input!\nError: Year must be between 1925 and 2025!")
    
    # Check day range 1-31
    if day_number < 1 or day_number > 31:
        raise ValueError("Invalid Input!\nError: Day must be between 1 and 31!")
    
    # Month names dictionary
    month_names = {
        "january": 1, "february": 2, "march": 3, "april": 4,
        "may": 5, "june": 6, "july": 7, "august": 8,
        "september": 9, "october": 10, "november": 11, "december": 12
    }
    
    # Short month names
    short_months = {
        "jan": 1, "feb": 2, "mar": 3, "apr": 4,
        "may": 5, "jun": 6, "jul": 7, "aug": 8,
        "sep": 9, "oct": 10, "nov": 11, "dec": 12
    }
    
    month_lower = month_part.lower()
    month_number = 0
    
    # Check if month is number
    if month_part.isdigit():
        month_number = int(month_part)
        if month_number < 1 or month_number > 12:
            raise ValueError("Invalid Input!\nError: Month number must be 1-12!")
    # Check if full month name
    elif month_lower in month_names:
        month_number = month_names[month_lower]
    # Check if short month name
    elif month_lower in short_months:
        month_number = short_months[month_lower]
    else:
        raise ValueError("Invalid Input!\nError: Invalid month name!")
    
    # Days in each month
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    # Check for leap year
    is_leap_year = False
    if year_number % 4 == 0:
        if year_number % 100 == 0:
            if year_number % 400 == 0:
                is_leap_year = True
        else:
            is_leap_year = True
    
    # February has 29 days in leap year
    if is_leap_year and month_number == 2:
        days_in_month[2] = 29
    
    # Check if day is valid for this month
    max_days = days_in_month[month_number]
    if day_number > max_days:
        raise ValueError("Invalid Input!\nError: This month doesn't have that many days!")
    
    return day_number, month_number, year_number