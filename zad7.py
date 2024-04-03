print("Podaj trzy liczby całkowite:")
num1 = int(input("Liczba 1: "))
num2 = int(input("Liczba 2: "))
num3 = int(input("Liczba 3: "))

if num1 >= num2 and num1 >= num3:
    max = num1
elif num2 >= num1 and num2 >= num3:
    max = num2
else:
    max = num3

print("Największa liczba to:", max)