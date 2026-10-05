import random

VOLBY = ["kámen", "nůžky", "papír"]
PORAZI = {"kámen": "nůžky", "nůžky": "papír", "papír": "kámen"}

def hra():
    skore = {"hrac": 0, "pocitac": 0, "remiza": 0}
    while True:
        tah = input("Kámen, nůžky nebo papír? (q = konec): ").strip().lower()
        if tah == "q":
            break
        if tah not in VOLBY:
            print("Neplatná volba, zkus znovu.")
            continue
        pocitac = random.choice(VOLBY)
        print(f"Počítač zvolil: {pocitac}")
        if tah == pocitac:
            print("Remíza.")
            skore["remiza"] += 1
        elif PORAZI[tah] == pocitac:
            print("Vyhrál jsi.")
            skore["hrac"] += 1
        else:
            print("Prohrál jsi.")
            skore["pocitac"] += 1

        if skore["hrac"] == 3 or skore["pocitac"] == 3:
            break

    if skore["hrac"] == 3:
        print("Vyhrál jsi celý zápas!")
    elif skore["pocitac"] == 3:
        print("Zápas vyhrál počítač.")
    print(f"Konečné skóre: ty {skore['hrac']}, počítač {skore['pocitac']}, remízy {skore['remiza']}")

hra()