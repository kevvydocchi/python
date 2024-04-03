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

# Input string and letter
target_string = input("Please input a string: ")
target_letter = input("Please input a letter to count: ")

# Define variables
pre_char = ''
twice_in_a_row_count = 0
count = 0

# For loop to check if a letter matches in that string
for char in target_string:
    if char == target_letter: # If matched
        count += 1 # Count how many times the letter occurs in that string
        if char == pre_char: # If matched with previous letter
            twice_in_a_row_count += 1
        pre_char = char # Assign the letter into pre_element

# Print outcomes
print(f"The target letter '{target_letter}' occurs {count} times in the string.")
print(f"The target letter '{target_letter}' occurs twice in a row {twice_in_a_row_count} times in the string.")
