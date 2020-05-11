def plus(x, y):
    return float(x) + float(y)


def minus(x, y):
    return float(x) - float(y)


def times(x, y):
    return float(x) * float(y)


def division(x, y):
    return float(x) / float(y)


def negation(x, y):
    return -float(x), -float(y)


def power(x, y):
    return float(x) ** float(y)


print(plus(5, "3"))
print(minus(5, "3"))
print(times(5, "3"))
print(division(5, "3"))
print(negation(5, "3"))
print(power(5, "3"))
