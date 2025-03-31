from datetime import datetime

def parse_date(date_str):
    try:
        try:
            dt = datetime.strptime(date_str, "%d-%m-%Y")
        except ValueError:
            dt = datetime.strptime(date_str, "%B %d, %Y")
        if dt.year < 1925 or dt.year > 2025:
            return None
        return dt.day, dt.month, dt.year
    except Exception:
        return None
