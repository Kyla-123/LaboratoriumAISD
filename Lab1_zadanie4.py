liczbaa = int(input("Podaj liczbę elementów w tablicy : "))
if liczbaa == 0:
    print("Liczba elementów w tablicy wynosi 0 więc tablica nie posiada minimalnej wartości")
    exit()
tablica = []
for i in range(liczbaa):
    liczba = int(input("Podaj liczbę: "))
    tablica.append(liczba)
wartosc_min = min(tablica)
print("Minimalna wartość w tablicy: ", wartosc_min)
