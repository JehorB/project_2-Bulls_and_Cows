"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
Bulls & Cows

author: Yehor Baranov
email: yhr.baranov@post.cz

"""
from random import sample
from textwrap import dedent

separator = "-" * 48

# pozdrav užitele
def salutation():
    return dedent(f"""
        Hi there!
        {separator}
        I've generated a random 4 digit number for you.
        Let's play a bulls and cows game.
        {separator}
    """)

print(salutation()) # test funkci salutation() / pozdrav

# výběr tajného čísla
def secret_number() -> str:
    return ''.join(sample("123456789", 4))

print(secret_number()) # test funkci secret_number() / tajemne číslo

# Ověřuje vstup uživatele
def chek_input(number_input: str) -> bool:
    if number_input.isdigit() and \
        len(set(number_input)) == 4 and \
        number_input[0] != "0":
        return True
    else:
        return dedent(f'''
            Your input is invalid. Please enter exactly 4 digits,
            no duplicates, no leading zero, and only digits.
        ''')

print(chek_input("21d3")) # test funkci chek_input() / validuj_vstup