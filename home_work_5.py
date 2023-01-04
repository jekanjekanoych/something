import random                                     # first_function


def get_random_value():
    return random.choice((1, 2, 3, 4, 5))


def get_random_values(choices, size=2):
    return random.choices(choices, k=size)


def retry(attempts=5, desired_value=None):

    def wrapper(func):

        def inner_wrapper(*args, **kwargs):

            for _ in range(attempts):

                if desired_value == func(*args, **kwargs):
                    return func(*args, **kwargs)

                return print('nothing was found')
        return inner_wrapper

    return wrapper


@retry(desired_value=3)
def get_random_value():
    return random.choice((1, 2, 3, 4, 5))


@retry(desired_value=[1, 2])
def get_random_values(choices, size=2):
    return random.choices(choices, k=size)


@retry(attempts=7, desired_value=3)
def get_random_value():
    return random.choice((1, 2, 3, 4, 5))


@retry(attempts=2, desired_value=[1, 2, 3])
def get_random_values(choices, size=2):
    return random.choices(choices, k=size)


print(get_random_value())
print(get_random_values([1, 2, 3, 4]))
print(get_random_values([1, 2, 3, 4], 3))
print(get_random_values([1, 2, 3, 4], size=1))


def print_squares(length_of_square, stop):           # second_function
    if length_of_square == 1:
        print('*')
        return
    if length_of_square == 2:
        print('**')
        return
    if stop == 0:
        print(length_of_square * '*')
    elif stop != length_of_square-1:
        print('*' + (length_of_square - 2) * ' ' + '*')
    else:
        print(length_of_square * '*')
        return

    print_squares(length_of_square, stop+1)


print_squares(length_of_square=4, stop=0)
