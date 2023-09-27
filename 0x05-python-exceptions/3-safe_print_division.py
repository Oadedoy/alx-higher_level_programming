#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        division = a / b
    except Exception:
        division = None
    finally:
        print("Inside division: {}".format(division))
        return (division)
