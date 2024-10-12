
import random
import json
from datetime import datetime

def main():
  """Toont het hoofdmenu en start het gekozen spel."""
  while True:
    print("\nWelkom bij Nano Store!")
    print("1. Raad het nummer")
    print("2. Galgje")
    print("3. dagboek")
    print("4. Afsluiten")

    keuze = input("Kies een spel (1-3): ")

    if keuze == "1":
      raad_het_nummer()
    elif keuze == "2":
      speel_galgje()
    elif keuze == "3":
      dag_boek()
    elif keuze == "4":
      print("Tot ziens!")
      break
    else:
      print("Ongeldige keuze. Probeer opnieuw.")


def dag_boek():
    return
 
# lijst maken waarvan de gebruiker uit kan kiezen wat hij/zij wil spelen. 

def speel_galgje():
    def kies_woord(moeilijkheidsgraad):
        """Kiest een woord uit het tekstbestand op basis van de moeilijkheidsgraad."""
        woorden = {}
        try:
            with open("makkelijk.txt", "r") as f:
                woorden["makkelijk"] = f.read().splitlines()
            with open("gemiddeld.txt", "r") as f:
                woorden["gemiddeld"] = f.read().splitlines()
            with open("moeilijk.txt", "r") as f:
                woorden["moeilijk"] = f.read().splitlines()
        except FileNotFoundError:
            print("Woordenlijst niet gevonden.")
            return None

        if moeilijkheidsgraad not in woorden:
            print("Ongeldige moeilijkheidsgraad.")
            return None

        return random.choice(woorden[moeilijkheidsgraad])

# word_list_ez = [
#     "appel", "auto", "fiets", "huis", "boom", "stoel", "tafel", "boek", "pen", "lamp",
#     "school", "koffer", "computer", "muis", "bord", "glas", "broek", "jas", "schoenen", "plant",
#     "tulp", "regen", "zon", "maan", "ster", "kind", "vogel", "vis", "kat", "hond",
#     "bal", "kaart", "weg", "vracht", "tas", "bed", "kussen", "laken", "zeep", "douche",
#     "tent", "koffie", "melk", "water", "boter", "brood", "kaas", "appelmoes", "sokken", "toets"
# ]
# word_list_oke = [
#     "camera", "horizon", "vakantie", "gadget", "architect", "elektronisch", "familie", "toerisme", "scenario", "parfum",
#     "strategisch", "docent", "inflatie", "museum", "restaurant", "bezoeker", "beheerder", "kabouter", "herinnering", "station",
#     "fantasie", "zwembad", "document", "kantoor", "wandeling", "verrassing", "evenement", "muziek", "concert", "schilderij",
#     "telefoon", "jurist", "tovenaar", "tandarts", "historicus", "kunstwerk", "thermometer", "uitzending", "symfonie", "bibliotheek",
#     "organisme", "grafiek", "commercieel", "architectuur", "schrijver", "universiteit", "paraplu", "gemeente", "kompas", "navigatie"
# ]
# word_list_diff = [
#     "psychologie", "xenofobie", "mysterieus", "paradox", "vernuftig", "ambtenarij", "quantumfysica", "synoniem", "chaos", "encyclopedie",
#     "hypothese", "constructie", "fysica", "karakteristiek", "idiosyncratisch", "juxtapositie", "ontwrichting", "bekwaamheid", "filosofie", "illusie",
#     "karaktereigenschap", "parlementariër", "delinquentie", "speculatie", "autobiografie", "procrastinatie", "inconsistentie", "verantwoordelijkheid", "reconstructie", "dialectiek",
#     "extravagant", "individu", "labyrint", "sociologie", "quarantaine", "volharding", "evolutionair", "perceptie", "transcendent", "machinist",
#     "ambiguïteit", "literaire", "substantieel", "cryptografie", "animositeit", "exclusiviteit", "fractaal", "methodologie", "ontologie", "introspectie"
# ]

def speel_galgje():
  """Speelt het galgje spel."""

  naam = input("Wat is je naam? ")
  moeilijkheidsgraad = input("Kies een moeilijkheidsgraad (makkelijk, gemiddeld, moeilijk): ")
  max_fouten = int(input("Hoeveel keer mag je raden? "))

  woord = kies_woord(moeilijkheidsgraad)                           # type: ignore
  if woord is None:
    return


def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    gegokten_leters = []
    gegokten_woorden = []
    tries = 6
    print("Laten we Galgje spelen!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Raad een letter of woord: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in gegokten_leters:
                print("Je hebt dit al geprobeerd: ", guess, "!")
            elif guess not in word:
                print(guess, "is niet in het woord :(")
                tries -= 1
                gegokten_leters.append(guess)
            else:
                print("Goed zo,", guess, "is in het woord!")
                gegokten_leters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in gegokten_woorden:
                print("Je hebt dit al geprobeerd: ", guess, "!")
            elif guess != word:
                print(guess, " is niet het woord :(")
                tries -= 1
                gegokten_woorden.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("ongeldige input")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Goed zo, je hebt het woord geraden!")
    else:
        print("Het spijt me, maar je hebt geen gokken meer. Het woord was " + word + ". Misschien heb je volgende keer meer geluk!")


def display_hangman(tries):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return stages[tries]

def main():
    naam = input("Wat is je naam? ")
    print(f"Welkom bij Galgje, {naam}!")
    difficulty = input("Kies een moeilijkheidsgraad (makkelijk, gemiddeld, moeilijk): ").lower()
    word = choose_word(difficulty)
    if word:
        play(word)
        while input("Wil je opnieuw spelen? (J/N) ").upper() == "J":
            difficulty = input("Kies een moeilijkheidsgraad (makkelijk, gemiddeld, moeilijk): ").lower()
            word = choose_word(difficulty)
            if word:
                play(word)

if __name__ == "__main__":
    main()











def raad_het_nummer():

    ### Raad het getal spel ###

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

    if poging < max_pogingen:
        print(f"Je hebt nog {max_pogingen - poging} poging(en) over.")
    else:
        print(f"Helaas, je hebt geen pogingen meer over. Het juiste getal was {random_getal}.")

### Raad het getal spel ###