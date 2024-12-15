"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
Bulls & Cows

author: Yehor Baranov
email: yhr.baranov@post.cz

"""
from random import sample, seed
from textwrap import dedent

separator = "-" * 52

# pozdrav užitele
def salutation():
    return dedent(f"""
        Hi there!
        {separator}
        I've generated a random 4 digit number for you.
        Let's play a bulls and cows game.
        {separator}
        Enter a number:
        {separator}
    """)

    # print(salutation()) # test funkci salutation() / pozdrav

# výběr tajného čísla
def secret_number() -> str:
    seed(0) # Nastavení pevného čísla pro test
    return ''.join(sample("123456789", 4))


# Ověřuje vstup uživatele
def check_input(number_input: str) -> bool:
    if number_input.isdigit() and \
        len(set(number_input)) == 4 and \
        number_input[0] != "0":
        return True
    else:
        return False


# srovnání čísel / comparing numbers
def comparing_numbers(number_s, number_g: str) -> bool:
    if number_s == number_g:
        return f"Correct, you've guessed the right number in 4 guesses!"
    
    secret_used = []
    guess_used = []
    bulls = 0
    cows = 0
    
    # Počítáme bulls / Count the bulls
    for i in range(4):
        if number_s[i] == number_g[i]:
            bulls += 1
            cows += 1
            secret_used.append(number_s[i])
            guess_used.append(number_g[i])

    # Počítáme cows / Count the cows
    for i in range(4):
        if number_g[i] != number_s[i]:
            if number_g[i] in number_s and \
            number_g[i] not in guess_used:
                cows += 1
                # Označení čísla jako použitého / Mark the number as used
                guess_used.append(number_g[i])
    return f"{bulls} bulls, {cows} cows"


# průběh hry
def major_game():
    print(salutation())
    secret_num = secret_number()
    while True:
        number_input = input(f">>> ")
        if check_input(number_input):
            result = comparing_numbers(secret_num, number_input)
            print(result)
            if "Correct" in result:
                break
        else:
            print(dedent(f'''
                    {separator}
                    Your input is invalid. Please enter exactly 4 digits,
                    no duplicates, no leading zero, and only digits.
                    {separator}
            '''))


major_game()