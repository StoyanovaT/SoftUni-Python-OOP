from functools import wraps


def even_parameters(function):
    @wraps(function)
    def wrapper(*args):
        for num in args:
            if not isinstance(num, int) or num % 2 != 0:
                return "Please use only even numbers!"
        return function(*args)

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))
