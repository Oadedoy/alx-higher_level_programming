#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    
    max_int = my_list[0]
    for i in my_list:
        if my_list[i] < my_list[i + 1]:
            max_int = my_list[i + 1]
            return max_int
        else:
            return my_list[i]