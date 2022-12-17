import package_example.modul_a  as x
from package_example.modul_a import funkcja_a_z_mod_a, sum_int as moda_sum_int

# to jest moduł

def sum_int(a: int, b: int) -> int:
    """

    """
    suma = a + b
    return suma

sum_int(1, 2)
moda_sum_int(1, 2)
funkcja_a_z_mod_a()
