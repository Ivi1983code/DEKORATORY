import time

class TimeMeasurment:
    def __enter__(self):
        self.zaciatok = time.time()
        self.cas_zaciatku = time.strftime("%H:%M:%S")  # Čas
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.koniec = time.time()
        trvanie = int(self.koniec - self.zaciatok)
        print(f"Dokončené v čase {self.cas_zaciatku} - blok trval {trvanie} sekundy")



with TimeMeasurment() as t:
    cislo = 1
    for i in range(100000000):
        cislo += i
    print(cislo)