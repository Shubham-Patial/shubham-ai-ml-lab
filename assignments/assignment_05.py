# --------------------------------------------
# Assignment 05 – File Handling & JSON (TEMPLATE ONLY)
# --------------------------------------------
# Write ONLY the program structure with comments.
# Do NOT write the solutions or final code.
# --------------------------------------------


# Q1
# Create a program that:
# 1. Opens a file "names.txt" in write mode
# 2. Writes 5 user‑entered names (one per line)
# 3. Opens the same file in read mode and prints all names
names = ["Sam", "Tam", "Ram", "Sham", "Yam"]
with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

with open("names.txt", "r") as f:
    for line in f:
        print(line.strip())
# Q2
# Create a program that:
# 1. Opens a file "log.txt" in append mode
# 2. Adds a new log entry (example: "Program run successfully")
# 3. Opens the file in read mode and prints all logs

with open("log.txt", "a") as file:
    file.write("Program run successfully\n")

with open("log.txt", "r") as file:
    for line in file:
        print(line.strip())

# Q3
# 1. Create a list of numbers: [5, 10, 15, 20, 25]
# 2. Use list comprehension to create a new list of numbers greater than 15
# 3. Print the new list

numbers = [5, 10, 15, 20, 25]
new_list = [number for number in numbers if number > 15]
print(new_list)

# Q4
# 1. Create a Python dictionary with 3 cities and their populations
# 2. Save it to "cities.json"
# 3. Load the JSON and print each city with its population
# 4. Ask user for a new city & population and update the JSON file


# Q5
# Write a program that:
# 1. Tries to open "data.txt" in read mode
# 2. If file does not exist, catch the exception
# 3. Print: "File not found!"


# END OF ASSIGNMENT TEMPLATE
