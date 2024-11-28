def GeneratorMien(predpona, koncovka):
    for predpona in predpona:
        yield predpona + koncovka

predpona = ["Ive", "Ane", "Evi", "Ani", "Ri"]
koncovka = "ta"


for meno in GeneratorMien(predpona, koncovka):
    print(f"Tvoje meno je {meno}.")