# Hra Bulls and Cows

## Popis

Hra "Bulls and Cows" je klasická logická hra, ve které se hráč snaží uhodnout tajné čtyřmístné číslo, které je počítačem náhodně vygenerováno. Po každém zadání čísla hráč obdrží informaci o tom, kolik číslic se shoduje na správné pozici (**bulls**) a kolik číslic je přítomno v čísle, ale na špatné pozici (**cows**).

## Funkce

- **Generování náhodného čísla**: Program generuje tajné čtyřmístné číslo bez opakujících se číslic.
- **Kontrola vstupu**: Hráč zadává 4místné číslo, program kontroluje, zda splňuje pravidla (4 číslice, unikátní, bez vedoucí nuly).
- **Počítání bulls a cows**: Po každém zadání čísla program informuje hráče o počtu **bulls** (číslích na správné pozici) a **cows** (číslích, které jsou v čísle, ale na jiném místě).
- **Čas hry**: Program sleduje čas, který hráč strávil hádáním, a zobrazuje ho ve formátu `minuty:sekundy:milisekundy`.
- **Opakování hry**: Po skončení hry se nabízí možnost zahrát znovu.

## Instalace

1. Stáhněte nebo naklonujte tento repozitář.
    ```bash
    git clone https://github.com/JehorB/project_2-Bulls_and_Cows.git
    ```
2. Ujistěte se, že máte nainstalovanou správnou verzi Pythonu (doporučeno Python 3.13 a vyšší).
3. Pokud máte externí závislosti (například v souboru `requirements.txt`), nainstalujte je pomocí příkazu:

    ```bash
    pip install -r requirements.txt
    ```

4. Spusťte hru:

    ```bash
    python main.py
    ```

## Použité knihovny

- **os**: pro vyčištění obrazovky.
- **sys**: pro správu výstupu na obrazovku.
- **time**: pro sledování času hry.
- **random**: pro generování náhodného čísla.
- **textwrap**: pro zlepšení čitelnosti výstupních řetězců.

## Příklad chodu programu

![](screenshots/image_1.jpeg)

## Poznámky

- Hra používá standardní knihovnu Pythonu, a tedy nevyžaduje instalaci dalších závislostí, pokud nepoužíváte externí knihovny.
- Podporovány jsou operační systémy Windows, macOS a Linux.
- Pro zobrazení "běžícího textu" nebo pro vyčištění obrazovky jsou použity systémové příkazy (`cls` pro Windows a `clear` pro Unix-systémy).

## Licence

Tento projekt je licencován pod licencí MIT. Další informace naleznete v souboru LICENSE.

### Autor
* [Yehor Baranov](https://github.com/JehorB)