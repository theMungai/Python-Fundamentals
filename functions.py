# function =  a block of a reusable code.
#             place() after the function name to invoke it

# to define a function you use def

# Example:

#   # || Beginner ||
# def function_name(name, age):
#     print(f"Happy Birthday to {name}")
#     print("How old are you now")
#     print(f"I'm {age}years old")
#     print("Happy Birthday to you")
#
# function_name("Dorcas", 23)
# function_name("Dorcas", 23)
# function_name("Dorcas", 23)


# def girl(name,age):
#     print(f"{name} is curious")
#     print(f"{name} is also hardworking")
#     print(f"She is {age} years old")
#     print()
# girl("Daisy", 20)
# girl("Dorcas",23)



      # || RETURN STATEMENT ||

# return = a statement used to end a function
#         and send a result back to the caller

# Example;
# def add(x, y):
#     z = x + y
#     return z
#
#
# def subtract(x, y):
#     z = x - y
#     return z
#
#
# def multiply(x, y):
#     z = x * y
#     return z
#
#
# def divide(x, y):
#     z = x / y
#     return z
#
# print(divide(1, 2))

# _________________________________________________________________
# def create_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last
#
# full_name = create_name("dorcas", "kiget")
#
# print(full_name)

#
#
# weight_kg = float(input('enter your weight in kg :'))
# height_m = float(input('enter your height in metres: '))
#
#
# def calculate_BMI (weight_kg, height_m):
#     BMI = weight_kg / (height_m ** 2)
#     return BMI
#
# def interprete_BMI(BMI):
#
#     if BMI > 35 and BMI <= 40:
#         return 'Overweight'
#
#     elif BMI < 34 and BMI > 25:
#         return 'normal weight'
#
#     elif BMI < 24 and BMI > 18:
#         return 'underweight'
#
#     else:
#         return 'invalid'
#
# BMI= calculate_BMI (weight_kg, height_m)
# print(BMI)
#
# BMI_category = interprete_BMI(BMI)
# print(f"BMI Category: {BMI_category}")

#
# def calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term_years):
#     # Convert annual interest rate to monthly rate
#     monthly_interest_rate = annual_interest_rate / 12 / 100
#
#     # Convert loan term from years to months
#     loan_term_months = loan_term_years * 12
#
#     # Calculate monthly payment
#     if monthly_interest_rate > 0:
#         monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term_months) / (
#                     (1 + monthly_interest_rate) ** loan_term_months - 1)
#     else:
#         monthly_payment = loan_amount / loan_term_months
#
#     return monthly_payment


# ----------------------------------------------------------------------------------------------------------------------

# def function_name(parameters):
#     print("Hello There")   # body of statement

# function_name(arguments) # calling a function.



# IN PROGRAMMING WE HAVE 2 TYPES OF FUNCTIONS:
#     1. Functions that perform a task.
#     2. Functions that calculate and RETURN a value.


# 1. FUNCTIONS THAT PERFORM A TASK
# In this one you are locked to print something in the terminal.

# def greet_message(first_name, last_name):
#     print(f"Hello {first_name} {last_name}")
#     print("Hope you are doing fine")
#     print()
#
# greet_message("Simon", "Mungai")
# greet_message("Donald", "Trump")
# greet_message("Vladimir", "Putin")

#-----------------------------------------------------------------------------------------------------------------------

#2. FUNCTIONS THAT CALCULATE AND RETURN A VALUE

# This one is NOT tied in printing something in the terminal.
# It simply returns a value.
# It is the best type of functions since it can be re-used in future.
# You can write it to a file.
# You can also send it in an email

# def get_greeting (name):
#     return f"Hi {name}"
#
# message = get_greeting("Mungai")
# print(message)

#-----------------------------------------------------------------------------------------------------------------------

#def increment(number, by):
 #   return number + by

 # result = increment(10 , 12)
 # print(result)
#print(increment(10, 12 ))   # both styles are the same.

# ----------------------------------------------------------------------------------------------------------------------

            #OPTIONAL PARAMETERS

# def increment(number, by=7):
#     return number + by
#
#
# print(increment(10))  # both styles are the same.


#===============================|| CALLING 2 FUNCTIONS ||===============================================================

# def greet(name):
#     """
#     This function takes a name as input and prints a greeting message.
#     """
#     print(f"Hello, {name}!")
#
# # Define the second function
# def square(number):
#     """
#     This function takes a number as input and returns its square.
#     """
#     return number ** 2
#
# # Example usage of the functions
# greet("Alice")  # Output: Hello, Alice!
# result = square(5)
# print(f"The square of 5 is: {result}")  # Output: The square of 5 is: 25

#=================================||  NUMBER OF ARGUMENTS  ||===========================================================
# Passing more than one arguements
# def multiply (*numbers):
#     print(numbers)
#
#
# multiply(2, 3, 4, 5)

#==================================|| Using tuples in loops  ||=========================================================

# def multiply(*numbers):
#     for number in numbers:
#         print(number)
#
#
# multiply(2, 3, 4, 5)

#=================================|| Multiplying arguments ||===========================================================

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total = total * number
#     return total
#
#
# print(multiply(2, 3, 4, 5))


#=======================================|| Passing Multiple Keyword Arguements  ||======================================
# def save_user(**user):
#     print(user)
#
#
# save_user(id=1, name="Simon", age=22)   # output = dictionary

#=========================================|| Accesing values of various keys ||=========================================

# def save_user(**user):
#     print(user)
#
#
# save_user(id=1, name="Simon", age=22)

#===========================================|| Scope ||=================================================================
# Refers to the region of the code where ab variable is defined.


#  1. Local Variable



#===============================|| Fizzbuzz Alogarithm ||===============================================================

Number = float(input("Enter Your Number: "))
def fizz_buzz():

    if (Number % 3 == 0) and (Number % 5 == 0):
        return "Fizz Buzz"

    if Number % 3 == 0:
        return "Fizz"

    if Number % 5 == 0:
        return "buzz"

    else:
        return "Invalid"


buzz = fizz_buzz()
print(buzz)











# correct_username = "admin"
# correct_password = "admin123"
#
# attempts = 0
# max_attempts = 3
#
# while attempts < max_attempts:
#     username = input("Enter your user name: ")
#     password = input("Enter your password: ")
#
#     if username == correct_username and password == correct_password:
#         print("Login successful, welcome.")
#         break
#     else:
#         print("Login unsuccessful!")
#         attempts = attempts + 1
#
#     if attempts == max_attempts:
#         print("Account blocked!!!")

























