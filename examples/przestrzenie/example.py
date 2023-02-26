a = 1


def foo():
    b = 1
    global a
    a += 2  # a = a + 2
    print("z funkcji", a)
    print(locals())
    print(globals())


print("z globala przed foo", a)
foo()
print("z globala", a)
