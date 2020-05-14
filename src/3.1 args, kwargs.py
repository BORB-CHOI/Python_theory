def plus(*args):
    result = 0
    for num in args:
        result += num
    print(result)


def printing(*args, **kwargs):
    print(args)
    print(kwargs)


plus(1, 3, 2, 4, 5, 6, 2)
printing(1, 12, 2, 3, 4, 5, 6, 76, asdh=True)
