def je_palindrom(retazec: str) -> bool:

    if len(retazec) <= 1:
        return True


    return (retazec[0] == retazec[-1]) and je_palindrom(retazec[1:-1])

print(je_palindrom("level"))  # -> True
print(je_palindrom("lehjdfvel"))  # -> False