import string    # gives us ascii_lowercase
from GetData import fileToStringList
import os


def OffByOne(s1, s2):
    """_determines if strings are off by one character_

    Args:
        s1 (_str_): _string 1_
        s2 (_str_): _string 2_

    Returns:
        _bool_: _whetehr conditions were fulfilled_
    """
    if len(s1) == len(s2):
        # set difference counter
        diff = 0

        # cycles thru all indices in s1
        for i in range(len(s1)):
            # if there's a diff, diff increments by 1
            if s1[i] != s2[i]:
                diff += 1
        return True if diff == 1 else False

    return False


def OffBySwap(s1, s2):
    """_determines if characters are off by one swap_

    Args:
        s1 (_str_): _first str_
        s2 (_str_): _second str_

    Returns:
        _bool_: _whether conditions fulfilled_
    """
    s1_orig = s1
    # proceeeds if strs are same length and not the same
    if (len(s1) == len(s2)) and s1 != s2:

        # iterates through all characters
        for i in range(len(s1) - 1):
            # strings immutable, turn into list to swap
            s1_list = list(s1_orig)

            # swap i, i+1 indices
            temp = s1_list[i]
            s1_list[i] = s1_list[i+1]
            s1_list[i+1] = temp

            # revert back into string and compare
            s1 = "".join(s1_list)
            if s1 == s2:
                return True
    return False


def ListOfDeleteOnes(s):
    """_returns list of strs that can be obtaiend from s
    by deleting one character_

    Args:
        s (_str_): _string to be converted_

    Returns:
        _list_: _possible strings_
    """
    orig_s = s
    # initiate empty list of words
    new_words = []

    # cycle through all letters
    for i in range(len(s)):

        # make a list since strings are immutable, delete index ch.
        s_list = list(orig_s)
        del s_list[i]

        # append new word to list
        new_words.append("".join(s_list))
    return new_words


def OffByExtra(s1, s2):
    """_returns True if removing one ch from s1 or s2 yields the
    other_

    Args:
        s1 (_str_): _first string_
        s2 (_str_): _second string_

    Returns:
        _bool_: _whether condition was fulfilled_
    """
    # combine two bools, if either works return True, else False
    if (s2 in ListOfDeleteOnes(s1)) or (s1 in ListOfDeleteOnes(s2)):
        return True
    return False


def ListOfNeighbors(s, L):
    """_list of neighbors of str:
    off by one or off by swap, or off by extra_

    Args:
        s (_str_): _str you compare against_
        L (_list_): _list of all english words_

    Returns:
        _list_: _neighbors of string_
    """
    # initialize empty list of neighbors
    neighbor_list = []

    # iterate through length of words list
    for i in range(len(L)):
        # set test word
        trial_ch = L[i]

        # test off by one, swap, and extra
        a = OffByOne(s, trial_ch)
        b = OffBySwap(s, trial_ch)
        c = OffByExtra(s, trial_ch)

        # if at least one is True, append to list
        if (a or b or c) and trial_ch != s:
            neighbor_list.append(trial_ch)
    # return list
    return neighbor_list


def ListOfNeighbors2(s, L):
    """_returns list of neighbors of neighbors of s,
    no repeat characters_

    Args:
        s (_str_): _string you compare to_
        L (_list_): _list of neighbors^2_

    Returns:
        _type_: _description_
    """
    # initialize empty list of neighbors^2
    n_neighbors = []

    # obtain list of neighbors of s from word list
    s_neighbors = ListOfNeighbors(s, L)

    # iterate through all neighbors
    for word in s_neighbors:
        # obtain neighbor list for each neighbor
        neighbors2 = ListOfNeighbors(word, L)

        # concat to neighbors^2 list
        n_neighbors += neighbors2

    # set allows only unique words (no repeats), put into list
    sorted_neighbors2 = list(set(n_neighbors))

    # return final neighbors^2 list
    return sorted_neighbors2


def ScrabbleScore(s):
    """ Returns the Scrabble value of the uppercase version of s.

    PreC: s is a nonempty string comprised of letters
    (of any, or mixed, case).
    """
    # retrieve string of capital letters
    Letters = string.ascii_uppercase

    # define supply (counts) and value lists of all letters
    Supply = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1,
              6, 4, 6, 4, 2, 2, 1, 2, 1]
    Value = [1, 3, 3, 2, 1, 4, 2, 4, 1,
             8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1,
             1, 4, 4, 8, 4, 10]

    # initialize word sum
    word_sum = 0

    # iterate through every character in s
    for ch in s:

        # obtain number of times ch appears in s
        letter_count = s.count(ch)

        # obtain index, supply, value
        letter_index = Letters.index(ch.upper())
        letter_supply = Supply[letter_index]
        letter_value = Value[letter_index]

        # preliminary check if count > supply, if yes, then sum = 0
        if letter_count > letter_supply:
            word_sum = 0

            # break out of for loop
            break

        # else incremement sum by value of letter
        else:
            word_sum += letter_value

    # returns final sum
    return word_sum


def retrieve_file():
    """_reads and makes a list of words from
    EnglishWords.txt_

    Returns:
        _list_: _list of words_
    """
    # obtain file path using os
    abs_path = os.path.dirname(__file__)
    relative_path = "EnglishWords.txt"
    file = os.path.join(abs_path, relative_path)

    # makes word list
    word_list = fileToStringList(file)
    return word_list


def nice_print(entry_list):
    """_finds scrabble score for all words in list
    and prints nicely_

    Args:
        entry_list (_list_): _list of words_
    """
    # iterates through all words
    for word in entry_list:
        # finds scrabble value
        value = ScrabbleScore(word)
        print(f"{word}: {value}")


def main():
    word_list = retrieve_file()
    while True:
        s = input("Enter a nonempty string of lowercase letters: ")
        if s.islower() is True:
            break
        else:
            print("Entry must be all lowercase letters.")

    # prints all the neighbors of s and their Scrabble scores
    print("\nNeighbors:\n")
    neighbors = ListOfNeighbors(s, word_list)
    nice_print(neighbors)

    # prints all the neighbors^2 of s and their Scrabble scores
    print("\nNeighbors of the Neighbors:\n")
    neighbors2 = ListOfNeighbors2(s, word_list)
    nice_print(neighbors2)


main()
