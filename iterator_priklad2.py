class IteratorMocnin:
    def __init__(self, x):
        self.x = x
        self.aktualne_cislo = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.aktualne_cislo > self.x:
            raise StopIteration
        mocnina = self.aktualne_cislo ** 2
        self.aktualne_cislo += 1
        return mocnina

mocniny = IteratorMocnin(5)
for mocnina in mocniny:
    print(mocnina)