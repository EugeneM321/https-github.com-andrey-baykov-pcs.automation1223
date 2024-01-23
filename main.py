# age = 'a'
# first_name = 'Alex'
#
# print(age)
# print(first_name)
#
# print(type(int(age)))
# print(type(first_name))

#
# name = input("What is your age? ")
#
# print(type(name))

# a = 4
# b = 2
#
# c = a / b
# print(c)

# > < bigger smaller
# == equal
# != not equal
#
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# sign = input("Enter '+', '-', '/', '*': ")
#
# if sign == '+':
#     print(a + b)
# elif sign == '-':
#     print(a - b)
# elif sign == '/':
#     if b != 0:
#         print(a / b)
#     else:
#         print("Can't divide by zero")
# elif sign == "*":
#     print(a * b)
# else:
#     print("Invalid")
#
# print("End")

# name = str(input("First name and last name "))
# age = int(input("Age "))
#
#
# if age <= 16:
#     print("Free")
# elif 16 <= age <= 35:
#     sign = str(input("Do you have membership card? "))
#     if sign == "Yes":
#         print("$10")
#     else:
#         print("$15")
# if age > 35:
#     print("$20")
#
# print("End")

# for index in range(10):
#     if index == 2 or index == 7:
#         break
#     print(index, "Hello")

#
# index = 5
# while True:
#     index = index - 1
#     if index == 0:
#         continue
#     if index == -5:
#         break
#     print(index, "Welcome")


# a = 1  # int
# b = 1.1  # float
# c = 'abc'  # str
# d = True  # bool
#
# person_1_name = 'Alex'
# person_1_last_name = 'A'
# person_1_age = 23
# person_2_name = 'Mary'
# person_2_last_name = 'M'
# person_2_age = 20
# person_3_name = 'Andrey'
# person_3_last_name = 'A'
# person_3_age = 40
#
# # Array
#
# person_1 = ['Alex', 'A', 23]
# person_2 = ['Mary', 'M', 20]
# person_3 = ['Andrey', 'A', 40]
#
# # print(len(person_1))
# #
# # for index in range(len(person_1)):
# #     print(person_1[index])
#
#
# # a = 'hello'
# # print(len(a))
# #
# # for index in range(len(a)):
# #     print(a[index])
# #
# # for item in person_2:
# #     print(item)
#
# # string_1 = 'hello world'
# #
# # print(string_1.lower())
# # print(string_1.upper())
# # print(string_1.title())
#
# array_tuple = ('Class', 'September', 'January')
# print(array_tuple[1])
#
# array_list = ['Class', 'September', 'January']
# print(array_list[-3])
#
#
# array_dict = {
#     'first_name': 'Andrey',
#     'age': 22,
#     'yes_no': False,
#     0: 100,
#     1: 200,
#     3: '300',
#     'abc': [1, 'hello', 3]
# }
# print(array_dict['abc'][1])
#
# array_set = {1, 2, 3, 4, 5, 6, 3}
# print(array_set)
#
# a_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 250]
# print(tuple(a_list))

def print_statement(number):
    print(f"Your number is {number}")
    print(f"************************")


a = input("Enter a number 1: ")
print_statement(a)
b = input("Enter a number 2: ")
print_statement(b)
c = input("Enter a number 3: ")
print_statement(c)
d = input("Enter a number 4: ")
print_statement(d)


try:
    number = int(input("Enter a number: "))
except:
    print("Invalid input. Try again")





