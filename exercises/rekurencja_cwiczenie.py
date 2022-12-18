

def flatten(elements: list) -> list:
    """

    >>> flatten([])
    []

    >>> flatten([1, 2])
    [1, 2]

    >>> flatten([1, 2, 3, [4, 5, [6]], 7])
    [1, 2, 3, 4, 5, 6, 7]
    """
    result = []
    for el in elements:
        if isinstance(el, list):
            for e in flatten(el):
                result.append(e)
        else:
            result.append(el)
    return result


class Count:
    def __init__(self, function):
        self.function = function
        self.cnt = 0

    def __call__(self, *args, **kwargs):
        self.function(*args, **kwargs)
        self.cnt += 1

@Count
def helloworld():
    print("Hello World!")
helloworld()
helloworld()
helloworld()
print(helloworld.cnt)