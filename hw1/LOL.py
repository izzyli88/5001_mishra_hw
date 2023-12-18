"""Isabelle Li - CS5001 HW1 - 15DEC2023
Problem 2: LOL? FWM!
    """

from datetime import datetime
from random import choice

""" Explores how long it takes you to enter a given random length-3 string."""

# The only variables you need to know about:
# S1 is the random test string
# S2 is the response string
# t1 is the first timestamp string
# t2 is the second timestamp string

alpha = 'abcdefghijklmnopqrstuvwxyz'
x = input('Press the return key when you are ready.')

S1 = choice(alpha) + choice(alpha) + choice(alpha)

prompt1 = 'The test string: '
prompt2 = 'Enter the test string as fast as you can: '

print('\n' + ' '*(len(prompt2) - len(prompt1)) + prompt1 + S1)
# First time stamp...
t1 = str(datetime.utcnow())
S2 = input(prompt2)
# Second time stamp
t2 = str(datetime.utcnow())

# Display the two timestamps...
print('\n' + t1 + '\n' + t2)

# Only add code below this line ##############################


def edit_time(time):
    """_gives input time in seconds_

    Args:
        time (_str_): _formal time str_

    Returns:
        _float_: _time in seconds_
    """
    # determine index of " ", slice string to remove everything up to " "
    index = time.find(" ")
    updated_time = time[index + 1:]

    # split list into 3 parts [hrs, mins, seconds], calc. total_secs
    final_time = updated_time.split(":")

    total_secs = (float(final_time[0]) * 3600 + float(final_time[1]) * 60 +
                  round(float(final_time[2]), 3))

    # return answer
    return total_secs


#  find total seconds for t1, t2
t1_sec = edit_time(t1)
t2_sec = edit_time(t2)

elapsed_time = round((t2_sec - t1_sec), 3)      # gets elapsed time

# check inputs
if S2 == S1:
    print("Correct response.")
elif len(S2) == 3 and S2 != S1:
    print("There is a character mismatch in your response.")

elif len(S2) != 3:
    print("Your response has the wrong number of characters.")

print("Elapsed Time = " + str(elapsed_time) + " seconds")
