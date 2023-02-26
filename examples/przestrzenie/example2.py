a = 1


def foo():
    b = 2

    def baz():
        nonlocal b
        print(a)
        print(b)

        b += 10
        print("locals baz", locals())
        print(globals())

    print("locals foo", locals())
    baz()


foo()
