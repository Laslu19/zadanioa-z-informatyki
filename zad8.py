print("Wybierz sposób podania wymiarów trójkąta:")
print("1. Podstawa i wysokość")
print("2. Długości wszystkich boków")

wybor = int(input("Twój wybór (1 lub 2): "))

if wybor == 1:
    podstawa = float(input("Podaj długość podstawy: "))
    wysokosc = float(input("Podaj wysokość: "))
    pole = 0.5 * podstawa * wysokosc
elif wybor == 2:
    a = float(input("Podaj długość boku a: "))
    b = float(input("Podaj długość boku b: "))
    c = float(input("Podaj długość boku c: "))
    pol_obwod = 0.5 * (a + b + c)
    pole = (pol_obwod * (pol_obwod - a) * (pol_obwod - b) * (pol_obwod - c)) ** 0.5

print("Pole trójkąta wynosi:", pole)