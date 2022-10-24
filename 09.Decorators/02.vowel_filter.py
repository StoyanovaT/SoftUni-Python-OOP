from functools import wraps


def vowel_filter(function):
    @wraps(function)
    def wrapper():
        letters = function()
        return [x for x in letters if x.lower() in "aeiouy"]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
