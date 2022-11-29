#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        last = number % 10
#        print(f"{last}", end="")
    elif number < 0:
        last = abs(number) % 10
#        print(f"{last}", end="")
    else:
        last = 0
    return last
