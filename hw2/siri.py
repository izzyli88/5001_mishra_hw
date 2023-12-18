"""_Isabelle Li - CS5001 HW2 - 15DEC2023
Problem 1: Siri Sez_
"""
"""converts a route string into a sequence of driving instructions"""


def siri_sez(x):
    """_given an intersection string of length 2,
    return the directions_

    Args:
        x (_str_): _intersection string_

    Returns:
        _str_: _turn directions_
    """
    start = x[0]
    end = x[1]
    turn_tup = (start, end)

    if start == end:
        dir = "Continue Straight"

    # u-turn
    elif turn_tup in [("n", "s"), ("s", "n"), ("w", "e"), ("e", "w")]:
        dir = "Make a U-Turn"

    # left
    elif turn_tup in [("n", "w"), ("s", "e"), ("w", "s"), ("e", "n")]:
        dir = "Turn Left"

    # right
    else:
        dir = "Turn Right"

    return dir


def trip_advisor(route):
    """_given a route of length 6, give directions_

    Args:
        route (_str_): _route string_
    """
    coords = {"n": "North", "s": "South", "e": "East", "w": "West"}

    start = route[0]
    start_dir = coords[start]
    print(f"Start Driving {start_dir}")

    # for loop to section route into 5 sublists and perform siri_sez on each
    for i in range(5):
        print(siri_sez(route[i:i+2]))


# main program (application script)
if __name__ == "__main__":
    dir = input("Enter an intersection string: ").lower()
    trip_advisor(dir)
