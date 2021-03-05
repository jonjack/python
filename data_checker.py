#!/usr/bin/env python3

def collect_date():
	return str(input("Enter your date - it must match this format -> dd/mm/yy: "))

def date_length_is_valid(date):
	return len(date) == 8

def date_contains_valid_slashes(date):
	dateArray = list(date)
	validity = False
	if dateArray[2] == "/" and dateArray[5] == "/":
		validity = True
	return validity

def is_int(digit):
    try:
        num = int(digit)
    except ValueError:
        return False
    return True

def date_contains_ints(date):
	arr = list(date)
	if is_int(arr[0]) and is_int(arr[1]) and is_int(arr[3]) and is_int(arr[4]) and is_int(arr[6]) and is_int(arr[7]):
	  return True
	return False

def is_february(date):
	dateArray = list(date)
	if month1 == 0 and month2 == 2:
		return True
	return False



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

    break


main()