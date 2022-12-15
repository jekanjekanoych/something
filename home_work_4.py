number_one = int(input("Input first number: "))     # task_a
number_two = int(input("Input second number: "))


def function_one(a_1, b_1):

    if a_1 > b_1:
        print("The bigger number is: ", a_1)
    elif a_1 == b_1:
        print("Write another numbers")
    elif a_1 == b_1 == 0:
        print("Write another numbers")
    else:
        print("The bigger number is: ", b_1)


function_one(number_one, number_two)


number_one = int(input("Input first number: "))     # task_b
number_two = int(input("Input second number: "))
number_three = int(input("Input third number: "))


def function_two(a_2, b_2, c_2):
    if a_2 < b_2 and a_2 < c_2:
        print("The smaller number is: ", a_2)
    elif b_2 < c_2 and b_2 < c_2:
        print("The smaller number is: ", b_2)
    elif a_2 == b_2 == c_2 == 0:
        print("Write another numbers")
    elif a_2 == b_2 == c_2:
        print("Write another numbers")
    else:
        print("The smaller number is: ", c_2)


function_two(number_one, number_two, number_three)


number_one = int(input("Input number: "))     # task_с


def function_three(a_3):
    if a_3 < 0:
        return a_3 * (-1)
    return a_3


print(f"The absolute value of {number_one} is :", function_three(number_one))


number_one = int(input("Input first number: "))     # task_d
number_two = int(input("Input second number: "))


def function_four(a_4, b_4):
    amount = a_4 + b_4
    return amount


print(f"The amount of {number_one} and {number_two} is: ",
      function_four(number_one, number_two))


number_one = int(input("Input number: "))     # task_e


def function_five(a_5):
    if a_5 > 0:
        print("It's positive number")
    elif a_5 == 0:
        print("it's zero")
    else:
        print("It's negative number")


function_five(number_one)
