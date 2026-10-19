def show_hierarchy(level):
    levels = {1: "CEO", 2: "Managers", 3: "Team Leaders", 4: "Employees"}
    if level > 4:          # base case: stop after Level 4
        return
    print("Level", level, "->", levels[level])
    show_hierarchy(level + 1)   # recursive call

show_hierarchy(1)

import math
import datetime
import random

travel = float(input("Enter Travel Expense: "))
food = float(input("Enter Food Expense: "))
hotel = float(input("Enter Hotel Expense: "))

total_expense = math.ceil(travel + food + hotel)

current_datetime = datetime.datetime.now()

booking_ref = random.randint(1000, 9999)

print("Total Travel Expense =", total_expense)
print("Current Date & Time =", current_datetime)
print("Booking Reference =", booking_ref)
