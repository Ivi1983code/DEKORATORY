import pickle

nakupny_zoznam = []

# Funkcie
def pridat_polozku():
    polozka = input("Zadajte názov položky: ")
    nakupny_zoznam.append(polozka)
    print(f"Položka '{polozka}' bola pridaná do zoznamu.")

def vypisat_polozky():
    if nakupny_zoznam:
        print("Váš nákupný zoznam:")
        for i, polozka in enumerate(nakupny_zoznam, start=1):
            print(f"{i}. {polozka}")
    else:
        print("Zoznam je prázdny.")

def zmazat_polozku():
    vypisat_polozky()
    try:
        cislo = int(input("Zadajte číslo položky na zmazanie: "))
        if 1 <= cislo <= len(nakupny_zoznam):
            zmazana = nakupny_zoznam.pop(cislo - 1)
            print(f"Položka '{zmazana}' bola zmazaná.")
        else:
            print("Nesprávne číslo.")
    except ValueError:
        print("Zadajte platné číslo.")

def upravit_polozku():
    vypisat_polozky()
    try:
        cislo = int(input("Zadajte číslo položky na úpravu: "))
        if 1 <= cislo <= len(nakupny_zoznam):
            nova_polozka = input("Zadajte nový názov položky: ")
            nakupny_zoznam[cislo - 1] = nova_polozka
            print(f"Položka č. {cislo} bola upravená na '{nova_polozka}'.")
        else:
            print("Nesprávne číslo.")
    except ValueError:
        print("Zadajte platné číslo.")

# ulozit pickle
def ulozit_do_pickle():
    nazov_suboru = input("Zadajte názov súboru na uloženie (napr. zoznam.pkl): ")
    try:
        with open(nazov_suboru, "wb") as subor:
            pickle.dump(nakupny_zoznam, subor)
        print(f"Zoznam bol uložený do súboru '{nazov_suboru}'.")
    except Exception as e:
        print(f"Chyba pri ukladaní: {e}")

# nacitat pickle
def nacitat_zo_pickle():
    nazov_suboru = input("Zadajte názov súboru na načítanie (napr. zoznam.pkl): ")
    try:
        with open(nazov_suboru, "rb") as subor:
            nakupny_zoznam = pickle.load(subor)
        print(f"Zoznam bol načítaný zo súboru '{nazov_suboru}'.")
        print("Obsah načítaného zoznamu:")
        vypisat_polozky()
    except Exception as e:
        print(f"Chyba pri načítaní: {e}")

# Hlavné menu
def menu():
    while True:
        print("\nNÁKUPNÝ ZOZNAM")
        print("1. Pridať položku")
        print("2. Vypísať všetky položky")
        print("3. Zmazať položku")
        print("4. Upraviť položku")
        print("5. Uložiť zoznam do súboru")
        print("6. Načítať zoznam zo súboru")
        print("7. Ukončiť")

        volba = input("Zvoľte možnosť: ")

        if volba == "1":
            pridat_polozku()
        elif volba == "2":
            vypisat_polozky()
        elif volba == "3":
            zmazat_polozku()
        elif volba == "4":
            upravit_polozku()
        elif volba == "5":
            ulozit_do_pickle()
        elif volba == "6":
            nacitat_zo_pickle()
        elif volba == "7":
            print("Koniec programu.")
            break
        else:
            print("Nesprávna voľba, skúste znova.")

menu()