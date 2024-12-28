"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
Bulls & Cows

author: Yehor Baranov
email: yhr.baranov@post.cz

"""
import os
from time import time, sleep
from random import sample, seed
from textwrap import dedent

separator = "-" * 52


# Pozdrav užitele / Greeting of the user
def salutation():
    """
    Funkce vrátí uvítací zprávu pro uživatele na začátku hry.
    Tato zpráva obsahuje název hry a stručné instrukce.

    Návratová hodnota:
        str: Uvítací zpráva pro uživatele.
    """
    return dedent(f"""
        Hi there!
        {separator}
        I've generated a random 4 digit number for you.
        Let's play a bulls and cows game.
        {separator}
        Enter a number:
        {separator}
    """).strip()


# Výběr tajného čísla / Selecting a secret number
def secret_number() -> str:
    """
    Funkce generuje náhodné čtyřciferné číslo bez opakujících se číslic.

    Návratová hodnota:
        str: Náhodné čtyřciferné číslo jako řetězec.
    """
    # seed(0) # Nastavení pevného čísla pro test
    # Generování náhodných čísel / Random number generation
    number = ''.join(sample("0123456789", 4))
    # Pokud je první číslo 0, generujte znovu / If the first number is 0, generate again
    while number[0] == 0:
        number = ''.join(sample("123456789", 4))
    return number


# Ověřuje vstup uživatele / Verifies user input
def check_input(guess: str) -> bool:
    """
    Funkce ověřuje, zda je vstup uživatele platný. 
    Vstup musí být čtyřmístné číslo, nesmí začínat nulou a nesmí obsahovat duplikáty.

    Parametry:
        guess (str): Vstupní řetězec, který uživatel zadal.

    Návratová hodnota:
        bool: True, pokud je vstup validní, jinak False.
    """
    if len(guess) != 4 or len(set(guess)) != 4 or not guess.isdigit() or guess[0] == "0":
        return False
    return True


# Srovnání čísel / Comparing numbers
def comparing_numbers(number_s, number_g: str, attempt: int, start_time: float) -> str:
    """
    Funkce porovnává zadané číslo (number_g) s tajným číslem (number_s) a vrátí
    počet "bulls" a "cows" podle pravidel hry. Pokud číslo uživatel uhodl,
    zavolá funkci stop_game() a vrátí vítězný výsledek.

    Parametry:
        number_s (str): Tajné číslo, které hráč hádá.
        number_g (str): Zadané číslo od hráče.
        attempt (int): Počet pokusů, které hráč již provedl.
        start_time (float): Čas začátku hry pro měření času.

    Návratová hodnota:
        str: Výsledek porovnání nebo vítězná zpráva.
    """
    if number_s == number_g:
        return stop_game(attempt, start_time)
    
    secret_used = []
    guess_used = []
    bulls = 0
    cows = 0
    
    # Počítáme bulls / Count the bulls
    for i in range(4):
        if number_s[i] == number_g[i]:
            bulls += 1
            cows += 1
            # Označení čísla jako použitého / Mark the number as used
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


# Konec hry / stop the game
def stop_game (attempt: int, start_time: float) -> str:
    """
    Funkce vypočítá čas, který hráč strávil hrou, a vrátí zprávu o vítězství včetně
    počtu pokusů a celkového času.

    Parametry:
        attempt (int): Počet pokusů, které hráč provedl.
        start_time (float): Čas začátku hry pro měření doby trvání.

    Návratová hodnota:
        str: Zpráva o vítězství a časovém výsledku.
    """
    end_time = time()
    game_duration = end_time - start_time # celkový čas hry
    display_time = format_game_time(game_duration)
    return dedent(f"""
            Correct, you've guessed the right number on {attempt} attempts
            in {display_time}
            That's amazing!
            """).strip()


# Formátování času hry / Game time formatting
def format_game_time(seconds: float) -> str:
    """
    Funkce formátuje čas na hodiny, minuty, sekundy a milisekundy.

    Parametry:
        seconds (float): Doba trvání hry v sekundách.

    Návratová hodnota:
        str: Formátovaný čas ve formátu "MMmin : SSsec : MMMms".
    """
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    millis = int ((seconds * 1000 % 1000))
    return f"{minutes:02}min : {secs:02}sec : {millis:03}ms"


# Průběh hry / Game progress
def major_game():
    """
    Hlavní herní smyčka. Zajišťuje hru, ve které hráč hádá tajné číslo. 
    Uživatel je vyzván k zadání čísla, které se porovnává s tajným číslem. 
    Funkce také sleduje počet pokusů a časový interval.

    Návratová hodnota:
        None
    """
    secret_num = secret_number()
    attempt = 1 # Počítadlo pokusů / Attempt counter
    start_time = time() #stopka / stopwatch

    while True:
        number_input = input(f">>> ").strip() # Vstup uživatele / User input
        if check_input(number_input):
            result = comparing_numbers(secret_num, number_input, attempt, start_time)
            print(f"{result}\n{separator}")
            if "Correct" in result:
                break
            attempt += 1
        else:
            print(dedent(f'''
                    {separator}
                    Your input is invalid. Please enter exactly 4 digits,
                    no duplicates, no leading zero, and only digits.
                    {separator}
            '''), end='')


# Spuštění hry / Start the game
def start_game():
    """
    Funkce spouští hru a po jejím dokončení nabízí hráči možnost hrát znovu nebo ukončit.
    Pokud hráč zadá "exit", hra se ukončí, jinak se spustí nová hra.

    Návratová hodnota:
        None
    """
    while True:
        print(salutation())
        major_game()
        # Spuštění nové hry / Start a new game
        play_again = input(dedent(f"""
                            Would you like to play again?
                            Press 'Enter' to play again or type 'exit' to quit.
                    """)).strip()
        if play_again.lower() == "exit":
            clear_screen()
            print(f"{separator}\n{"Game Over":^52}\n{separator}")
            sleep(3)
            break

# Čištění obrazovky / Screen cleanup
def clear_screen():
    """
    Funkce slouží k vyčištění obrazovky terminálu. Podle operačního systému 
    vybere správnou příkazovou funkci pro vyčištění obrazovky.

    - Pro Windows používá příkaz 'cls'.
    - Pro Linux a macOS používá příkaz 'clear'.
    
    Pokud není možné spustit příkaz pro vyčištění obrazovky (například v některých IDE), 
    funkce nebude dělat nic.

    Návratová hodnota:
        None
    """
    # Pro / for Windows
    if os.name == 'nt':
        os.system('cls')
    # Pro / for Linux, macOS
    else:
        os.system('clear')

start_game()