from life_path_calculator import calculate_life_path_number

def compare_life_path_numbers(dob1, dob2):
    lp1 = calculate_life_path_number(*dob1)
    lp2 = calculate_life_path_number(*dob2)
    return lp1 == lp2
