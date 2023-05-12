a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
if a == b:
    dzielnik = a
else:
    while b != 0:
        zmienna = a
        a = b
        b = zmienna % b
    dzielnik = a
print("Największy wspólny dzielnik sposobem 2 wynośi :", dzielnik)

