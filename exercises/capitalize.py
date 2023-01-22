"""
# Exercise - capitalize

You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.

    alison heck => Alison Heck

Given a full name, your task is to capitalize the name appropriately.

## Input Format

A single line of input containing the full name S


## Constraints

    0 < len(S) < 1000
    The string consists of alphanumeric characters and spaces.

Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

## Output Format

Print the capitalized string S


## Examples

    a b => A B
    1 2 3  4 => 1 2 3  4
    a b c 4d => A B C 4d


"""


def solve(s):

    out = ""
    new_word = True
    for sign in s:
        if new_word:
            sign = sign.upper()
            new_word = False
        out += sign

        if sign == " ":
            new_word = True
    return out


# print("a b c 4d".title())

if __name__ == "__main__":
    assert solve("a b") == "A B"
    assert solve("1 2 3  4") == "1 2 3  4"
    assert solve("a b c 4d") == "A B C 4d"
