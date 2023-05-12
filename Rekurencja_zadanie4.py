def kalkulatorbin(liczba):
    tablicabin = []
    while liczba != 0:
        if liczba % 2 == 0:
            tablicabin.append(0)
        else:
            tablicabin.append(1)
        liczba = liczba // 2
    tablicabin.reverse()
    return tablicabin
liczba = int(input("Podaj liczbę całkowitą: "))
liczbabin = kalkulatorbin(liczba)
print("Liczba podana to", liczba, "w systemie binarnym wygląda tak :",liczbabin)
