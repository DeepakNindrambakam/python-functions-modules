import mathon for addition
def add(a, b):
    return a + b

# Function for square root
def square_root(num):
    return math.sqrt(num)

# Function for power
def power(base, exponent):
    return math.pow(base, exponent)

# User input
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Addition:", add(x, y))
print("Square Root of first number:", square_root(x))
print("Power:", power(x, y))
import random

def guess_game():
    secret_number = random.randint(1, 10)

    guess = int(input("Guess a number between 1 and 10: "))

    if guess == secret_number:
        return "Correct Guess!"
    else:
        return f"Wrong! The number was {secret_number}"

# Function call
result = guess_game()
print(result)
import datetime

def show_datetime():
    current = datetime.datetime.now()
    return current

print("Current Date and Time:", show_datetime())
def calculate_average(marks):
    return sum(marks) / len(marks)

def find_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"

# Input marks
marks = []

for i in range(3):
    mark = int(input(f"Enter mark {i+1}: "))
    marks.append(mark)

average = calculate_average(marks)
grade = find_grade(average)

print("Average:", average)
print("Grade:", grade)
import random

def roll_dice():
    return random.randint(1, 6)

print("Rolling Dice...")
print("You got:", roll_dice())
import math

def circle_area(radius):
    return math.pi * radius * radius

r = float(input("Enter radius: "))


# Functi
print("Area of Circle:", circle_area(r))
from datetime import date

def calculate_age(birth_year):
    current_year = date.today().year
    return current_year - birth_year

year = int(input("Enter your birth year: "))

print("Your age is:", calculate_age(year))
