import sys

def check_even_odd(num):
    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

try:
    if len(sys.argv) == 1:
        raise AssertionError("AssertionError: no argument is provided")    
    elif len(sys.argv) != 2:
        raise AssertionError("AssertionError: more than one argument is provided")
    try:
        num = int(sys.argv[1])
    except ValueError:
        raise AssertionError("AssertionError: argument is not an integer")
    check_even_odd(num)
except AssertionError as e:
    print(e)
