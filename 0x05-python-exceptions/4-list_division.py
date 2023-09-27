#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for a in range(list_length):
        try:
            new_list = my_list_1[a] / my_list_2[a]
        except ZeroDivisionError:
            print("division by 0")
            new_list = 0
        except TypeError:
            print("wrong type")
            new_list = 0
        except IndexError:
            print("out of range")
            new_list = 0
        finally:
            new_list.append(new_list)

    return (new_list)
