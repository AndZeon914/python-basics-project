"""
Домашнее задание №1
Функции и структуры данных
"""

from math import sqrt

def power_numbers(*args):
    x = []
    for i in args:
        x.append(i**2)
    return x

#print(power_numbers(1,2,3,4,5,7))


    # """
    # функция, которая принимает N целых чисел,
    # и возвращает список квадратов этих чисел
    # >>> power_numbers(1, 2, 5, 7)
    # <<< [1, 4, 25, 49]
    # """


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(xstr, d_type):
    x = []

    if d_type == EVEN:
        for i in xstr:
            if i % 2 == 0:
                x.append(i)

    elif d_type == ODD:
        for i in xstr:
            if i % 2 != 0:
                x.append(i)

    elif d_type == PRIME:
        for i in xstr:
            n = 2
            if i < 2:
                izPrime = False
            else:
                izPrime = True
            while n <= sqrt(i):
                if i % n == 0:
                    izPrime = False
                    break
                n += 1
            if izPrime:
                x.append(i)
    return x

print(filter_numbers([0,1,2,3,4,5,6,7,8,9,11,13], PRIME))


#for i in range(3, 6 // 3):
#print(4 // 2 + 1)

    # """
    # функция, которая на вход принимает список из целых чисел,
    # и возвращает только чётные/нечётные/простые числа
    # (выбор производится передачей дополнительного аргумента)
    #
    # >>> filter_numbers([1, 2, 3], ODD)
    # <<< [1, 3]
    # >>> filter_numbers([2, 3, 4, 5], EVEN)
    # <<< [2, 4]
    # """


# FAILED testing/test_homework_01/test_main.py::test_filter_numbers[0-odd] - as...
# FAILED testing/test_homework_01/test_main.py::test_filter_numbers[0-even] - a...
# FAILED testing/test_homework_01/test_main.py::test_filter_numbers[1-odd] - as...
# FAILED testing/test_homework_01/test_main.py::test_filter_numbers[1-even] - a...
# FAILED testing/test_homework_01/test_main.py::test_filter_numbers[2-odd] - as...
# FAILED testing/test_homework_01/test_main.py::test_filter_numbers[2-even] - a...
# FAILED testing/test_homework_01/test_main.py::test_filter_numbers[3-odd] - as...
# FAILED testing/test_homework_01/test_main.py::test_filter_numbers[3-even] - a...
# FAILED testing/test_homework_01/test_main.py::test_filter_numbers[4-odd] - as...
# FAILED testing/test_homework_01/test_main.py::test_filter_numbers[4-even] - a...
# FAILED testing/test_homework_01/test_main.py::test_filter_numbers[5-odd] - as...
# FAILED testing/test_homework_01/test_main.py::test_filter_numbers[5-even] - a...
# FAILED testing/test_homework_01/test_main.py::test_filter_numbers[6-odd] - as...
# FAILED testing/test_homework_01/test_main.py::test_filter_numbers[6-even] - a...
# FAILED testing/test_homework_01/test_main.py::test_filter_numbers[7-odd] - as...
# FAILED testing/test_homework_01/test_main.py::test_filter_numbers[7-even] - a...
# FAILED testing/test_homework_01/test_main.py::test_filter_numbers[8-odd] - as...
# FAILED testing/test_homework_01/test_main.py::test_filter_numbers[8-even] - a...
# FAILED testing/test_homework_01/test_main.py::test_filter_numbers[9-odd] - as...
# FAILED testing/test_homework_01/test_main.py::test_filter_numbers[9-even] - a...
# FAILED testing/test_homework_01/test_main.py::test_filter_numbers_consts[p0]
# FAILED testing/test_homework_01/test_main.py::test_filter_numbers_consts[p1]
# FAILED testing/test_homework_01/test_main.py::test_filter_numbers_consts[p2]
