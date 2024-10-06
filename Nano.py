
import random
import json
from datetime import datetime

def main():
  """Toont het hoofdmenu en start het gekozen spel."""
  while True:
    print("\nWelkom bij Nano Store!")
    print("1. Raad het nummer")
    print("2. Galgje")
    print("3. Afsluiten")

    keuze = input("Kies een spel (1-3): ")

    if keuze == "1":
      raad_het_nummer()
    elif keuze == "2":
      speel_galgje()
    elif keuze == "3":
      print("Tot ziens!")
      break
    else:
      print("Ongeldige keuze. Probeer opnieuw.")



# positionering van functies verbeteren 
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


def toon_woord(woord, geraden_letters):
  """Toont het woord met de geraden letters en streepjes voor de ongeraden letters."""
  weergave = ""
  for letter in woord:
    if letter in geraden_letters:
      weergave += letter
    else:
      weergave += "_"
  return weergave

def speel_galgje():
  """Speelt het galgje spel."""

  naam = input("Wat is je naam? ")
  moeilijkheidsgraad = input("Kies een moeilijkheidsgraad (makkelijk, gemiddeld, moeilijk): ")
  max_fouten = int(input("Hoeveel keer mag je raden? "))

  woord = kies_woord(moeilijkheidsgraad)
  if woord is None:
    return

  geraden_letters = []
  fouten = 0

  while fouten < max_fouten:
    print("\nWoord:", toon_woord(woord, geraden_letters))
    print("Geraden letters:", geraden_letters)
    print("Je hebt nog", max_fouten - fouten, "pogingen over.")

    gok = input("Raad een letter: ").lower()

    if len(gok) != 1 or not gok.isalpha():
      print("Ongeldige invoer. Voer één letter in.")
      continue

    if gok in geraden_letters:
      print("Je hebt deze letter al geraden.")
      continue

    geraden_letters.append(gok)

    if gok not in woord:
      fouten += 1
      print("Fout!")

    if all(letter in geraden_letters for letter in woord):
      print("\nGefeliciteerd! Je hebt het woord geraden:", woord)
      gewonnen = True
      break

  if fouten == max_fouten:
    print("\nHelaas, je hebt het woord niet geraden. Het woord was:", woord)
    gewonnen = False

  # Score opslaan (bonus)
  score = {
      "naam": naam,
      "gewonnen": gewonnen,
      "aantal_pogingen": fouten,
      "datum": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  }
  try:
    with open("score.txt", "a") as f:
      f.write(json.dumps(score) + "\n")
  except Exception as e:
    print("Fout bij het opslaan van de score:", e)

speel_galgje()













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