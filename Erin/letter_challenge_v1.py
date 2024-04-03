"""
File name: letter_challenge.py
Author: Erin Cho
Created: 1/04/2024
Description:
Letter counter challenge
For this challenge you need to write a program that will read a string
Count how many times a letter occurs in that string (you can specify the letter you want to look for)
Display how many times a letter occurs twice in a row
Must be able to work with both low and upper case letters (Case sensitive)
"""

# Function to get two inputs - String and letter
# 1. Check how many times a letter occurs in the string
# 2. Check how many times a letter occurs twice in a row
# Return output 1 and 2
def letter_occurrence(string, letter):

    pre_element = ''
    twice_in_a_row_count = 0
    count = 0

    # For loop to check if a letter matches in that string
    for e in string:
        if e == letter: # If matched
            count += 1 # Count how many times the letter occurs in that string
            if e == pre_element: # If matched with previous letter
                twice_in_a_row_count += 1 # Count how many times the letter occurs twice in a row
        pre_element = e # Assign the letter into pre_element

    # Return two output
    return count, twice_in_a_row_count

# Main function to print output
def main():

    # Input string
    target_string = input("Please input a string: ")
    target_letter = input("Please input a letter to count: ")

    count_occurrence, count_twice_in_a_row = letter_occurrence(target_string, target_letter)

    # Print outcomes
    print(f"The target letter '{target_letter}' occurs {count_occurrence} times in the string.")
    print(f"The target letter '{target_letter}' occurs twice in a row {count_twice_in_a_row} times in the string.")

# Execute main function
if __name__ == "__main__":
    main()