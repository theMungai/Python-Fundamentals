import math
# pi = 3.14
# print(round(pi))
# print(math.ceil(pi))  -- round a number UP to a whole nearest integer
# print(math.floor(pi))    -- round a number DOWN to a whole nearest integer
# print(abs(pi))  -- gives you the absolute value of the number. How far the number is away from zero
# print(pow(pi,2))    --raised to power of
# print(math.sqrt(pi))  -- SQUARE ROOT

# name = ''
# while name != 'your name':
#     print('Please type your name.')
# name = input()
# print('Thank you!')



# def bill (username, amount, due_date):
#     print(f"Hey {username} ")
#     print(f"Your monthly salary amounting to KSh{amount} is due on {due_date} ")
# bill("Mungai", 5000, "9/7/2024")

# movies = [["Social Network", "Suicide Squad", "Barbie"], ["The 100", "Scandal", "Night Agent", "Under Paris",
#           "The Ultimatum"]]
# print(movies[1][::])

# myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
#
# spam = {'name': 'Zophie', 'age': 7}

#=============================================================================================================

# def greet (first_name, last_name):
#     print(f"Hi there {first_name} {last_name}")
#     print("Welcome aboard")
#     print()
#
#
# greet("Simon", "Mungai")
# greet("John", "Smith")


def increment (number, by = 2):
    return number + by


print(increment(10, 2))


#=======================================================================================================================

#calculating area of a trapezium
# upper_line = float(input('Enter length of upper line (cm): '))
# lower_line = float(input('Enter length of lower line (cm): '))
# height = float(input('Enter the height of a trapezium (cm): '))
#
# def area_of_a_trapezium():
#     Area = 0.5 * (upper_line + lower_line) * height
#     return Area
#
# Area = area_of_a_trapezium()
# print('Area of a trapezium = ' + str(Area) + 'cm2')

#=======================================================================================================================

# Calculating volume of a three-quarter of a sphere
#Volume of a three quarter of a sphere = 4/3(pi) * r**3

# from math import *
#
# radius = float(input('Enter Your radius: '))
# def volume_of_a_sphere():
#     volume = 3 / 4 * 4 / 3 * pi * radius ** 3
#     return volume
#
#
# Volume = volume_of_a_sphere()
# print('Volume of a three-quarters of a sphere is: ' + str(Volume) + 'cm3')

#=======================================================================================================================

# Calculating Simple Interest

# Principal = float(input('Enter the principal (KShs.): '))
# Rate = float(input('Enter the Interest Rate (%): '))
# Time = float(input('Enter the loan duration (years): '))
#
# Simple_interest = Principal * Rate/100 * Time
#
# def simple_interest():
#     Simple_interest = Principal * Rate / 100 * Time
#     return Simple_interest
#
# SI = simple_interest()
# print('The Simple Interest = ' + 'KShs.' + str(SI))






# Principal = float(input("Enter amount (KShs): "))
# Rate = float(input("Enter Your Rate(%): "))
# Time = float(input("Enter your given duration: "))
#
#
# def simple_interest():
#     simple_interest = Principal * Rate/100 * Time
#     return simple_interest
#
# SI = simple_interest()
# print("The total interest is KShs:" + str(SI))





















