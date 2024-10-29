import random



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