"""""""""""""""
Error messages
"""""""""""""""
errZero = "Cannot divide by zero."
errStr = "String or characters cannot be input to mathematical equation, please use integer only."
errFlt = "Cannot use float number, please use integer only."
errIdx = "Upper bound index must be greater than lower bound index."

"""""""""
Functions
"""""""""
def __checkOne(input):
    if input == 0:
        raise ZeroDivisionError(errZero)
    elif type(input) is float:
        raise ValueError(errFlt)
    elif type(input) is str:
        raise ValueError(errStr)

def __checkTwo(lower, upper):
    if type(lower) is float:
        raise ValueError(errFlt)
    elif type(upper) is float:
        raise ValueError(errFlt)
    elif type(lower) is str:
        raise ValueError(errStr)
    elif type(upper) is str:
        raise ValueError(errStr)
    elif upper < lower:
        raise IndexError(errIdx)
    return


def exampleTwoOne(input_x:int) -> float:
    """
    Calculate f(x)=(1/x + 3*x) based on input x

    :param int input_x: input to equation
    :return: f(x)
    :rtype: float
    :raises ZeroDivisionError: if input_x is equal to zero
    :raises ValueError: if input_x is a string
    """

    return (1/input_x + 3*input_x)

def exampleTwoSix(lower_b: int, upper_b: int) -> int:
    """
    Calculate summation of equation SUM(i-1) from lower to upper bounds of summation for integer i

    :param int lower_b: lower bound of summation
    :param int upper_b: upper bound of summation
    :return: summation
    :rtype: int
    :raises ValueError: if inputs are not integers
    :raises IndexError: if lower bound is greater than upper bound
    """

    __checkTwo(lower_b, upper_b)

    sum = 0
    for i in range(lower_b, upper_b+1):
        sum += i-1
    return sum

def exampleTwoSeven(lower_b: int, upper_b: int) -> int:
    """
    Calculate summation of equation SUM(3*i) from lower to upper bounds of summation for integer i

    :param int lower_b: lower bound of summation
    :param int upper_b: upper bound of summation
    :return: summation
    :rtype: int
    :raises ValueError: if inputs are not integers
    :raises IndexError: if lower bound is greater than upper bound
    """

    __checkTwo(lower_b, upper_b)
    
    sum = 0
    for i in range(lower_b, upper_b+1):
        sum += 3*i
    return sum