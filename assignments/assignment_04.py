# --------------------------------------------
# Assignment 04 – Python Fundamentals (OOP)
# Template for Answers
# --------------------------------------------

# Q1 – BankAccount class with deposit, withdraw, check_balance
# Your answer here:

class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Money deposited successful...")
            print(f"{amount} is deposited in account number : {self.account_number}")
        else:
            print("Please enter atleast 1 Dollar")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Please enter at least 1 Dollar")
            return

        if amount > self.balance:
            print("You don't have enough money to withdraw!")
            return

        else:
            self.balance -= amount
            print("Money withdrawn successfully...")
            print(f"{amount} is withdrawn from account number: {self.account_number}")
                

    def check_balance(self):
        print(f"Current balance: {self.balance}")

ba = BankAccount(123334, "Shubh", 10000)
ba.check_balance()
ba.deposit(30000)
ba.check_balance()
ba.withdraw(450)
ba.check_balance()

# Q2 – Book class with reviews
# Your answer here:

class Book:
    def __init__(self, title, author, list_of_review):
        self.title = title
        self.author = author
        self.list_of_review = list_of_review

    def add_review(self, review):
        self.list_of_review.append(review)
        print("Review Added!")
    
    def count_review(self):
        print(f"There are {len(self.list_of_review)} reviews")

    def display_review(self):
        if len(self.list_of_review) == 0:
            print("No reviews yet.")
        else:
            for review in self.list_of_review:
                print(review)

b = Book("Harry Bhai", "Shubh", [])
b.add_review("This is the first review")
b.count_review()
b.add_review("This is second review")
b.add_review("This is third review")
b.display_review()
b.count_review()

# Q3 – Student class with encapsulation (getters/setters)
# Your answer here:

class Student:
    def __init__(self, name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

    def getter(self):
        return (f"Roll no {self.__roll_no} s name is {self.__name} has {self.__marks} marks ")
    
    def setter(self, name, marks, roll_no):
        if not name.strip():
            return "Can't be empty name"
        self.__name = name
        if marks < 0:
            return "Marks can't be less than 0"
        self.__marks = marks
        if roll_no < 1 or roll_no > 100:
            return "Can't be this big"
        self.__roll_no = roll_no

s = Student("Shubham", 10, 85)
print(s.getter())
print(s.setter("Sam", 44, 76))
print(s.getter())

# Q4 – Shape class and overridden area() in Circle, Rectangle, Triangle
# Your answer here:
class Shape:
    pass

class Circle(Shape):
    pass

# Q5 – Vehicle → Car, Bike (inheritance)
# Your answer here:
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

# Q6 – Abstract Employee class + Intern, FullTimeEmployee, ContractEmployee
# Your answer here:


# Q7 – Person class (constructor overloading via default params)
# Your answer here:


# Q8 – Player class with class variable to track count
# Your answer here:


# Q9 – Multiple inheritance: Herbivore, Carnivore, Omnivore → Bear
# Your answer here:


# Q10 – Mini OOP Chat System (User, Message, ChatRoom)
# Your answer here:
