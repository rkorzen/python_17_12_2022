"""
folder examples traktujemy jako root

Jeśli uruchomimy modul z folderu:

pakiekt_wewnetrzny

to dostaniemy błąd:

ModuleNotFoundError: No module named 'pakiet_zewnetrzny'

Jeśli odkomentujemy kod

# from pathlib import Path
# import sys

# # Ustawienie BASE_DIR i dodanie do sys.path
# BASE_DIR = Path(__file__).resolve().parent.parent.parent
# sys.path.insert(0, str(BASE_DIR))
# print(sys.path)

i uruchomim moduł to błędu nie będzie.

mozemy te uruchomić kod z poziomy katalogu examples - ale jako moduł

$ python3 -m pakiet_zewnetrzny.pakiet_wewnetrzny.modul_wewnetrzny


"""
# from pathlib import Path
# import sys

# # Ustawienie BASE_DIR i dodanie do sys.path
# BASE_DIR = Path(__file__).resolve().parent.parent.parent
# sys.path.insert(0, str(BASE_DIR))
# print(sys.path)


from pakiet_zewnetrzny.modul_zewnetrzny_2 import funkcja_z_modulu_zewnetrznego


def funkcja_z_modulu_wewnetrznego():
    print(f"funkcja z modułu {__name__} z pakietu {__package__}")


if __name__ == "__main__":

    funkcja_z_modulu_zewnetrznego()
