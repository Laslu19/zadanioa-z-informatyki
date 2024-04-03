a = int(input("Podaj pierwszą liczbę całkowitą: "))
b = int(input("Podaj drugą liczbę całkowitą: "))

if a > b:
    print(f"Większa liczba to: {a}")
elif b > a:
    print(f"Większa liczba to: {b}")
else:
    print(a, "(są równe)")