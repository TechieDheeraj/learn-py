import functools
import operator

def add(n):
    return n+n

def run_lambdas():

    # Return chars only
    filter_chars = lambda s : ''.join([ch for ch in s if not ch.isdigit()]) 
    print("chars are:", filter_chars("h3ll0W0rld"))

    # used inside sorted function
    l = ["0", "-1", "-2", "2", "3"]
    print("sorted numerically: ", sorted(l, key=lambda x: int(x)))
    print("original list is ", l)

    """
       The filter() function in Python filters elements from an iterable 
       (like a list) based on a function (or None for truthy values). 
       It returns an iterator that yields those elements for which 
       the function returns True.
    """

    # filter positive even numbers
    seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -5, -4]
    result = list(filter(lambda x: not (x % 2 == 0 and x > 0), seq))
    print("filter out positive evens", result)

    numbers = (1, 2, 3, 4)
    numbers1 = (1, 2, 3, 4)
    numbers2 = (5, 6, 7, 8)
    result = map(add, numbers)
    print(list(result))

    """
       Returns a list of the results after applying the given function to 
       each item of a given iterable (list, tuple etc.)
    """
    # added each element of two tuples
    result1 = map(lambda x, y: x+y, numbers1, numbers2)
    print(list(result1))
    st = ['sat', 'bat', 'cat', 'mat']
    print("maps to list ", list(map(list, st)))

    """
        The reduce(fun,seq) function is used to apply a particular function 
        passed in its argument to all of the list elements mentioned in the 
        sequence passed along.This function is defined in “functools” module.
    """

    print("The sum of numbers are: ", functools.reduce(lambda a, b: a+b, numbers), end="\n")
    print("max element in list is ", functools.reduce(lambda a, b: a if a > b else b, numbers))
    print("with opertor functions:", functools.reduce(operator.mul, numbers))
    print(functools.reduce(operator.add, ["hello", "world"]))

