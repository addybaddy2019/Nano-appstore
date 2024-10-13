
import random
import json
from datetime import datetime

def kies_woord(moeilijkheidsgraad):
    """Kiest een woord op basis van de moeilijkheidsgraad."""
    try:
        if moeilijkheidsgraad == "makkelijk":
            with open("woordenlijst_mak.txt", "r") as file:
                woorden = file.readlines()
        elif moeilijkheidsgraad == "gemiddeld":
            with open("woordenlijst_oke.txt", "r") as file:
                woorden = file.readlines()
        elif moeilijkheidsgraad == "moeilijk":
            with open("woordenlijst_moei.txt", "r") as file:
                woorden = file.readlines()
        else:
            print("Ongeldige moeilijkheidsgraad. Kies uit makkelijk, gemiddeld of moeilijk.")
            return None

        return random.choice([woord.strip() for woord in woorden]).upper()
    except FileNotFoundError:
        print("Kon het woordenbestand niet vinden.")
        return None

def speel_galgje(woord):
    """Speelt een potje galgje."""
    woord_voltooid = "_" * len(woord)
    geraden = False
    geraden_letters = []
    geraden_woorden = []
    pogingen = 6
    print("Laten we Galgje spelen!")
    print(toon_galg(pogingen))
    print(woord_voltooid)
    print("\n")

    while not geraden and pogingen > 0:
        gok = input("Raad een letter of het hele woord: ").upper()
        if len(gok) == 1 and gok.isalpha():
            if gok in geraden_letters:
                print(f"Je hebt de letter {gok} al geraden.")
            elif gok not in woord:
                print(f"{gok} zit niet in het woord.")
                pogingen -= 1
                geraden_letters.append(gok)
            else:
                print(f"Goed zo! {gok} zit in het woord!")
                geraden_letters.append(gok)
                woord_als_lijst = list(woord_voltooid)
                indices = [i for i, letter in enumerate(woord) if letter == gok]
                for index in indices:
                    woord_als_lijst[index] = gok
                woord_voltooid = "".join(woord_als_lijst)
                if "_" not in woord_voltooid:
                    geraden = True
        elif len(gok) == len(woord) and gok.isalpha():
            if gok in geraden_woorden:
                print(f"Je hebt het woord {gok} al geraden.")
            elif gok != woord:
                print(f"{gok} is niet het juiste woord.")
                pogingen -= 1
                geraden_woorden.append(gok)
            else:
                geraden = True
                woord_voltooid = woord
        else:
            print("Ongeldige invoer.")

        print(toon_galg(pogingen))
        print(woord_voltooid)
        print("\n")

    if geraden:
        print(f"Gefeliciteerd! Je hebt het woord geraden: {woord}!")
    else:
        print(f"Helaas, je hebt geen pogingen meer. Het woord was: {woord}.")

def toon_galg(pogingen):
    """Geeft de huidige status van de galg weer."""
    stages = [
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \
        --------
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     /
        --------
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |
        --------
        """,
        """
           --------
           |      |
           |      O
           |     \|
           |      |
           |
        --------
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
        --------
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
        --------
        """,
        """
           --------
           |      |
           |
           |
           |
           |
        --------
        """,
    ]
    return stages[pogingen]

def dagboek():
    """Functie om een dagboekentry te maken."""
    datum = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = input("Schrijf je dagboekentry: ")
    try:
        with open("dagboek.json", "a") as dagboek_file:
            json.dump({"datum": datum, "entry": entry}, dagboek_file)
            dagboek_file.write("\n")
        print("Entry succesvol opgeslagen.")
    except Exception as e:
        print(f"Fout bij het opslaan van de entry: {e}")

def raad_het_nummer():
    """Raad het nummer spel."""
    max_getal = int(input("Wat is het hoogste getal dat je wilt raden? "))
    random_getal = random.randint(1, max_getal)
    max_pogingen = int(input("Hoeveel keer mag je raden? "))

    print(f"Je hebt {max_pogingen} pogingen om een getal tussen 1 en {max_getal} te raden.")

    for poging in range(1, max_pogingen + 1):
        gok = int(input(f"Poging {poging}: Raad het getal: "))

        if gok == random_getal:
            print(f"Gefeliciteerd! Je hebt het juiste getal geraden in {poging} poging(en).")
            break
        elif gok < random_getal:
            print("Fout! Het getal is hoger.")
        else:
            print("Fout! Het getal is lager.")

    if poging == max_pogingen and gok != random_getal:
        print(f"Helaas, je hebt geen pogingen meer. Het juiste getal was {random_getal}.")

def hoofdmenu():
    """Toont het hoofdmenu en start het gekozen spel."""
    while True:
        print("\nWelkom bij Nano Store!")
        print("1. Raad het nummer")
        print("2. Galgje")
        print("3. Dagboek")
        print("4. Afsluiten")

        keuze = input("Kies een optie (1-4): ")

        if keuze == "1":
            raad_het_nummer()
        elif keuze == "2":
            moeilijkheidsgraad = input("Kies een moeilijkheidsgraad (makkelijk, gemiddeld, moeilijk): ").lower()
            woord = kies_woord(moeilijkheidsgraad)
            if woord:
                speel_galgje(woord)
        elif keuze == "3":
            dagboek()
        elif keuze == "4":
            print("Tot ziens!")
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")

if __name__ == "__main__":
    hoofdmenu()