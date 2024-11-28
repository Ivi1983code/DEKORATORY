import random

class IteratorNahodnychCisiel:
    def __init__(self):
        print('Inicializuj náhodnú kocku')
        self.ukoncit = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.ukoncit:
            raise StopIteration
        nahodne_cislo = random.randint(1, 6)
        if nahodne_cislo == 6:
            self.ukoncit = True
        return nahodne_cislo

kostka = IteratorNahodnychCisiel()
for hod_kostkou in kostka:
    print(f'Padlo {hod_kostkou}')
print('Ukončené.')