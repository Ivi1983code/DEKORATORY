import pickle
import json

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

# Uložiť do pickle
def ulozit_do_pickle():
    nazov_suboru = input("Zadajte názov súboru na uloženie (napr. zoznam.pkl): ")
    try:
        with open(nazov_suboru, "wb") as subor:
            pickle.dump(nakupny_zoznam, subor)
        print(f"Zoznam bol uložený do súboru '{nazov_suboru}'.")
    except Exception as e:
        print(f"Chyba pri ukladaní do pickle: {e}")

# Načítať z pickle
def nacitat_zo_pickle():
    nazov_suboru = input("Zadajte názov súboru na načítanie (napr. zoznam.pkl): ")
    try:
        with open(nazov_suboru, "rb") as subor:
            nakupny_zoznam = pickle.load(subor)
        print(f"Zoznam bol načítaný zo súboru '{nazov_suboru}'.")
        vypisat_polozky()
    except Exception as e:
        print(f"Chyba pri načítaní z pickle: {e}")

# Uložiť do JSON
def ulozit_do_json():
    nazov_suboru = input("Zadajte názov súboru na uloženie (napr. zoznam.json): ")
    try:
        with open(nazov_suboru, "w", encoding="utf-8") as subor:
            json.dump(nakupny_zoznam, subor, ensure_ascii=False, indent=4)
        print(f"Zoznam bol uložený do súboru '{nazov_suboru}'.")
    except Exception as e:
        print(f"Chyba pri ukladaní do JSON: {e}")

# Načítať z JSON
def nacitat_zo_json():
    nazov_suboru = input("Zadajte názov súboru na načítanie (napr. zoznam.json): ")
    try:
        with open(nazov_suboru, "r", encoding="utf-8") as subor:
            nakupny_zoznam = json.load(subor)
        print(f"Zoznam bol načítaný zo súboru '{nazov_suboru}'.")
        vypisat_polozky()
    except Exception as e:
        print(f"Chyba pri načítaní z JSON: {e}")

# Hlavné menu
def menu():
    while True:
        print("\nNÁKUPNÝ ZOZNAM")
        print("1. Pridať položku")
        print("2. Vypísať všetky položky")
        print("3. Zmazať položku")
        print("4. Upraviť položku")
        print("5. Uložiť zoznam do pickle")
        print("6. Načítať zoznam z pickle")
        print("7. Uložiť zoznam do JSON")
        print("8. Načítať zoznam z JSON")
        print("9. Ukončiť")

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
            ulozit_do_json()
        elif volba == "8":
            nacitat_zo_json()
        elif volba == "9":
            print("Koniec programu.")
            break
        else:
            print("Nesprávna voľba, skúste znova.")

menu()