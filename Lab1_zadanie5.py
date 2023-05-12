liczba_wierszy = int(input("Podaj liczbę wierszy tablicy dwuwymiarowej: "))
liczba_kolumn = int(input("Podaj liczbę kolumn tablicy dwuwymiarowej: "))
tablica = []
for i in range(liczba_wierszy):
    wiersz = []
    for j in range(liczba_kolumn):
        liczba = int(input("Podaj wartość tablicy [{}] [{}]: ".format(i, j)))
        wiersz.append(liczba)
    tablica.append(wiersz)
print("Tablica przed przeniesieniem najmniejszych wartości wygląda tak :")
for wiersz in tablica:
    print(wiersz)
for i in range(liczba_wierszy):
    min_wartosc = min(tablica[i])
    index_min = tablica[i].index(min_wartosc)
    tablica[i][0], tablica[i][index_min] = tablica[i][index_min], tablica[i][0]
print("Tablica po przeniesieniu najmniejszych wartości wygląda tak :")
for wiersz in tablica:
    print(wiersz)
