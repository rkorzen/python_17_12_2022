from typing import Optional, Callable


def cut(elements: list, start: Callable, stop: Callable) -> list:
    result = []
    can_add = False
    for el in elements:
        if start(el):
            can_add = True

        if can_add:
            if stop(el):
                break
            result.append(el)

    return result


if __name__ == "__main__":
    assert cut([], start=lambda x: x, stop=lambda x: x) == []
    assert (
        cut([1, 2, 3, 4, 5, 6, 7, 8], start=lambda x: x > 3, stop=lambda x: x < 8) == []
    )
    assert cut(
        [1, 2, 3, 4, 5, 6, 7, 8], start=lambda x: x > 3, stop=lambda x: x == 8
    ) == [4, 5, 6, 7]
    assert (
        cut([1, 2, 3, 4, 5, 6, 7, 8], start=lambda x: x > 4, stop=lambda x: x < 7) == []
    )
    assert cut(
        [1, 2, 3, 4, 5, 6, 7, 8], start=lambda x: x > 4, stop=lambda x: x == 7
    ) == [5, 6]
    assert cut([1, 3, 5, 4, 6, 8], start=lambda x: True, stop=lambda x: x % 2 == 0) == [
        1,
        3,
        5,
    ]
