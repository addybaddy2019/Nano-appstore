import random

def galgje():
    """
    Start het Galgje-spel, inclusief het kiezen van een woord, het spelen van een ronde, en het weergeven van de galgstatus.
    """
    moeilijkheidsgraad = input("Kies een moeilijkheidsgraad (1: makkelijk, 2: gemiddeld, 3: moeilijk): ")
    try:
        if moeilijkheidsgraad == "1":
            with open("woordenlijst_mak.txt", "r") as file:
                woorden = file.readlines()
        elif moeilijkheidsgraad == "2":
            with open("woordenlijst_oke.txt", "r") as file:
                woorden = file.readlines()
        elif moeilijkheidsgraad == "3":
            with open("woordenlijst_moei.txt", "r") as file:
                woorden = file.readlines()
        else:
            print("Ongeldige moeilijkheidsgraad. Kies uit makkelijk, gemiddeld of moeilijk.")
            return

        woord = random.choice([woord.strip() for woord in woorden]).upper()
    except FileNotFoundError:
        print("Kon het woordenbestand niet vinden.")
        return

    woord_voltooid = "_" * len(woord)
    geraden = False
    geraden_letters = []
    geraden_woorden = []
    pogingen = 6

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

    print("Laten we Galgje spelen!")
    print(stages[pogingen])
    print(" ".join(woord_voltooid))
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

        print(stages[pogingen])
        print(" ".join(woord_voltooid))
        print("\n")

    if geraden:
        print(f"Gefeliciteerd! Je hebt het woord geraden: {woord}!")
    else:
        print(f"Helaas, je hebt geen pogingen meer. Het woord was: {woord}.")

# Start het Galgje-spel
def main():
    galgje()

if __name__ == "__main__":
    main()  # Start het hoofdmenu als het script wordt uitgevoerd