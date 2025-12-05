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
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    
class Rectangle(Shape):
    def __init__(self, length, breath):
        self.length = length
        self.breath = breath
    def area(self):
        return self.length * self.breath
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
    
c = Circle(5)
print(c.area)
r = Rectangle(3, 3)
print(r.area)
t = Triangle(5, 5)
print(t.area)

# Q5 – Vehicle → Car, Bike (inheritance)
# Your answer here:
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"{self.brand} ---> {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, seat):
        super().__init__(brand, model)
        self.seat = seat

    def __str__(self):
        return f"{super().__str__()} --> {self.seat}"

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def __str__(self):
        return f"{super().__str__()} --> {self.engine_cc}"
    
c = Car("Porche", "911 GT", 2)
b = Bike("Yamaha", "R15", 155)
print(c)
print(b)

# Q6 – Abstract Employee class + Intern, FullTimeEmployee, ContractEmployee
# Your answer here:
class Employee(ABC):
    @abstractmethod
    def calculate_salaryI():
        pass

class Intern(Employee):
    pass

class FullTimeEmployee(Employee):
    pass

class ContractEmployer(Employee):
    pass

# Q7 – Person class (constructor overloading via default params)
# Your answer here:


# Q8 – Player class with class variable to track count
# Your answer here:


# Q9 – Multiple inheritance: Herbivore, Carnivore, Omnivore → Bear
# Your answer here:


# Q10 – Mini OOP Chat System (User, Message, ChatRoom)
# Your answer here:
