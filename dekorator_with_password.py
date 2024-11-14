def vyprintuj_a_pust(func):
    def nova_funkce(a,b):
        print(f"pouštíme funkci {func.__name__} s parametry {a}, {b}")
        return func(a,b)
    return nova_funkce

def with_password(func):
    def wrapper(*args, **kwargs):
        password = "lama"
        user_input = input("Zadajte heslo: ")
        if user_input == password:
            return func(*args, **kwargs)
        else:
            print("Nesprávne heslo.")
    return wrapper

@with_password
@vyprintuj_a_pust
def soucet(a,b):
    return a+b

@with_password
@vyprintuj_a_pust
def rozdil(a,b):
    return a-b


print(soucet(3,5))
print(rozdil(3,5))