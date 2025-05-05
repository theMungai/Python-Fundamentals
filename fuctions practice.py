# 1 . Write a program to create a function that takes two arguments,
#-- name and age, and print their value.

# def name_and_age (name , age):
#     print(name , age)
#
#
# name_and_age("Simon", 24)


#=======================================================================================================================


# Exercise 2: Create a function with variable length of arguments

# def func1(*args):
#     for i in args:
#         print(i)
#
#
# func1(10, 20, 30)
# func1(40, 50)

#=======================================================================================================================

# Exercise 3: Return multiple values from a function

# Write a program to create function calculation() such that it can accept two variables
# and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.

# def calculation(a,b):
#     addition = a + b
#     subtraction = a - b
#
#     return addition, subtraction
#
#
#
# results = calculation(40,10)
# print(results)


#=======================================================================================================================

# Exercise 4: Create a function with a default argument

# Write a program to create a function show_employee() using the following conditions.
#
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

# def show_employee(name, salary =9000):
#     print("Name:",name, "Salary:", salary)
#
#
#
# show_employee("Simon", 12000)
# show_employee("Trump")


#=======================================================================================================================
# Exercise 5: Create an inner function to calculate the addition in the following way
# . Create an outer function that will accept two parameters, a and b
# . Create an inner function inside an outer function that will calculate the addition of a and b
# . At last, an outer function will add 5 into addition and return it

# def outer_fun(a, b):
#     square = a ** 2
#
#     # inner function
#     def addition(a, b):
#         return a + b
#
#     # call inner function from outer function
#     add = addition(a, b)
#     # add 5 to the result
#     return add + 5
#
# result = outer_fun(5, 10)
# print(result)

#=======================================================================================================================

#Exercise 6: Create a recursive function

# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

#A recursive function is a function that calls itself again and again.
# def addition(num):
#     if num:
#         # call same function by reducing number by 1
#         return num + addition(num - 1)
#     else:
#         return 0
#
# res = addition(10)
# print(res)



#=======================================================================================================================

#Exercise 7: Assign a different name to function and call it through the new name

# def display_student(name, age):
#     print(name, age)
#
#
# display_student("Emma", 26)
#
# showcase_teacher = display_student
#
# showcase_teacher("Simon", 30)


#=======================================================================================================================

# Exercise 8: Generate a Python list of all the even numbers between




#=======================================================================================================================

# Exercise 9: Find the largest item from a given list

# x = [4, 6, 8, 24, 12, 2]
# print(max(x))

#======================================================================================================================
#calculating BMI
# weight_kg = input("Enter Your Weight(kg): ")
# height_m = input(("Enter your height(m): "))
#
# def calculate_BMI(weight_kg, height_m):
#     BMI = weight_kg/height_m **2
#     return BMI
#
#     def interprete_BMI(weight_kg,height_m):
#         if BMI >= 40:
#             return "Obesity III (Severe)"
#
#         elif BMI < 40 and BMI == 35:
#             return "Obesity II"
#
#         elif BMI < 35 and BMI == 30:
#             return "Obesity I"
#
#         elif BMI < 30 and BMI == 25:
#             return "Overweight"
#
#         elif BMI < 25 and BMI == 19:
#             return "Normal Weight"
#
#         else:
#             return "Underweight"
#
#
#
# BMI = calculate_BMI(weight_kg, height_m)
# print(f"Your BMI = {BMI}")
#
# BMI = interprete_BMI()
# print()

