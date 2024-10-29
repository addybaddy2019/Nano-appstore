import random  
import json  
from datetime import datetime  
import Dagboekprog
import Raadhetnummerspel
import SpelGalgje

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
            Raadhetnummerspel.raad_het_nummer()
        elif keuze == "2":  # Start het spel 'Galgje' als je optie 2 kiest
            moeilijkheidsgraad = input("Kies een moeilijkheidsgraad (1 = makkelijk, 2 = gemiddeld, 3 = moeilijk): ")
            woord = SpelGalgje.kies_woord(moeilijkheidsgraad)
            if woord:
                SpelGalgje.speel_galgje(woord)
        elif keuze == "3":  # Laat je een dagboekentry maken als je optie 3 kiest
            Dagboekprog.dagboek()
        elif keuze == "4":  # Sluit het programma af als je optie 4 kiest
            print("Tot ziens!")
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")  # Zegt dat je een verkeerde keuze hebt gemaakt

if __name__ == "__main__":
    hoofdmenu()  # Start het hoofdmenu als het script wordt uitgevoerd