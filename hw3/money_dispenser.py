"""_Isabelle Li - CS5001 HW3 - 15DEC2023
Problem 1: Money Dispenser_
"""

# given 20s, 10s, 5s, 1s, 0.25s, 0.10s, 0.05s, 0.01s, find lowest combo

# defining constant
CURRENT_SUM = 0

# defines a dictionary for dollar amount: name
# use ints, mult. all values by 100
amnts = {2000: "twenties", 1000: "tens", 500: "fives", 100: "ones",
         25: "quarters", 10: "dimes", 5: "nickels",
         1: "pennies"}

# ask for user input, convert dollar amount to cents
original_money = float(input("Give money amount: ")) * 100

# new var. money to keep track of remaining money, orig. for comparison at end
money = original_money

# cycles through all keys:values in dictionary
for k, v in amnts.items():
    # only look at key if amount is more than bill value
    if money >= k:
        # determine number of bills needed
        num_bills = money // k

        # determine remainder, update money
        remainder = money % k
        money = remainder

        # update currrent sum
        CURRENT_SUM += num_bills * k

        # only prints bills if bills are used
        if num_bills > 0:
            print(f"Number of {v}: {num_bills}")

# update sum to correct sig figs
final_sum = CURRENT_SUM

# comparison to check if program is successful
if final_sum == original_money:
    print("Success")
else:
    print("Fail")


# original code #
# twenties = int(money // 20)
# rem_20 = money % 20

# tens = int(rem_20 // 10)
# rem_10 = rem_20 % 10

# fives = int(rem_10 // 5)
# rem_5 = round((rem_10 % 5), 2)

# ones = int(rem_5 // 1)
# rem_1 = round((rem_5 % 1), 2)

# quarters = int(rem_1 // 0.25)
# rem_q = round((rem_1 % 0.25), 2)

# dimes = int(rem_q // 0.10)
# rem_d = round((rem_q % 0.10), 2)

# nickels = int(rem_d // 0.05)
# rem_n = round((rem_d % 0.05), 2)

# pennies = int(rem_n / 0.01)
