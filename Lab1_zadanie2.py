def sprawdz_liczby():
    i = int(input("Podaj ilość liczb w ciągu: "))

    if i == 0:
        print("Ilość ujemnych liczb wynosi 0.")
        return

    ilosc = 0

    while i > 0:
        N = int(input("Podaj liczbę N: "))

        if N > 0:
            i -= 1
            if i == 0:
                print("Ilość liczb:", ilosc)
                return
        elif N < 0:
            ilosc += 1
            i -= 1
        else:  # N == 0
            if i == 0:
                print("Ilość liczb:", ilosc)
                return
            else:
                i -= 1

    print("Ilość ujemnych liczb:", ilosc)


sprawdz_liczby()