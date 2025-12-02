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
def add_student():
    name = input("Enter the name of the student = ")
    marks = int(input("Enter the mark of the student = "))
    student[name] = marks
    print("Student Added!!")

def update_student():
    name = input("Enter the name of the student you want to update marks of = ")
    if name in student:
        new_marks = int(input("Enter the new mark of the student = "))
        student[name] = new_marks
        print("Marks Updated!!")
    else:
        print("No student with this name found..")

def search_student():
    name = input("Enter the name of the student you want to search marks of = ")
    if name in student:
        print(f"{name} has {student[name]}")
    else:
        print("No student with this name found..")

def display():
    for name, marks in student.items():
        print(f"{name} : {marks}")

student ={}
while True:
    print("Press A to Add a student")
    print("Press B to Update marks")
    print("Press C to Search for a student")
    print("Press D to Display all data")
    print("Press E to exit program")

    choice = input("Enter your choice: ").upper()

    match choice:

        case "A":
            add_student()
        case "B":
            update_student()
        case "C":
            search_student()
        case "D":
            display()
        case "E":
            print("Exiting program...")
            break
        case _:
            print("Invalid choice. Try again.")
# Q6 – Dictionary mapping words to their lengths
# Your answer here:

words = ["apple", "banana", "kiwi", "cherry", "mango"]
words_dict = {}
length = 0
for word in words:
    length = len(word)
    words_dict[word] = length
print(words_dict)

# Q7 – Count spaces in a string
# Your answer here:

txt = input("Enter a string: ")
print("Number of spaces =", txt.count(" "))

# Q8 – Check if two lists share no common elements
# Your answer here:

list_1 = list(map(int, input("Enter a couple of integers in list one = ").split()))
list_2 = list(map(int, input("Enter a couple of integers in list two = ").split()))
flag = False
for n in list_2:
    if n in list_1:
        flag = True

if flag:    
    print("Both Lists share common elements")
else:
    print("Both Lists share non common elements")

# Q9 – Print elements that appear more than once
# Your answer here:

given_list = list(input("Enter a couple of integers in list one = ").split())
empty_list = []
empty_set = set()
for elm in given_list:
    if elm not in empty_list:
        empty_list.append(elm)
    else:
        empty_set.add(elm)
print(empty_set)



# Q10 – Print unique characters + count
# Your answer here:

given_string = input("Enter any string you want to = ")
unique_string = set(given_string)
print(f"{unique_string} are unique characters and the count is = {len(unique_string)}")