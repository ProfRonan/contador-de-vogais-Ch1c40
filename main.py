"""This program counts the number of vowels in a string."""

def count_vowels(string:str) -> int:
    vogais = "aeiouAEIOU"
    quantidade = 0
    for char in string:
        if char in vogais:
            quantidade += 1
    return quantidade