def add(n):
    return n+n

def run_lambdas():
    seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = filter(lambda x: x % 2 != 0, seq)
    print(result, type(result))

    numbers = (1, 2, 3, 4)
    numbers1 = (1, 2, 3, 4)
    numbers2 = (5, 6, 7, 8)
    result = map(add, numbers)
    print(list(result))

    result1 = map(lambda x, y: x+y, numbers1, numbers2)
    print(list(result1))

