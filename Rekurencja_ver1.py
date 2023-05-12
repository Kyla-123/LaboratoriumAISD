a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
if a == b:
    dzielnik = a
else:
    while True:
        if a > b:
            a = a - b
        else:
            b = b - a
        if a == b:
            gcd = a
            break
print("Największy wspólny dzielnik: ", dzielnik)
