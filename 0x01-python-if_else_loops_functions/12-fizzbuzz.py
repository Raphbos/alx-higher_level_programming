#!/usr/bin/python3
def fizzbuzz():
    for yes in range(1, 101):
        if not (yes % 3) and not (yes % 5):
            print("FizzBuzz ", end='')
        elif not (yes % 3):
            print("Fizz ", end='')
        elif not (yes % 5):
            print("Buzz ", end='')
        else:
            print("{} ".format(yes), end='')
