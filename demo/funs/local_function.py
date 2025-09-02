v = 1  # Global Variable
def f1():
    global v
    v = 2
    a = 100   # Enclosing Variable
    # Local or nested function
    def f2():
        b = 200  # Local variable
        nonlocal a
        a = 10
        print(v, a, b)

    f2()
    print(a)

f1()
