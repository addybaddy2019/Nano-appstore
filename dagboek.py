import json
from datetime import datetime

def dagboek(bestands_pad="dagboek.json", aanvullen=True):
    """
    Functie om een dagboekentry te maken en op te slaan in een JSON-bestand.

    Args:
        bestands_pad (str): Het pad naar het bestand waarin de dagboekentry moet worden opgeslagen.
        aanvullen (bool): Als True, voegt de entry toe aan het bestaande bestand, anders wordt het bestand overschreven.
    """
    # Haal de huidige datum en tijd op
    datum = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Vraag de gebruiker om een dagboekentry
    entry = input("Schrijf je dagboekentry: ")
    # Data die moet worden opgeslagen
    nieuwe_data = {"datum": datum, "entry": entry}

    try:
        # Controleer of data moet worden toegevoegd aan een bestaand bestand
        if aanvullen:
            try:
                # Lees de bestaande data uit het bestand
                with open(bestands_pad, 'r') as bestand:
                    bestaande_data = json.load(bestand)
                # Controleer of de bestaande data een lijst is, anders maak het een lijst
                if not isinstance(bestaande_data, list):
                    bestaande_data = [bestaande_data]
                bestaande_data.append(nieuwe_data)
            except FileNotFoundError:
                # Als het bestand niet bestaat, begin met een lege lijst
                bestaande_data = [nieuwe_data]
        else:
            # Als het bestand niet wordt aangevuld, begin met alleen de nieuwe data
            bestaande_data = [nieuwe_data]

        # Schrijf de bijgewerkte data naar het bestand
        with open(bestands_pad, 'w') as bestand:
            json.dump(bestaande_data, bestand, indent=4)

        print("Entry succesvol opgeslagen.")
    except Exception as e:
        print(f"Fout bij het opslaan van de entry: {e}")

# Voorbeeld van hoe de functie aan te roepen


def main():
    dagboek()

if __name__ == "__main__":
    main()  # Start het hoofdmenu als het script wordt uitgevoerd