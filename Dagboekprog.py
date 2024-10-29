from datetime import datetime  
import json  


def dagboek():
    """Functie om een dagboekentry te maken."""
    datum = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Haalt de huidige datum en tijd op
    entry = input("Schrijf je dagboekentry: ")  # Vraagt je om je dagboek te schrijven
    try:
        schrijf_naar_bestand("dagboek.json", {"datum": datum, "entry": entry}, aanvullen=True)  # Schrijft het naar het bestand
        print("Entry succesvol opgeslagen.")
    except Exception as e:
        print(f"Fout bij het opslaan van de entry: {e}")  # Zegt dat er iets fout ging bij het opslaan
        
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