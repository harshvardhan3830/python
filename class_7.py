# Dictionaries

# my_dict = {"name": "Harshvardhan", "age": 26, "city": "Jaipur"}

# my_dict["city"] = "mumbai" #reassigning values
# print(my_dict["city"])

# print("city" in my_dict)


# print("My dict is ====>>>>> ", my_dict.items())


# Functions


# def max_of_three_numbers(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         print(num1)
#     elif num2 >= num1 and num2 >= num3:
#         print(num2)
#     else:
#         print(num3)


# max_of_three_numbers(10, 20, 1)


# fizz buzz

# num % 3 = 0.  fizz
# num % 5 = 0.  Buzz
# num %3 && num %  5 = 0    fizzbuzz


def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("fizz_buzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print("-1")


# 20

for i in range(20):
    fizz_buzz(i + 1)
