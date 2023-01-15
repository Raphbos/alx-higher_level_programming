#!/usr/bin/python3
def fizzbuzz():
    yes = range(1, 101)	
    for yes in range(1, 101):
        if ((yes%3) == False) and ((yes%5) == False):
            print("FizzBuzz ", end='')
        elif (yes%3) == False:
            print("Fizz ", end='')
        elif (yes%5) == False:
            print("Buzz ", end='')
        else:
            print("{} ".format(yes), end='')
