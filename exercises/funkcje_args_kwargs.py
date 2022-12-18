
def fill(*args, **kwargs):
    text = "\n".join(args)
    for k, v in kwargs.items():
        text = text.replace(f"${k}", str(v))
    return text


if __name__ == "__main__":
    assert fill("") == ""
    assert fill("$d") == "$d"
    assert fill("$d", d=50) == "50"
    assert fill("$d-$e", d=50, e="cos") == "50-cos"
    assert fill("cena $cena1", "waga $waga", cena1=10, waga=20) ==  "cena 10\nwaga 20"
    assert fill("cena y $x waga $y $z $d", x=10, y=20, z=10) == "cena y 10 waga 20 10 $d"

