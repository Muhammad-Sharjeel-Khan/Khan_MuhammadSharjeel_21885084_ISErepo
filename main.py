from date_parser import parse_date
from life_path_calculator import calculate_life_path_number
from lucky_colour import get_lucky_colour
from generation_identifier import get_generation
from master_number import is_master_number

def main():
    print("Numerology Analysis Tool")
    bday_input = input("Enter your birthday (dd-mm-yyyy or Month dd, yyyy): ")
    parsed = parse_date(bday_input)
    if not parsed:
        print("Invalid date format or out-of-range year (1925–2025).")
        return

    day, month, year = parsed
    life_path = calculate_life_path_number(day, month, year)
    colour = get_lucky_colour(life_path)
    generation = get_generation(year)
    master = is_master_number(life_path)

    print(f"Life Path Number: {life_path}")
    print(f"Master Number? {'Yes' if master else 'No'}")
    print(f"Lucky Colour: {colour}")
    print(f"Generation: {generation}")

if __name__ == "__main__":
    main()
