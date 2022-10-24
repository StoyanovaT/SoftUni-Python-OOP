def genrange(start, end):
    value = start

    while value <= end:
        yield value
        value += 1
    # ili:
    # return (x for x in range(start, end + 1))


print(list(genrange(1, 10)))