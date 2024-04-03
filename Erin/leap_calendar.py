"""
File name: leap_calendar_challenge.py
Author: Erin Cho
Created: 1/04/2024
Description:
This challenge requires you to write an algorithm in any programming language that
will check whether a specified year is a leap year or not and then give the answer to the
user. A leap year is a year on the Gregorian calendar that has 366 days (a normal year
has 365 days).
On the Gregorian calendar, a year is a leap year if it meets the following conditions:
• The year can be evenly divided by 4-
• The year cannot be evenly divided by 100, unless the year can also be evenly divided
by 400
As examples, the years 2000, 2012, 2016, and 2400 are leap years. But the years 1800,
1900, 2100, and 2200 are NOT leap years
Rules:
1. The algorithm must be able to accurately check if a year is a leap year or not. It
must give an answer to the user eg. "2016 is a leap year".
2. Start by specifying a test year in a variable eg. $year= 2016;
Then try adding input so that the user can check different years ( eg. textbox input).
3. For this challenge you cannot use any other existing functions ( eg. date functions) in
the programming language to check if a given year is a leap year.
4. Add error checking for if the input is not a valid year (eg. contains letters or spaces).
5. Test your algorithm using a range of test data (known leap years and known normal
years).
6. Simplify your code and make it as efficient as possible.
"""
print(f"This program checks if a year entered is a leap year or not")

# Assign 2016 into year variable for a test
# year = 2016

# Create a function to check if a year entered is valid
def check_year_input(year):
    if year.isdigit():
        return True
    else:
        return False

# Create a function to check if a year entered is a leap year or not
def check_leap_year(year):
    if (year % 4 ==0) and (year % 100 != 0):
        return True
    elif (year % 400 == 0):
        return True
    else:
        return False

# Get an input for a year then convert string into integer value
year = input("Please input a year: ")

# Use a function to check if a year entered is valid
if check_year_input(year):
    # Convert string to integer
    year = int(year)

    # Use a function 'check_leap_year' to check if a year entered is a leap year or not
    if check_leap_year(year):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
else:
    print(f"Please enter a valid year.")