x = int(input("Podaj pierwszą liczbę:"))
y = int(input("Podaj drugą liczbę:"))
z = int(input("Podaj trzecią liczbę:"))

if x > y and x > z:
    print(f"x({x}) jest największy")
elif y > x and y > z:
    print(f"y({y}) jest największy")
elif z > x and z > y:
    print(f"z({z}) jest największy")