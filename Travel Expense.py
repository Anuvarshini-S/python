import math, datetime, random

ticket = float(input("Enter ticket cost: "))
hotel = float(input("Enter hotel cost per night: "))
nights = int(input("Enter number of nights: "))
persons = int(input("Enter number of travellers: "))

total = round((ticket + hotel * nights) * 1.05, 2)    # total with 5% tax
per_person = math.ceil(total / persons)               # math module

print("\nDate & Time :", datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))   # datetime module
print("Booking Ref : TRV" + str(random.randint(1000, 9999)))                   # random module
print("Total       : Rs.", total)
print("Per Person  : Rs.", per_person)