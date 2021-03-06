#!/usr/bin/env python3


date = "12/02/20"

month1 = date[3]
month2 = date[4]

month = month1 + month2

print("month: ", month)

print("month int: ", int(month))


legal_month_days = {  1: 31, 2: 28, 3: 31, 4: 30, 
                      5: 31, 6: 30, 7: 31, 8: 31, 
                      9: 30, 10: 31, 11: 30, 12: 31 }

leap_feb_days = 29


print("month_days[1]: ", legal_month_days[1])
print("month_days[7]: ", legal_month_days[7])
print("month_days[2]: ", legal_month_days[2])

# -------------------------------------------

date = "30/13/20"

def is_int(digit):
    try:
        num = int(digit)
    except ValueError:
        return False
    return True

def is_month_valid(date):
	month = date[3] + date[4]
	if is_int(month):
		month = int(month)
		if month > 0 and month < 13:
			return True
	return False

def is_leap_year(date):
	year = date[6] + date[7]
	if is_int(year):
		year = int(year)
		if year % 4 == 0:
			return True
	return False

print("is valid month: ", is_month_valid(date))
print("is leap year: ", is_leap_year(date))

def is_month_february(date):
	if is_int(date[3]) and is_int(date[4]):
		if int(date[3]) == 0 and int(date[4]) == 2:
			return True
	return False

print("is feb: ", is_month_february(date))

def are_days_valid_for_month(date):
	days = date[0] + date[1]
	month = date[3] + date[4]
	if is_int(days) and is_int(month):
		days = int(days)
		month = int(month)
		if is_month_february(date) and is_leap_year(date):
			return days > 0 and days < leap_feb_days + 1
		else:
			return days > 0 and days < legal_month_days[month] + 1



print("are days valid: ", are_days_valid_for_month(date))




