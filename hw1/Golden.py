"""Isabelle Li - CS5001 HW1 - 15DEC2023
Problem 1: Golden Ratio
    """
import math


class InvalidInt(Exception):
    pass


def fib_num(num):
    """_function to determine fib num at any num_

    Args:
        num (_int_): _place of fib sequence_

    Returns:
        _int_: _fib num_
    """
    fn = round((1/math.sqrt(5)) * ((((1+math.sqrt(5))/2)**num)
                                   - ((1-math.sqrt(5))/2)**num))
    return fn


def ratio(num, num1):
    """_function to determine the ratio fn+1/fn_

    Args:
        num (_int_): _fn_
        num1 (_int_): _fn1_

    Returns:
        _float_: _ratio_
    """
    rn = num1/num
    return rn


def lucas(num, num1):
    """_determine lucas num given 2 consecutive fib nums_

    Args:
        num (_int_): _fn_
        num1 (_int_): _fn1 (subsequent fib num)_

    Returns:
        _int_: _lucas num_
    """
    ln = (2 * num1) - num
    return ln


try:
    # check for int by int conversion of input
    n = int(input("Enter an integer for nth value"
                  " of the Fibonacci sequence: "))

    # check for pos/neg num + raise
    if (n <= 0) or (n > 35):
        raise InvalidInt()

    # define n+1
    n1 = n + 1

    # fn, fn1, fn2 determination
    fn = fib_num(n)
    fn1 = fib_num(n1)
    fn2 = fib_num(n + 2)        # for rn1 calc

    # ratio determination: rn, rn1
    rn = ratio(fn, fn1)
    rn1 = ratio(fn1, fn2)

    # lucas num (ln, ln1)
    ln = lucas(fn, fn1)
    ln1 = lucas(fn1, fn2)

    # print out statements
    print(f"{n}\t {fn}\t {rn}\t {ln}")
    print(f"{n1}\t {fn1}\t {rn1}\t {ln1}")

# not an int exception
except ValueError:
    print("Input must be an integer.")

# positive number exception
except InvalidInt:
    print("Input must be pos. and less than 35.")

# tells user that input check is done, even for invalid entry
finally:
    print("Input check is done.")
