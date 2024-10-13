import random  
import json  
from datetime import datetime  

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

def schrijf_naar_bestand(bestands_pad, data, aanvullen=False):
    """Schrijft data naar een JSON-bestand."""
    if aanvullen:  # Checkt of je data moet toevoegen aan een bestaand bestand
        try:
            with open(bestands_pad, 'r') as bestand:  # Opent het bestand om de bestaande data te lezen
                bestaande_data = json.load(bestand)  # Laadt de bestaande data uit het bestand
            bestaande_data.update(data)  # Voegt de nieuwe data toe aan de bestaande data
            with open(bestands_pad, 'w') as bestand:  # Opent het bestand opnieuw om de bijgewerkte data op te slaan
                json.dump(bestaande_data, bestand, indent=4)  # Schrijft alles terug in het bestand, netjes met inspringingen
        except FileNotFoundError:
            print("Bestand niet gevonden. Er wordt een nieuw bestand aangemaakt.")  # Zegt dat het bestand niet gevonden is, dus er wordt een nieuw bestand gemaakt
            with open(bestands_pad, 'w') as bestand:  # Maakt een nieuw bestand aan
                json.dump(data, bestand, indent=4)  # Schrijft de nieuwe data in het nieuwe bestand
    else:
        with open(bestands_pad, 'w') as bestand:  # Opent het bestand om te schrijven (of maakt een nieuw bestand)
            json.dump(data, bestand, indent=4)  # Schrijft de nieuwe data erin

def speel_galgje(woord):
    """Speelt een potje galgje."""
    woord_voltooid = "_" * len(woord)  # Maakt een string met streepjes voor elk letter van het woord
    geraden = False  # Houdt bij of het woord al geraden is
    geraden_letters = []  # Lijst om alle letters die al geraden zijn op te slaan
    geraden_woorden = []  # Lijst om alle woorden die al geraden zijn op te slaan
    pogingen = 6  # Je hebt 6 kansen om te raden

    print("Laten we Galgje spelen!")
    print(toon_galg(pogingen))  # Laat zien hoeveel fouten je al hebt gemaakt
    print(woord_voltooid)  # Laat zien hoe ver je bent met het woord
    print("\n")

    while not geraden and pogingen > 0:  # Blijft doorgaan totdat je het woord raadt of je geen pogingen meer hebt
        gok = input("Raad een letter of het hele woord: ").upper()  # Vraagt je om een letter of het hele woord te raden
        if len(gok) == 1 and gok.isalpha():  # Checkt of je één letter hebt ingevoerd
            if gok in geraden_letters:  # Als je die letter al hebt geprobeerd
                print(f"Je hebt de letter {gok} al geraden.")
            elif gok not in woord:  # Als de letter niet in het woord zit
                print(f"{gok} zit niet in het woord.")
                pogingen -= 1  # Je verliest een poging
                geraden_letters.append(gok)  # Voeg de letter toe aan de lijst van al geraden letters
            else:
                print(f"Goed zo! {gok} zit in het woord!")  # Als de letter wel in het woord zit
                geraden_letters.append(gok)  # Voeg de letter toe aan de lijst van al geraden letters
                woord_als_lijst = list(woord_voltooid)  # Zet het woord in een lijst zodat je letters kunt veranderen
                indices = [i for i, letter in enumerate(woord) if letter == gok]  # Vind de plekken waar de letter zit
                for index in indices:
                    woord_als_lijst[index] = gok  # Vervang de streepjes met de juiste letter
                woord_voltooid = "".join(woord_als_lijst)  # Zet alles weer in een string
                if "_" not in woord_voltooid:  # Als er geen streepjes meer zijn, heb je het woord geraden
                    geraden = True
        elif len(gok) == len(woord) and gok.isalpha():  # Checkt of je het hele woord hebt geraden
            if gok in geraden_woorden:  # Als je het woord al hebt geprobeerd
                print(f"Je hebt het woord {gok} al geraden.")
            elif gok != woord:  # Als het niet het juiste woord is
                print(f"{gok} is niet het juiste woord.")
                pogingen -= 1  # Je verliest een poging
                geraden_woorden.append(gok)  # Voeg het geraden woord toe aan de lijst
            else:
                geraden = True  # Als het juiste woord is, zet je geraden op True
                woord_voltooid = woord  # Zet het woord helemaal vol
        else:
            print("Ongeldige invoer.")  # Zegt dat de invoer niet klopt

        print(toon_galg(pogingen))  # Laat zien hoeveel fouten je al hebt gemaakt
        print(woord_voltooid)  # Laat zien hoe ver je bent met het woord
        print("\n")

    if geraden:  # Als je het woord hebt geraden
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
    return stages[pogingen]  # Geeft de juiste weergave van de galg op basis van hoeveel pogingen je nog hebt

def dagboek():
    """Functie om een dagboekentry te maken."""
    datum = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Haalt de huidige datum en tijd op
    entry = input("Schrijf je dagboekentry: ")  # Vraagt je om je dagboek te schrijven
    try:
        schrijf_naar_bestand("dagboek.json", {"datum": datum, "entry": entry}, aanvullen=True)  # Schrijft het naar het bestand
        print("Entry succesvol opgeslagen.")
    except Exception as e:
        print(f"Fout bij het opslaan van de entry: {e}")  # Zegt dat er iets fout ging bij het opslaan

def raad_het_nummer():
    """Raad het nummer spel."""
    max_getal = int(input("Wat is het hoogste getal dat je wilt raden? "))  # Vraagt je om het hoogste getal te kiezen
    random_getal = random.randint(1, max_getal)  # Kiest een willekeurig getal tussen 1 en het gekozen maximum
    max_pogingen = int(input("Hoeveel keer mag je raden? "))  # Vraagt hoeveel keer je mag raden

    print(f"Je hebt {max_pogingen} pogingen om een getal tussen 1 en {max_getal} te raden.")

    for poging in range(1, max_pogingen + 1):  # Loopt door al je pogingen heen
        gok = int(input(f"Poging {poging}: Raad het getal: "))  # Vraagt je om een gok

        if gok == random_getal:  # Als je het juiste getal raadt
            print(f"Gefeliciteerd! Je hebt het juiste getal geraden in {poging} poging(en).")
            break
        elif gok < random_getal:  # Als je gok te laag is
            print("Fout! Het getal is hoger.")
        else:  # Als je gok te hoog is
            print("Fout! Het getal is lager.")

    if poging == max_pogingen and gok != random_getal:  # Als je al je pogingen hebt gebruikt en het niet goed hebt
        print(f"Helaas, je hebt geen pogingen meer. Het juiste getal was {random_getal}.")

def hoofdmenu():
    """Toont het hoofdmenu en start het gekozen spel."""
    while True:
        print("\nWelkom bij Nano Store!")
        print("1. Raad het nummer")
        print("2. Galgje")
        print("3. Dagboek")
        print("4. Afsluiten")

        keuze = input("Kies een optie (1-4): ")  # Vraagt je om een keuze te maken

        if keuze == "1":  # Start het spel 'Raad het nummer' als je optie 1 kiest
            raad_het_nummer()
        elif keuze == "2":  # Start het spel 'Galgje' als je optie 2 kiest
            moeilijkheidsgraad = input("Kies een moeilijkheidsgraad (1 = makkelijk, 2 = gemiddeld, 3 = moeilijk): ")
            woord = kies_woord(moeilijkheidsgraad)
            if woord:
                speel_galgje(woord)
        elif keuze == "3":  # Laat je een dagboekentry maken als je optie 3 kiest
            dagboek()
        elif keuze == "4":  # Sluit het programma af als je optie 4 kiest
            print("Tot ziens!")
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")  # Zegt dat je een verkeerde keuze hebt gemaakt

if __name__ == "__main__":
    hoofdmenu()  # Start het hoofdmenu als het script wordt uitgevoerd