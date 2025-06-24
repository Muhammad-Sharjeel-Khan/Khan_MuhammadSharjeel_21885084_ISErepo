# Generation finder module  
# This finds what generation someone belongs to based on birth year

def find_generation(year):
    # Check which generation based on year ranges
    if 1901 <= year <= 1945:
        return "Silent Generation"
    elif 1946 <= year <= 1964:
        return "Baby Boomers"
    elif 1965 <= year <= 1979:
        return "Generation X"
    elif 1980 <= year <= 1994:
        return "Millennials"
    elif 1995 <= year <= 2009:
        return "Generation Z"
    elif 2010 <= year <= 2024:
        return "Generation Alpha"
    else:
        return "Unknown"