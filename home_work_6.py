def get_even_or_odd_numbers(number, boolean):
    return [i for i in range(number) if i % 2 == 0 and boolean is True] or \
           [i for i in range(number) if i % 2 != 0]


def search_words(letters, *words):
    return [i for j in words for i in j if letters in i]


def flatten(*arr):
    yield from [i for k in arr for j in k for i in j]


if __name__ == '__main__':
    assert get_even_or_odd_numbers(3, True) == [0, 2]
    assert get_even_or_odd_numbers(4, False) == [1, 3]

    assert search_words('he', ['hello', 'orange', 'phenomenon']) \
           == ['hello', 'phenomenon']
    assert search_words('abc', ['hello', 'orange', 'phenomenon']) == []

    generator = flatten([[1, 2], [], [3, 4, 5]])
    assert next(generator) == 1
    assert next(generator) == 2
    assert next(generator) == 3
    assert next(generator) == 4
    assert next(generator) == 5
