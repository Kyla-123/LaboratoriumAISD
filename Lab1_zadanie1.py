import math

a = float(input("Podaj wartość a: "))
b = float(input("Podaj wartość b: "))
c = float(input("Podaj wartość c: "))

if a == 0:
    print("To nie jest równanie kwadratowe.")
else:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b - math.sqrt(delta))/(2*a)
        x2 = (-b + math.sqrt(delta))/(2*a)
        print("x1 =", x1)
        print("x2 =", x2)
    elif delta < 0:
        print("Brak rozwiązań rzeczywistych.")
    else:
        x1 = -b/(2*a)
        print("x1 =", x1)