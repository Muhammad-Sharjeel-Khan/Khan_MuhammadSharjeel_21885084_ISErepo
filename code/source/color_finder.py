# Lucky color finder module
# This finds the lucky color for a life path number

def find_lucky_color(life_path_number):
    # Color mapping for each life path number
    colors = {
        1: "Red",
        2: "Orange", 
        3: "Yellow",
        4: "Green",
        5: "Sky Blue",
        6: "Indigo",
        7: "Violet",
        8: "Magenta",
        9: "Gold",
        11: "Silver",
        22: "White",
        33: "Crimson"
    }
    
    # Check if number is valid
    if life_path_number not in colors:
        raise ValueError(f"Invalid Life Path Number: {life_path_number}")
    
    return colors[life_path_number]