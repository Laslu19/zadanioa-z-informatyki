from math import sqrt, cos, sin

a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

def wyrazenie_1(a, b):
    return sqrt(7 / (a**3 + cos(b)))

def wyrazenie_2(a, b):
    return sin((a + b)**4 / (sqrt(11) + 1))

def wyrazenie_3(a):
    return (cos(a + 1) / (sqrt(5) + 3))**3

# Obliczenia
wynik_1 = wyrazenie_1(a, b)
wynik_2 = wyrazenie_2(a, b)
wynik_3 = wyrazenie_3(a)

# Wyświetlanie wyników
print(f"Wartość wyrażenia 1 dla a={a}, b={b}: {wynik_1}")
print(f"Wartość wyrażenia 2 dla a={a}, b={b}: {wynik_2}")
print(f"Wartość wyrażenia 3 dla a={a}: {wynik_3}")