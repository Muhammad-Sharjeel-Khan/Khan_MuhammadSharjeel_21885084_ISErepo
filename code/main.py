# Main program for numerology calculator
# This brings together all the modules

from source.birthday_checker import check_birthday
from source.life_path_calculator import calculate_life_path_number
from source.color_finder import find_lucky_color
from source.generation_finder import find_generation

def main():
    # Get first birthday from user
    birthday1 = input("Enter your birthday (e.g., 09 July 2005 or 13 Nov 1987): ")
    
    # Check if birthday is valid
    day1, month1, year1 = check_birthday(birthday=birthday1)
    
    # Calculate life path number
    lpn1 = calculate_life_path_number(day=day1, month=month1, year=year1)
    
    # Find lucky color
    color1 = find_lucky_color(lpn1)
    
    # Find generation
    gen1 = find_generation(year=year1)
    
    # Show results for first birthday
    print(f"\nYour birthday : {birthday1}")
    print(f"Your life path number : {lpn1}")
    print(f"Your lucky color : {color1}")
    print(f"Your generation : {gen1}")
    
    # Ask if user wants to compare with another birthday
    compare_choice = input("\nDo you want to compare with another birthday? (yes/y): ").lower()
    
    if compare_choice == "yes" or compare_choice == "y":
        # Get second birthday
        birthday2 = input("Enter second birthday (e.g., 09 July 2005 or 13 Nov 1987): ")
        
        # Check second birthday
        day2, month2, year2 = check_birthday(birthday=birthday2)
        
        # Calculate for second birthday
        lpn2 = calculate_life_path_number(day=day2, month=month2, year=year2)
        color2 = find_lucky_color(lpn2)
        gen2 = find_generation(year=year2)
        
        # Show second birthday results
        print(f"\nSecond birthday : {birthday2}")
        print(f"Life path number : {lpn2}")
        print(f"Lucky color : {color2}")
        print(f"Generation : {gen2}")
        
        # Create comparison table
        print("\n" + "=" * 50)
        print(f"{'COMPARISON':^50}")
        print("=" * 50)
        
        # Show comparison
        p1_label = "Person 1"
        p1_birthday = f"Birthday: {birthday1}"
        p1_lpn = f"Life Path Number: {lpn1}"
        p1_lucky = f"Lucky Color: {color1}"
        p1_gen = f"Generation: {gen1}"
        
        p2_label = "Person 2"
        p2_birthday = f"Birthday: {birthday2}"
        p2_lpn = f"Life Path Number: {lpn2}"
        p2_lucky = f"Lucky Color: {color2}"
        p2_gen = f"Generation: {gen2}"
        
        col_width = 24
        
        print(f"{p1_label:^{col_width}} | {p2_label:^{col_width}}")
        print("-" * 50)
        print(f"{p1_birthday:<{col_width}} | {p2_birthday:<{col_width}}")
        print(f"{p1_lpn:<{col_width}} | {p2_lpn:<{col_width}}")
        print(f"{p1_lucky:<{col_width}} | {p2_lucky:<{col_width}}")
        print(f"{p1_gen:<{col_width}} | {p2_gen:<{col_width}}")
        print("-" * 50)
        
        # Compare life path numbers
        if lpn1 == lpn2:
            comparison_result = f"Same Life Path Number: {lpn1}"
        else:
            comparison_result = f"Different Life Path Numbers: {lpn1} vs {lpn2}"
        
        print(f"{comparison_result:^50}")
        print("=" * 50)

if __name__ == "__main__":
    main()