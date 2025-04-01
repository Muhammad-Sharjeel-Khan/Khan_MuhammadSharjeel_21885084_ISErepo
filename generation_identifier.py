def get_generation(year):
    if 1925 <= year <= 1945:
        return "Silent Generation"
    elif 1946 <= year <= 1964:
        return "Baby Boomers"
    elif 1965 <= year <= 1980:
        return "Gen X"
    elif 1981 <= year <= 1996:
        return "Millennials"
    elif 1997 <= year <= 2012:
        return "Gen Z"
    elif 2013 <= year <= 2025:
        return "Gen Alpha"
    else:
        return "Unknown"
