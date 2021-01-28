def z():
    print("Hello world")


def f(x):
    if callable(x):
        x()
    else:
        print(x)


f(z)
f(5)