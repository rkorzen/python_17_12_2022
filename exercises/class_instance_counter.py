
class Foo:
    count = 0

    def __init__(self):
        self.__class__.count += 1


    def __del__(self):
        self.__class__.count -= 1


assert Foo.count == 0
f = Foo()
assert Foo.count == 1
f = Foo()
print(Foo.count)
assert Foo.count == 1

del f
assert Foo.count == 0


