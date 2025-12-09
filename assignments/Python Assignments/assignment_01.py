# --------------------------------------------
# Assignment 01 – Python Fundamentals
# Date: 2025-11-15
# Student: Shubham Patial
# --------------------------------------------

# Q1
# Write a program that asks the user for their name and age.
# Then print a sentence like:
# "Hello Shradha, you are 21 years old!"

name = input("Enter your name = ")
age = int(input("Enter your age = "))
print(f"Hello {name}, you are {age} years old!")

# Q2
# Take two numbers as input from the user and print their:
# - sum
# - difference
# - product
# - quotient

num_1 = int(input("Enter your first number = "))
num_2 = int(input("Enter your second number = "))
print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 * num_2)
print(num_1 / num_2)

# Q3
# Ask the user to enter two integers and one float.
# Convert them all to floats and print their average.

n_1 = int(input("Enter your first integer number = "))
n_2 = int(input("Enter your second integer number = "))
fn  = float(input("Enter any float number = "))
print((float(n_1) + float(n_2) + fn)/3)

# Q4
# The user enters a string containing a number (e.g., "45").
# Convert it to:
# - an integer
# - a float
# - a string again
# Print all three values with their types.

str_num = input("Enter any number = ")
print(str_num, type(int(str_num)))
print(str_num, type(float(str_num)))
print(str_num, type(str_num))

# Q5
# Evaluate the following expression and print the result:
# x = 10 + 3 * 2 ** 2
# Also explain (in comments) why the output is what it is based on operator precedence.

x = 10 + 3 * 2 ** 2
print(x)
 
""" the Python "order of operations" (or operator precedence),
just like in regular math (PEMDAS/BODMAS)! 
Operator precedence in Python:
- Exponent (**) first → 2**2 = 4
- Multiplication (*) next → 3*4 = 12
- Addition (+) last → 10 + 12 = 22
"""

# Q6
# Write a program to swap values of two numbers entered by the user.

value_1 = input("Enter the first value = ")
value_2 = input("Enter the second value = ")
print(f"Before swap: value_1 = {value_1}, value_2 = {value_2}")
value_3 = value_1
value_1 = value_2
value_2 = value_3
print(f"After swap: value_1 = {value_1}, value_2 = {value_2}")

# Q7
# Ask the user for a temperature in Celsius (string input).
# Convert it to float, then calculate and print temperature in Fahrenheit.
# Formula:
# Fahrenheit

temp = input("Enter the temperature in Celsius = ")
fahrenheit_value = (float(temp) * 9/5) + 32

print(f"The value of temp in Fahrenheit is = {fahrenheit_value}")