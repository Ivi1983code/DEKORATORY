import csv

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

def ulozit_do_csv():
    nazov_suboru = input("Zadajte názov súboru na uloženie (napr. zoznam.csv): ")
    try:
        with open(nazov_suboru, "w", newline="", encoding="utf-8") as subor:
            writer = csv.writer(subor)
            for polozka in nakupny_zoznam:
                writer.writerow([polozka])
        print(f"Zoznam bol uložený do súboru '{nazov_suboru}'.")
    except Exception as e:
        print(f"Chyba pri ukladaní: {e}")

def nacitat_zo_csv():
    nazov_suboru = input("Zadajte názov súboru na načítanie (napr. zoznam.csv): ")
    try:
        with open(nazov_suboru, "r", encoding="utf-8") as subor:
            reader = csv.reader(subor)
            global nakupny_zoznam
            nakupny_zoznam = [riadok[0] for riadok in reader]
        print(f"Zoznam bol načítaný zo súboru '{nazov_suboru}'.")
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
            ulozit_do_csv()
        elif volba == "6":
            nacitat_zo_csv()
        elif volba == "7":
            print("Koniec ")
            break
        else:
            print("Nesprávne, skúste znova.")


menu()