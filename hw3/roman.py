"""_Isabelle Li - CS5001 HW3 - 16DEC2023
Problem 2: Roman Numerals_
"""


def AllCharsOK(R):
    """_checks if characters in input str are valid
    roman numeral chars_

    Args:
        R (_str_): _user input_

    Returns:
        _bool_: _t/f whether condition succeeds_
    """
    # defines list of valid roman characters
    good_ch = ["m", "d", "c", "l", "x", "v", "i"]

    # cycles through every ch in input string, if not, return False
    for ch in R:
        if ch not in good_ch:
            return False

    # if success, return True
    return True


def AllFreqsOK(R):
    """_checks if frequency of roman chs is valid_

    Args:
        R (_str_): _user input_

    Returns:
        _bool_: _t/f whether condition holds_
    """
    return (R.count("m") <= 3
            and R.count("c") <= 3
            and R.count("x") <= 3
            and R.count("i") <= 3
            and R.count("d") <= 1
            and R.count("l") <= 1
            and R.count("v") <= 1)


def SingleOK(c, s, R):
    """_returns True if c is not in R
    OR if c is in R and not preceded by an character in S
    otherwise returns False_

    Args:
        c (_str_): _character you compare against_
        s (_str_): _c must come befofre all characters in s_
        R (_str_): _user input_

    Returns:
        _bool_: _whether conditions were fulfilled_
    """
    # checks if target character comp against in R string
    if c.lower() not in R:
        return True

    # cycle throughs all characters in s
    for ch in s:
        edited_ch = ch.lower()
        if edited_ch not in R:
            pass

        if edited_ch in R:
            # gets index of first appearance of ch
            character_index = R.find(edited_ch)

            # rfind to get last index of target character
            compare_index = R.rfind(c.lower())

            # comparison
            return character_index > compare_index
    return True


def AllSinglesOK(R):
    """Returns True if and only if R is a single-legal string.

    PreC: R is a non-null string.
    """
    M_ok = SingleOK('M', 'DLXVI', R)
    D_ok = SingleOK('D', 'LXVI', R)
    C_ok = SingleOK('C', 'LVI', R)
    L_ok = SingleOK('L', 'VI', R)
    X_ok = SingleOK('X', 'V', R)
    return M_ok and D_ok and C_ok and L_ok and X_ok


def DoubleOK(s, R):
    """_rteurns True if s is not in R or if s occurs once in R
    and the first occurrence of s[0] is the first occurrence of s
    Otherwise False is returned_

    Args:
        s (_str_): _double character str_
        R (_str_): _input str_

    Returns:
        _bool_: _whether condition is met_
    """
    # checks if s is in R, if yes, return True
    if s.lower() not in R:
        return True

    # index check
    return R.find(s.lower()) == R.find(s[0].lower())


def AllDoublesOK(R):
    """Returns True if and only if R is a double-legal string.

    PreC: R is a non-null string.
    """
    C_ok = DoubleOK('CD', R) and DoubleOK('CM', R)
    X_ok = DoubleOK('XL', R) and DoubleOK('XC', R)
    I_ok = DoubleOK('IV', R) and DoubleOK('IX', R)
    return C_ok and X_ok and I_ok


def Value(R):
    """_determines numerical value of roman number_

    Args:
        R (_str_): _input string_

    Returns:
        _int_: _numerical value_
    """
    # define ongoing sum
    sum = 0

    # define dictionaries
    roman_add_dict = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100,
                      "d": 500, "m": 1000}

    roman_subtract_dict = {"cm": -200, "cd": -200, "xc": -20, "xl": -20,
                           "ix": -2, "iv": -2}

    # cycle through every chaarcter, add initial values
    for ch in R:
        sum += roman_add_dict[ch]

    # cycle through all the trouble strings
    for concern in roman_subtract_dict.keys():
        if concern in R:
            # subtract value from ongoing sum
            sum += roman_subtract_dict[concern]

    # return numerical value
    return sum


if __name__ == '__main__':
    R = input('Enter a Roman Numeral String'
              '(do not surround with quotes): ').lower()
    print('AllCharsOK(R)   is ', AllCharsOK(R))
    print('AllFreqsOK(R)   is ', AllFreqsOK(R))
    print('AllSinglesOK(R) is ', AllSinglesOK(R))
    print('AllDoublesOK(R) is ', AllDoublesOK(R))
    OK = (AllCharsOK(R) and AllFreqsOK(R) and AllSinglesOK(R)) and\
        AllDoublesOK(R)
    if OK:
        print('Value = %1d' % Value(R))
    else:
        print('Not a valid Roman numeral string.')
