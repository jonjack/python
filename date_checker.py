#!/usr/bin/env python3

legal_month_days = {  1: 31, 2: 28, 3: 31, 4: 30, 
                      5: 31, 6: 30, 7: 31, 8: 31, 
                      9: 30, 10: 31, 11: 30, 12: 31 }

leap_feb_days = 29

def collect_date():
	return str(input("Enter your date - it must match this format -> dd/mm/yy: "))

def date_length_is_valid(date):
	return len(date) == 8

def date_contains_valid_slashes(date):
	if date[2] == "/" and date[5] == "/":
		return True
	return False

def is_int(digit):
    try:
        num = int(digit)
    except ValueError:
        return False
    return True

def date_contains_ints(date):
	if is_int(date[0]) and is_int(date[1]) and is_int(date[3]) and is_int(date[4]) and is_int(date[6]) and is_int(date[7]):
		return True
	return False

def is_month_february(date):
	if is_int(date[3]) and is_int(date[4]):
		if int(date[3]) == 0 and int(date[4]) == 2:
			return True
	return False

def is_leap_year(date):
  year = date[6] + date[7]
  if is_int(year):
    year = int(year)
    if year % 4 == 0:
      return True
  return False

def is_month_valid(date):
  month = date[3] + date[4]
  if is_int(month):
    month = int(month)
    if month > 0 and month < 13:
      return True
  return False

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


def main():
  
  date = ""
  validate = True

  while validate:

    date = collect_date()

    if date_length_is_valid(date) == False:
      #print("debugging: invalid length")
      continue

    if date_contains_valid_slashes(date) == False:
      #print("debugging: invalid slashes")
      continue

    if date_contains_ints(date) == False:
      #print("debugging: invalid ints")
      continue

    if is_month_valid(date) == False:
      #print("debugging: invalid month")
      continue

    if are_days_valid_for_month(date) == False:
      #print("debugging: days are not valid for month")
      continue

    print("All validation checks passed for date: ", date)

    break


main()