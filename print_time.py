import time

# Dekorátor
def print_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Uplynulý čas: {(end - start):.4f} sekúnd")
        return result
    return wrapper


@print_time
def dlha_funkcia():
    print("Spúšťam dlho trvajúcu funkciu...")
    time.sleep(1)
    print("Funkcia ukončená.")

dlha_funkcia()