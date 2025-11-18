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

def even_num_checker(num_1, num_2):
    start = min(num_1, num_2)
    end = max(num_1, num_2)
    print(f"Even numbers between {start} and {end} are ----")
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i)

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
        print("0 cannot be splitt....")
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

def count_digits(number):
    count = 0
    for i in number:
        count += 1
    print(count)

number = input("Enter a number you wanna count the total digits of = ")
count_digits(number)

# Q5
# Write a function that returns the sum of digits of a number n.

def sum_of_digits(number):
    sum = 0
    for i in number:
        sum += int(i)
    print(sum)
number = input("Enter a number you wanna find the sum of digits of = ")
sum_of_digits(number)

# Q6
# Write a program to print all numbers from 1 to 100
# that are divisible by both 3 and 5.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} is divisible by both 3 and 5")

# Q7
# Continuously take input number n from the user
# and print whether it is positive or negative,
# until the user enters "Quit".

flag = True
while flag:
    choice = input("Enter a number or 'Quit' to exit: ").strip()
    if choice.lower() == "quit":
        flag = False
        print("You can use our service anytime")
    elif choice.isdigit():
        num = int(choice)
        if num >= 0:
            print("The entered number is a positive number...")
        else:
            print("The entered number is a negative number...")

# Q8
# Create a simple calculator function:
# calculator(a, b, operation)
# The operation parameter can be: '+', '-', '*', '/'
# Perform the correct arithmetic operation based on user input.

num_1 = float(input("Enter your first number: "))
operation = input("'+', '-', '*', '/' ")
num_2 = float(input("Enter your second number: "))

match operation:

    case "+":
        print(f"The sum of {num_1} and {num_2} is = {num_1 + num_2}")
    case "-":
        print(f"The subtraction of {num_1} and {num_2} is = {num_1 - num_2}")
    case "*":
        print(f"The multiply of {num_1} and {num_2} is = {num_1 * num_2}")
    case "/":
        print(f"The divison of {num_1} and {num_2} is = {num_1 / num_2}")
    case _:
        print("Invalid operation entered.")

# Q9
# Write a function is_prime(n).
# Return True if n is a prime number, else return False.
# Hint:
# - Prime checking only for 2 or greater
# - A non-prime number divides by at least one number in [2, n-1]

def is_prime(n):
    if n < 2:
        print(f'{n} is not a prime number')
        return

    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is  not a prime number")
            return

    print(f"{n} is a prime number")

number = int(input("Enter a number to check whether it is prime or not = "))
is_prime(number)
# Q10
# Number Guessing Game:
# Choose a secret number (hardcoded by you).
# Ask the user to guess it and print:
# - "Too high" if guess > number
# - "Too low" if guess < number
# - "Correct!" if guess == number

SECRET_NUMBER = 45

while True:
    guess = int(input("Enter any number from (1-100) to guess = "))
    if guess > SECRET_NUMBER:
        print("Too High")
    elif guess < SECRET_NUMBER:
        print("Too Low")
    else:
        print("Correct!")
        break
    



# Could have used other ways too but I am limited to what is taught in class as these are the practice assignments according to what is taught in class.