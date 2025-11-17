# --------------------------------------------
# Assignment 02 – Python Fundamentals
# Date: 2025-11-16
# Student: Shubham Patial
# --------------------------------------------

# Q1
# Write a program that takes salary as input.
# Using conditional statements, calculate the final tax rate based on:
# - If salary < 30,000 → 5%
# - If salary is 30,000–70,000 → 15%
# - If salary > 70,000 → 25%

salary = int(input("Enter your salary = "))
if salary < 30000:
    tax_rate = 0.05
elif salary <= 70000:
    tax_rate = 0.15
else:
    tax_rate = 0.25

tax_amount = salary * tax_rate
print(f"Total Tax Owed: ${tax_amount}")
print(f"Net Salary After Tax: ${salary - tax_amount}")

# Q2
# Write a function that takes two integers a and b
# and prints all even numbers between them (inclusive).

def even_num_checker(start, end):
    start = min(num_1, num_2)
    end = max(num_1, num_2)
    print(f"Even numbers between {start} and {end} are ----")
    for i in range(start, end + 1):
        if i%2 != 0:
            continue
        else:
            print(f"{i}")

num_1 = int(input("Enter the first number = "))
num_2 = int(input("Enter the second number = "))
even_num_checker(num_1, num_2)

# Q3
# Write a function that prints the digits of a number n.
# Example: if n = 312 → print 3, 1, 2
# Hint:
# - Rightmost digit of N is N % 10
# - To remove rightmost digit → N = N // 10

def split_number(num):

    current_num = num
    digits = []

    if current_num == 0:
        print("There is no number to split.....")
        return
     
    while current_num > 0:
        last_digit = current_num % 10
        digits.append(last_digit)
        remaining_digits = current_num // 10
        current_num = remaining_digits

    digits.reverse()
    for n in digits:
        print(f"{n}, ", end="")


number = int(input("Enter any number you want to split = "))
split_number(number)
    

# Q4
# Write a function that returns the count of digits in a number n.

# Q5
# Write a function that returns the sum of digits of a number n.

# Q6
# Write a program to print all numbers from 1 to 100
# that are divisible by both 3 and 5.

# Q7
# Continuously take input number n from the user
# and print whether it is positive or negative,
# until the user enters "Quit".

# Q8
# Create a simple calculator function:
# calculator(a, b, operation)
# The operation parameter can be: '+', '-', '*', '/'
# Perform the correct arithmetic operation based on user input.

# Q9
# Write a function is_prime(n).
# Return True if n is a prime number, else return False.
# Hint:
# - Prime checking only for 2 or greater
# - A non-prime number divides by at least one number in [2, n-1]

# Q10
# Number Guessing Game:
# Choose a secret number (hardcoded by you).
# Ask the user to guess it and print:
# - "Too high" if guess > number
# - "Too low" if guess < number
# - "Correct!" if guess == number
