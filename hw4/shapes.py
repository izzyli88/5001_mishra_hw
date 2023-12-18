"""Isabelle Li - CS5001 HW4 - 16DEC2023
Shapes
"""


class InvalidNum(Exception):
    pass


# function definitions


def left_triangle(n):
    """_makes a left triangle w/ size n_

    Args:
        n (_int_): _max side length of triangle_
    """
    # forces i to iterate through [1, n]
    for i in range(1, n + 1):
        print()


def arrowhead(n):
    """_makes an arrowhead w/ size n_

    Args:
        n (_int_): _max length of arrowhead_
    """
    # makes first half [1, n]
    for i in range(1, n+1):
        print(i * "*")

    # makes 2nd half [n-1, 1]
    for j in range(n-1, 0, -1):
        print(j * "*")


def right_triangle(n):
    """_makes a right triangle w/ size n_

    Args:
        n (_int_): _max side length of triangle_
    """
    # [n, 1], i decrements by one each time
    for i in range(n, 0, -1):
        print(i * "*")


def boomerang(n):
    """_makes a boomerang w/ size n_

    Args:
        n (_int_): _max size of boomerang_
    """
    # draw first half
    for i in range(n-1, -1, -1):
        print(2 * i * " ", (n-i) * "*")

    # draws second half
    for j in range(1, n):
        print(2 * j * " ", (n-j) * "*")


def ask_user():
    """_user prompt_

    Returns:
        _int_: __user input
    """
    print("What shape shall we draw?")
    print("0 - nothing")
    print("1 - left triangle")
    print("2 - arrowhead")
    print("3 - right triangle")
    print('4 - boomerang')
    return int(input("Enter choice: "))


if __name__ == "__main__":

    cont_game = True
    while cont_game:
        try:
            shape_choice = ask_user()
            if shape_choice == 0:
                print("Good game.")
                cont_game = False
            elif not (0 <= shape_choice <= 4):
                raise InvalidNum
            else:
                valid_shape = True
                while valid_shape:
                    try:
                        size = int(input("Enter size (int, >= 3): "))
                        if not size >= 3:
                            raise InvalidNum
                        else:
                            valid_shape = False
                    except (ValueError, InvalidNum):
                        print("Size should be an int >= 3. ")

            if shape_choice in [1, 2, 3, 4]:
                if shape_choice == 1:
                    left_triangle(size)
                elif shape_choice == 2:
                    arrowhead(size)
                elif shape_choice == 3:
                    right_triangle(size)
                else:
                    boomerang(size)
        except (ValueError, InvalidNum):
            print("Answer must be an int [0-4]")
