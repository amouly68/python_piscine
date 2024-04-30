def square(x: int | float) -> int | float:
    """ Returns the square of a number """
    return x * x


def pow(x: int | float) -> int | float:
    """ Returns the exponiation"""
    return x ** x


def outer(x: int | float, function) -> object:
    count = 0

    def inner() -> float:
        nonlocal count
        result = x
        count += 1
        for _ in range(count):
            result = function(result)
        return result
    return inner

# def outer(x: int | float, function) -> object:
#     count = 0
#     def inner() -> float:
#         nonlocal x
#         x = function(x)
#         return x

#     return inner
