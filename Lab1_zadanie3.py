import random

liczba_elementow = int(input("Podaj liczbę elementów w tablicy: "))

if liczba_elementow == 0:
    print("Liczba elementów w tablicy wynosi 0 dlatego nie można sprawdzić czy element należy do tablicy")
    exit()

tablica = [random.randint(0, 10) for i in range(liczba_elementow)]

N = int(input("Podaj liczbę do sprawdzenia w przedziale od 0-10: "))

if N in tablica:
    print("Liczba", N, "znajduje się w tablicy.")
else:
    print("Liczba", N, "nie znajduje się w tablicy jednowymiarowej.")

print("Liczby w które znajdują się w tablicy to :",   tablica)
