from hroml import test

def ex21(input_x):
    if input_x == 0:
        raise ZeroDivisionError
    else:
        return (1/input_x + 3*input_x)