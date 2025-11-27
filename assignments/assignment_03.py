# --------------------------------------------
# Assignment 03 – Python Fundamentals
# Date: 2025-11-25
# Student: Shubham Patial
# --------------------------------------------

# Q1 – Check if string is a palindrome
# Your answer here:

is_palindrome = input("Enter the string you want to check = ")
reversed_string = is_palindrome[::-1]
if reversed_string == is_palindrome:
    print(f"{is_palindrome} is palindrome...")
else:
    print(f"{is_palindrome} is not a palindrome string.")

# Q2 – Compute average of a list of integers
# Your answer here:

given_list = [2, 4, 5, 6, 7, 9, 3]
for i in given_list:
    total += i
avg = total/len(given_list)
print(avg)

# Q3 – Input two lists, merge them, sort result
# Your answer here:

list_1 = list(map(int, input("Enter a couple of integers in list one ").split()))
list_2 = list(map(int, input("Enter a couple of integers in list two =").split()))

merged_list = list_1 + list_2

merged_list.sort()

print(merged_list)

# Q4 – From a tuple: make tuple of evens & tuple of odds
# Your answer here:

given_tuple = (2,5,3,56, 21, 66, 341, 32, 65, 787, 98)
even_list = []
odd_list = []
for elm in given_tuple:
    if elm % 2 == 0:
        even_list.append(elm)
    else:
        odd_list.append(elm)
even_tuple = tuple(even_list)
odd_tuple = tuple(odd_list)
print(f"{even_tuple} is an even tuple")
print(f"{odd_tuple} is an odd tuple")

# Q5 – Dictionary menu program (Add, Update, Search, Display)
# Your answer here:

words = ["apple", "banana", "kiwi", "cherry", "mango"]
words_dict = {}
length = 0
for word in words:
    length = len(word)
    words_dict[word] = length
print(words_dict)

# Q6 – Dictionary mapping words to their lengths
# Your answer here:


# Q7 – Count spaces in a string
# Your answer here:


# Q8 – Check if two lists share no common elements
# Your answer here:


# Q9 – Print elements that appear more than once
# Your answer here:


# Q10 – Print unique characters + count
# Your answer here:
