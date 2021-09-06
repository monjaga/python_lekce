def foo(x, y, z=0):
    return 100 * x + 10 * y + 1 * z


print(foo(1, 2, 3))
print(foo(1, 2))


def bar(args):
    for arg in args:
        print('bar arg =', arg)


bar([1, 2, 3])
