from string import ascii_lowercase

reversed_alphabet = ascii_lowercase[::-1]


def make_row(text):
    """
    ba -> b-a-b
    cba -> c-b-a-b-c

    """

    return "-".join(text + text[::-1][1:])

def make_rows(letters, longest_len):
    rows = []
    for i in range(len(letters)):
        fragment = letters[:i + 1]
        text = make_row(fragment)
        rows.append(text.center(longest_len, "-"))
    return rows + rows[::-1][1:]


def print_rangioli(size):
    letters = reversed_alphabet[-size:]
    longest = make_row(letters)
    longest_len = len(longest)
    return "\n".join(make_rows(letters, longest_len))

print(print_rangioli(10))


if __name__ == "__main__":
    expected = """--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------"""
    assert print_rangioli(5) == expected

    assert print_rangioli(3) == """----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----"""

    assert print_rangioli(2) == """--b--
b-a-b
--b--"""