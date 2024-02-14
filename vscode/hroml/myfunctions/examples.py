def exampleTwoOne(input_x):
    if input_x == 0:
        raise ZeroDivisionError
    else:
        return (1/input_x + 3*input_x)

def exampleTwoSix(init, max_i):
    sum = 0
    for i in range(init, max_i+1):
        sum += i-1
    return sum

def exampleTwoSeven(init, max_i):
    sum = 0
    for i in range(init, max_i+1):
        sum += 3*i
    return sum