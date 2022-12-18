"""
wykonaj skrypt z opcją -O oraz bez niej:

$ python assert_debug_off.py

Traceback (most recent call last):
  File "/Users/rkorzen/PycharmProjects/szkolenia/k-python-2-17-12-2022/examples/assert_debug_off.py", line 16, in <module>
    assert max_value == 30
AssertionError

$ python -O assert_debug_off.py

(no assert)
"""


x = 30
y = 20
z = 10

max_value = z if z > y else y if y > z else x

assert max_value == 30
