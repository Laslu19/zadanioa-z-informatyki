import math

print("Wybierz figurę:")
print("1. Kwadrat")
print("2. Prostokąt")
print("3. Trójkąt")

wybor = int(input("Twój wybór (1, 2 lub 3): "))

if wybor == 1:
    bok = float(input("Podaj długość boku kwadratu: "))
    pole = bok ** 2
    print("Pole kwadratu wynosi:", pole)
elif wybor == 2:
    bok_a = float(input("Podaj długość pierwszego boku prostokąta: "))
    bok_b = float(input("Podaj długość drugiego boku prostokąta: "))
    pole = bok_a * bok_b
    print("Pole prostokąta wynosi:", pole)
elif wybor == 3:
    podstawa = float(input("Podaj długość podstawy trójkąta: "))
    wysokosc = float(input("Podaj wysokość trójkąta: "))
    pole = 0.5 * podstawa * wysokosc
    print("Pole trójkąta wynosi:", pole)