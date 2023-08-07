# Write a program to check whether a person is eligible to vote or not?

# print("Please input Your Age : ", end="")
# per1 = input()
# if 0 < int(per1):
#     if 18 <= int(per1):
#         print("You are eligible to vote.")
#     else:
#         print("You are not eligible to vote.")
# else:
#     print("input wrong age")

# -------///-----------///-----------///-------

# Write a program to check char is vowel or not.

# print("Please input any character : ", end="")
# vowel_1 = input()
# if vowel_1.isalpha():
#     if len(vowel_1) == 1 and vowel_1.isalpha():
#         if vowel_1 == "a" or vowel_1 == "A":
#             print(f"'{vowel_1}' is a Vowel")
#         elif vowel_1 == "e" or vowel_1 == "E":
#             print(f"'{vowel_1}' is a Vowel")
#         elif vowel_1 == "i" or vowel_1 == "I":
#             print("'{}' is a Vowel".format(vowel_1))
#         elif vowel_1 == "o" or vowel_1 == "O":
#             print("'{}' is a Vowel".format(vowel_1))
#         elif vowel_1 == "u" or vowel_1 == "U":
#             print("'%s' is a Vowel" % (vowel_1))
#         else:
#             print("'%s' is not a Vowel" % (vowel_1))
#     else:
#         print("Please enter a single alphabet character.")
# else:
#     print("Please enter a alphabet character.")

# -------///-----------///-----------///-------

# Write a program to check the number is positive or negative. User input.

# print("Please input any Number : ", end="")
# num_p_N = input()
# if 0 == int(num_p_N):
#     print("0 is not ")
# elif 0 < int(num_p_N):
#     print(f"{num_p_N} is Positive")
# else:
#     print(f"{num_p_N} is Negative")

# -------///-----------///-----------///-------

# Write a program to check whether a number is odd or even?
#
# print("input any Number : ", end="")
# even_odd = input()
# if int(even_odd) != 0:
#     if int(even_odd) % 2 == 0:
#         print(f"'{even_odd}' is Even")
#     else:
#         print(f"'{even_odd}' is Odd")
# else:
#     print(f"'{even_odd}' is not a even or odd ")

# -------///-----------///-----------///-------

# Write a program to display the grade of the user in subject A, ask user marks obtained out of 100
#
# print("Subject A marks input : ", end="")
# sub_A = input()
# if 0 <= float(sub_A) and 100 >= float(sub_A):
#     if float(sub_A) >= 80:
#         print("Grade A")
#     elif float(sub_A) >= 70 and float(sub_A) < 80:
#         print("Grade B+")
#     elif float(sub_A) >= 60 and float(sub_A) < 70:
#         print("Grade B")
#     elif float(sub_A) >= 50 and float(sub_A) < 60:
#         print("Grade C")
#     else:
#         print("Fail")
# else:
#     print("Please input correct marks")

# -------///-----------///-----------///-------

# Write a program to check whether a number is divisible by 7

# print("check number is divisible by 7")
# print("input any number : ", end="")
# num_check = input()
# if num_check.isdigit() :
#     if int(num_check) % 7 == 0:
#         print(f"{num_check} is divisible by 7")
#     else:
#         print(f"{num_check} is not divisible by 7")
# else:
#     print("input correct number")

# -------///-----------///-----------///-------

# Write a program to check if year is leap year.
#
# print("input a year : ", end="")
# leap_year = input("")
# if leap_year.isdigit():
#         if int(leap_year) % 400 == 0:
#             print(f"{leap_year} is a leap year")
#         else:
#             print(f"{leap_year} is not a leap year")
# else:
#     print("input correct year")

# -------///-----------///-----------///-------

# Write a program to ask user its name and check whether name consists of 5 or more letters
#
# print("Please input Your Name : ", end="")
# name = input("")
# if name.isalpha():
#     if len(name) > 5:
#         print("Your name consist is more than 5 letters")
#     elif len(name) == 5:
#         print("Your name consist in 5 letters")
#     else:
#         print("Your name consist in less than 5 letters")
# else:
#     print("input correct name")


# -------///-----------///-----------///-------

# Write a program that accepts 3 inputs from user. input 1 and input 2 should
# be numbers and the third input should be mathematical operator. Perform operation accordingly

# print("Calculator")
# print("input 1 number : ", end="")
# num_1 = input()
# print("input 2 number : ", end="")
# num_2 = input()
# print("input any + , - , * , / operator : ", end="")
# operator = input()
#
# if num_1.isdigit() and num_2.isdigit():
#     num_1 = int(num_1)
#     num_2 = int(num_2)
#     if operator == '+':
#         add = num_1 + num_2
#         print("{} + {} = {}".format(num_1, num_2, add))
#     elif operator == '-':
#         sub = num_1 - num_2
#         print("{} - {} = {}".format(num_1, num_2, sub))
#     elif operator == '*':
#         mul = num_1 * num_2
#         print("{} * {} = {}".format(num_1, num_2, mul))
#     elif operator == '/':
#         div = num_1 // num_2
#         print("{} / {} = {}".format(num_1, num_2, div))
#     else:
#         print("Wrong operator.")
# else:
#     print("input correct numbers.")

# -------///-----------///-----------///-------

# Write a program that accepts 1 input from user and check if the number is divisible by 2 and 3 both.

# print("check number is divisible by 2 and 3")
# print("input any number : ", end="")
# num_1 = input("")
#
# if int(num_1) % 2 == 0 and int(num_1) % 3 == 0:
#     print(f"{num_1} is divisible by 2 and 3")
# elif int(num_1) % 2 == 0:
#     print(f"{num_1} is divisible by 2")
# elif int(num_1) % 3 == 0:
#     print(f"{num_1} is divisible by 3")
# else:
#     print(f"{num_1} is not divisible by 2 and 3")

# -------///-----------///-----------///-------

# Write a program that accepts 2 inputs from user and check which number is largest.
#
# print("largest Number")
# print("input number 1 : ", end="")
# num_1 = input()
# print("input number 2 : ", end="")
# num_2 = input()
#
# if num_1 > num_2:
#     print(f"{num_1} is larger than {num_2}")
# else:
#     print(f"{num_2} is larger than {num_1}")

# -------///-----------///-----------///-------

# Write a program that accepts 3 input from user and check which number is largest.

# print("largest number")
# print("input number 1 : ", end="")
# num_1 = input()
# print("input number 2 : ", end="")
# num_2 = input()
# print("input number 3 : ", end="")
# num_3 = input()
#
# if num_1.isdigit() and num_2.isdigit() and num_3.isdigit():
#     if num_1 > num_2 and num_1 > num_3:
#         print(f"{num_1} is larger than {num_2} and {num_3}")
#     elif num_2 > num_1 and num_2 > num_3:
#         print(f"{num_2} is larger than {num_1} and {num_3}")
#     elif num_3 > num_1 and num_3 > num_2:
#         print(f"{num_3} is larger than {num_1} and {num_2}")
# else:
#     print("input correct numbers")

# -------///-----------///-----------///-------

# Write a program that accepts 3 input from user and check the second is largest.
#
# print("largest number")
# print("input number 1 : ", end="")
# num_1 = input()
# print("input number 2 : ", end="")
# num_2 = input()
# print("input number 3 : ", end="")
# num_3 = input()
#
# if num_1.isdigit() and num_2.isdigit() and num_3.isdigit():
#     if num_1 > num_2 and num_1 > num_3:
#         if num_2 > num_3:
#             print(f"{num_2} is larger than {num_3} and smaller than  {num_1}")
#         else:
#             print(f"{num_3} is larger than {num_2} and smaller than  {num_1}")
#     elif num_2 > num_1 and num_2 > num_3:
#         if num_1 > num_3:
#             print(f"{num_1} is larger than {num_3} and smaller than  {num_2}")
#         else:
#             print(f"{num_3} is larger than {num_2} and smaller than  {num_2}")
#     elif num_3 > num_1 and num_3 > num_2:
#         if num_1 > num_2:
#             print(f"{num_1} is larger than {num_3} and smaller than  {num_3}")
#         else:
#             print(f"{num_2} is larger than {num_2} and smaller than  {num_3}")
# else:
#     print("input correct numbers")

# -------///-----------///-----------///-------

# Write a python program that accept user an input. The valid input should be of following
# - GREEN or gREEN or green etc
# - RED or red or rEd etc
# - YELLOW or yellow or yELlOw etc

# program should display the following message on checking above input
# Car is allowed to go
# Car has to wait
# Car has to stop
# invalid input

# ############ANSWER#############

# print("input color : ", end="")
# color = input()
# if color.isalpha():
#     if color == "green" or color == "GREEN" or color == "Green" or color == "gREEN":
#         print("Car is allowed to go")
#     elif color == "red" or color == "RED" or color == "Red" or color == "rED":
#         print("Car has to wait")
#     elif color == "yellow" or color == "YELLOW" or color == "Yellow" or color == "yELLOW":
#         print("Car has to stop")
#     else:
#         print("Input correct Color")
# else:
#     print("Input  alphabets")

# -------///-----------///-----------///-------

# Write a program to trace your subject mark. Your program should fulfill the following conditions:

# If the subject mark is below 0 and above 100, print “error: mark should be between 0 and 100 only”
# display "you are fail" if their mark is below 50.
# display "you are pass" if they score 50 and above.
# If subject mark is between 50 and 60, Remark: Good
# If subject mark is between 60 and 80, Remark: Very Good
# If subject mark is between 80 and 100, Remark: Outstanding

# #############ANSWER#############

# print("Subject A marks input : ", end="")
# sub_A = input()
# if 0 <= float(sub_A) and 100 >= float(sub_A):
#     if float(sub_A) >= 80:
#         print("You are Pass \nRemark : Outstanding")
#     elif float(sub_A) >= 60 and float(sub_A) < 80:
#         print("You are Pass \nRemark : Very Good")
#     elif float(sub_A) >= 50 and float(sub_A) < 60:
#         print("You are Pass \nRemark : good")
#     else:
#         print("You are Fail")
# else:
#     print('"Error : mark should be between 0 and 100 only"')
#
