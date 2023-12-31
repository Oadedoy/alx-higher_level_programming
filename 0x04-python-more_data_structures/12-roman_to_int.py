#!/usr/bin/python3
def to_subtract(list_num):
    to_sub = 0
    max_list = max(list_num)

    for a in list_num:
        if max_list > a:
            to_sub += a

    return (max_list - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(numerals.keys())

    num = 0
    last_rom = 0
    list_num = [0]

    for char in roman_string:
        for r_num in list_keys:
            if r_num == char:
                if numerals.get(char) <= last_rom:
                    num += to_subtract(list_num)
                    list_num = [numerals.get(char)]
                else:
                    list_num.append(numerals.get(char))

                last_rom = numerals.get(char)

    num += to_subtract(list_num)

    return (num)#!/usr/bin/python3
def to_subtract(list_num):
    to_sub = 0
    max_list = max(list_num)

    for a in list_num:
        if max_list > a:
            to_sub += a

    return (max_list - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(numerals.keys())

    num = 0
    last_rom = 0
    list_num = [0]

    for char in roman_string:
        for r_num in list_keys:
            if r_num == char:
                if numerals.get(char) <= last_rom:
                    num += to_subtract(list_num)
                    list_num = [numerals.get(char)]
                else:
                    list_num.append(numerals.get(char))

                last_rom = numerals.get(char)

    num += to_subtract(list_num)

    return (num)
