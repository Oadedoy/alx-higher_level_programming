#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    counter = len(argv) - 1
    word = "arguments"

    if counter == 0:
        print(f"{counter} {word}.")
    elif counter != 1:
        print(f"{counter} {word}:")
    else:
        word = "argument"
        print(f"{counter} {word}:")

    if counter >= 1:
        for count, args in enumerate(argv):
            if count == 0:
                continue
            print(f"{count}: {args}")
