def get_lucky_colour(life_path):
    colour_map = {
        1: "Red",
        2: "Orange",
        3: "Yellow",
        4: "Green",
        5: "Blue",
        6: "Indigo",
        7: "Violet",
        8: "Pink",
        9: "Gold"
    }
    return colour_map.get(life_path, "None")
