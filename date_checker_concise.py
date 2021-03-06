#!/usr/bin/env python3

# Read about how this works at 
#     https://www.programiz.com/python-programming/datetime/strptime

from datetime import datetime


def is_valid_date(date):
    try:
        datetime.strptime(date, "%d/%m/%y")
    except ValueError:
        return False
    return True

# everything below this line is just test data and debug statements
date_1 = "21/02/20"
date_2 = "aaaaaaaa"
date_3 = "32/12/20"
date_4 = "0/12/20"
date_5 = "30/12/8"
date_6 = "44444444"
leap_year_valid_feb = "29/02/20"
leap_year_invalid_feb = "29/02/19"

print("is date_1 valid = ", is_valid_date(date_1))
print("is date_2 valid = ", is_valid_date(date_2))
print("is date_3 valid = ", is_valid_date(date_3))
print("is date_4 valid = ", is_valid_date(date_4))
print("is date_5 valid = ", is_valid_date(date_5))
print("is date_6 valid = ", is_valid_date(date_6))
print("is leap_year_valid_feb valid = ", is_valid_date(leap_year_valid_feb))
print("is leap_year_invalid_feb valid = ", is_valid_date(leap_year_invalid_feb))