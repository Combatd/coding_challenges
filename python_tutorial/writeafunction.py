'''
An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
    The year can be evenly divided by 100, it is NOT a leap year, unless:
        The year is also evenly divisible by 400. Then it is a leap year.

This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

Task

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.
'''
'''
Whiteboarding

* #is_leap(year) receives an integer as an argument.
* We first check that the argument year is integer type.
* Initialize a boolean leap as False.
* Then we can check for two sets of conditionals, and if one set is true, we seat leap to true.
    * A leap year happens every 4 years.
    * A leap year is divisible by 100 is only a leap year if it is also divisible by 400.
* We can't have year outside of integer values of year from 1900 to 100000, or we return False.
* At the end of the function, return leap boolean value
'''

def is_leap(year):
    leap = False
    
    
    # Write your logic here
    if isinstance(year, int) and year >= 1900 and year <= 100000:
        if year % 4 == 0 and year % 100 != 0:
            leap = True
        elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
            leap = True

    return leap

year = int(input())