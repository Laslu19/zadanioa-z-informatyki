print("Wybierz operację:")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")

wybor = int(input("Twój wybór (1, 2, 3 lub 4): "))

if wybor not in [1, 2, 3, 4]:
    print("Niepoprawny wybór.")
else:
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))

    if wybor == 1:
        wynik = liczba1 + liczba2
        print("Wynik dodawania:", wynik)
    elif wybor == 2:
        wynik = liczba1 - liczba2
        print("Wynik odejmowania:", wynik)
    elif wybor == 3:
        wynik = liczba1 * liczba2
        print("Wynik mnożenia:", wynik)
    elif wybor == 4:
        if liczba2 == 0:
            print("Nie można dzielić przez zero.")
        else:
            wynik = liczba1 / liczba2
            print("Wynik dzielenia:", wynik)