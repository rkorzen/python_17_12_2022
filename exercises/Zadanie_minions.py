"""
## Zadanie rozgrzewkowe

### Minions Game

Mamy Kevina i Stuarta oraz jakieś słowo

Kevin buduje ciągi znaków zaczynające się na samogłosek.
Stuart robi to samo, zaczynając od spółgłosek.

Dostają punkt za każdy ciąg znaków, który się zawiera w zadanym słowie. Jeśli ciąg występuję wiele razy do dostaje tyle punktów ile wystąpień

Wynik to nazwa wygranego gracza i jego punkty. Ewentualnie Draw - jeśli remis.
Słowa składają się z dużych liter.

### przykłady

Słowo A daje zwycięstwo Kevina (Kevin 1)
Słowo B daje zwycięstwo Stuartowi (Stuart 1)

Słowo AB daje zwycięstwo Kevina, ponieważ A daje 1 pkt i AB daje 1 pkt. Stuart ma tylko B. Więc wynik to Kevin 2

Weźmy słowo BANANA


| Stuart   |        | Kevin |          |
|----------|--------|-------|----------|
| Words    | Points | Words | Points   |
| B        | 1      | A     | 3        |
| N        | 2      | AN    | 2        |
| BA       | 1      | ANA   | 2        |
| NA       | 2      | ANAN  | 1        |
| BAN      | 1      | ANANA | 1        |
| NAN      | 1      |       |          |
| BANA     | 1      |       |          |
| NANA     | 1      |       |          |
| BANAN    | 1      |       |          |
| BANANA   | 1      |       |          |
|----------|--------|-------| -------- |
| Total    | 12     |       | 9        |

Wynik to Stuart 12

Słowo ABBA


| Stuart    |        | Kevin   |        |
|-----------|--------|---------|--------|
| Words     | Points | Words   | Points |
| B         | 2      | A       | 2      |
| BB        | 1      | AB      | 1      |
| BA        | 1      | ABB     | 1      |
| BBA       | 1      | ABBA    | 1      |
| --------- | ------ | ------- | ------ |
| Total     | 5      |         | 5      |

Wynik: Draw

### Przykładowe testy:

    assert minion_game("A") == "Kevin 1"
    assert minion_game("B") == "Stuart 1"
    assert minion_game("AB") == "Kevin 2"

    assert minion_game("BANANA") == "Stuart 12"
    assert minion_game("ALA") == "Kevin 4"

    assert minion_game("BAANANAS") == "Kevin 19"
    assert minion_game("ABBA") == "Draw"
    assert minion_game("BANANANAAAS") == "Draw"

"""

VOWELS = "AEIOU"

def minion_game(string: str) -> str:
    # stuart_score = 0
    # kevin_score = 0

    stuart_score = kevin_score = 0

    length = len(string)

    for i, letter in enumerate(string):
        if letter in VOWELS:
            kevin_score += length - i
        else:
            stuart_score += length - i

    if stuart_score == kevin_score:
        return "Draw"
    elif stuart_score > kevin_score:
        return f"Stuart {stuart_score}"
    else:
        return f"Kevin {kevin_score}"


if __name__ == "__main__":

    assert minion_game("A") == "Kevin 1"
    assert minion_game("B") == "Stuart 1"
    assert minion_game("AB") == "Kevin 2"

    assert minion_game("BANANA") == "Stuart 12"
    assert minion_game("ALA") == "Kevin 4"

    assert minion_game("BAANANAS") == "Kevin 19"
    assert minion_game("ABBA") == "Draw"
    assert minion_game("BANANANAAAS") == "Draw"