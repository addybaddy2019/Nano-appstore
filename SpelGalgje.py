import random 


def kies_woord(moeilijkheidsgraad):
    """Kiest een woord op basis van de moeilijkheidsgraad."""
    try:
        if moeilijkheidsgraad == "1":  # Checkt of je de makkelijke optie hebt gekozen
            with open("woordenlijst_mak.txt", "r") as file:  # Opent het bestand met makkelijke woorden
                woorden = file.readlines()  # Leest alle woorden uit het bestand
        elif moeilijkheidsgraad == "2":  # Checkt of je de gemiddelde optie hebt gekozen
            with open("woordenlijst_oke.txt", "r") as file:  # Opent het bestand met gemiddelde woorden
                woorden = file.readlines()  # Leest alle woorden uit het bestand
        elif moeilijkheidsgraad == "3":  # Checkt of je de moeilijke optie hebt gekozen
            with open("woordenlijst_moei.txt", "r") as file:  # Opent het bestand met moeilijke woorden
                woorden = file.readlines()  # Leest alle woorden uit het bestand
        else:
            print("Ongeldige moeilijkheidsgraad. Kies uit makkelijk, gemiddeld of moeilijk.")  # Zegt dat je een verkeerde optie hebt gekozen
            return None

        return random.choice([woord.strip() for woord in woorden]).upper()  # Kiest een willekeurig woord, haalt spaties weg en maakt alles hoofdletters
    except FileNotFoundError:
        print("Kon het woordenbestand niet vinden.")  # Zegt dat het bestand niet gevonden kan worden
        return None

def speel_galgje(woord):
    """Speelt een potje galgje."""
    woord_voltooid = "_" * len(woord)  # Maak een lege representatie van het woord met streepjes
    geraden = False  # Houdt bij of het woord is geraden
    geraden_letters = []  # Lijst van reeds geraden letters
    geraden_woorden = []  # Lijst van reeds geraden woorden
    pogingen = 6  # Aantal pogingen dat de speler heeft

    print("Laten we Galgje spelen!")
    print(toon_galg(pogingen))  # Toon de huidige staat van de galg
    print(" ".join(woord_voltooid))  # Toon het huidige geraden woord met spaties tussen de letters
    print("\n")

    while not geraden and pogingen > 0:  # Blijf doorgaan totdat het woord is geraden of de pogingen op zijn
        gok = input("Raad een letter of het hele woord: ").upper()  # Vraag de speler om een letter of het hele woord te raden
        if len(gok) == 1 and gok.isalpha():  # Controleer of de invoer een enkele letter is
            if gok in geraden_letters:  # Controleer of de letter al eerder is geraden
                print(f"Je hebt de letter {gok} al geraden.")
            elif gok not in woord:  # Controleer of de letter niet in het woord zit
                print(f"{gok} zit niet in het woord.")
                pogingen -= 1  # Verminder het aantal pogingen
                geraden_letters.append(gok)  # Voeg de letter toe aan de lijst van geraden letters
            else:
                print(f"Goed zo! {gok} zit in het woord!")
                geraden_letters.append(gok)  # Voeg de letter toe aan de lijst van geraden letters
                woord_als_lijst = list(woord_voltooid)  # Zet het geraden woord in een lijst om het bij te werken
                indices = [i for i, letter in enumerate(woord) if letter == gok]  # Zoek de indices van de letter in het woord
                for index in indices:
                    woord_als_lijst[index] = gok  # Vervang de streepjes met de juiste letter
                woord_voltooid = "".join(woord_als_lijst)  # Zet de lijst terug naar een string
                if "_" not in woord_voltooid:  # Controleer of het hele woord is geraden
                    geraden = True
        elif len(gok) == len(woord) and gok.isalpha():  # Controleer of de invoer het hele woord is
            if gok in geraden_woorden:  # Controleer of het woord al eerder is geraden
                print(f"Je hebt het woord {gok} al geraden.")
            elif gok != woord:  # Controleer of het woord niet juist is
                print(f"{gok} is niet het juiste woord.")
                pogingen -= 1  # Verminder het aantal pogingen
                geraden_woorden.append(gok)  # Voeg het woord toe aan de lijst van geraden woorden
            else:
                geraden = True  # Het woord is correct geraden
                woord_voltooid = woord
        else:
            print("Ongeldige invoer.")

        print(toon_galg(pogingen))  # Toon de huidige staat van de galg
        print(" ".join(woord_voltooid))  # Toon het huidige geraden woord met spaties tussen de letters
        print("\n")

    if geraden:
        print(f"Gefeliciteerd! Je hebt het woord geraden: {woord}!")  # De speler heeft gewonnen
    else:
        print(f"Helaas, je hebt geen pogingen meer. Het woord was: {woord}.")  # De speler heeft verloren

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
    return stages[pogingen]  # Geef de status van de galg op basis van het aantal resterende pogingen