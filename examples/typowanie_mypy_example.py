from typing import Union, Optional

a: int = 1
#           >= 3.10          < 3.10
# def suma(a: int | float, b: Union[int, float]) -> Union[int, float]:
#     return a + b


# Numeric = int | float # >3.10
Numeric = Union[int, float]

def suma(a: Numeric, b: Numeric, c: Optional[int] = None) -> Numeric:
    return a + b

print(suma(1, 2))
print(suma(1.1, 2.2))
# print(suma("a", "b"))