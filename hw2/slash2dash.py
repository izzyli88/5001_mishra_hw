"""_Isabelle Li - CS5001 HW2 - 15DEC2023
Problem 1: Slash-Date to Dash-Date_
"""
"""converts slash date to dash table format"""

"2/29/2015"


def format_date_month(slice):
    if len(slice) == 1:
        format = "0" + slice
    else:
        format = slice

    return format


slash_date = input("Enter a date: ")

index_slash_one = slash_date.find("/")

index_slash_two = slash_date.find("/", index_slash_one + 1)

# format month
month_slice = slash_date[:index_slash_one]
month = format_date_month(month_slice)


# format date
date_slice = slash_date[index_slash_one + 1: index_slash_two]
date = format_date_month(date_slice)

# year conversion
year_slice = slash_date[index_slash_two + 1::]

if 0 <= int(year_slice) < 23:
    year = "20" + year_slice

elif 24 <= int(year_slice) <= 99:
    year = "19" + year_slice

else:
    year = year_slice

# final formatting + output
dash_date = month + "-" + date + "-" + year

print("Converted date is " + dash_date)
