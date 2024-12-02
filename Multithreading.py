import threading

class ThreadWithReturnValue(threading.Thread):
    def __init__(self, funkcia, argumenty=()):
        super().__init__(target=funkcia, args=argumenty)
        self.vysledok = None

    def run(self):
        self.vysledok = self._target(*self._args)

    def join(self):
        super().join()
        return self.vysledok

def scitaj_cisla(po):
    return sum(range(1, po + 1))

def nasob_cisla(po):
    vysledok = 1
    for i in range(1, po + 1):
        vysledok = vysledok * i
    return vysledok

scitanie = ThreadWithReturnValue(funkcia=scitaj_cisla, argumenty=(1000000,))
nasobenie = ThreadWithReturnValue(funkcia=nasob_cisla, argumenty=(100,))

scitanie.start()
nasobenie.start()

scitanie = scitanie.join()
nasobenie = nasobenie.join()

print("Súčet čísel od 1 do 1000000 je:", scitanie)
print("Násobenie čísel od 1 do 100 je:", nasobenie)