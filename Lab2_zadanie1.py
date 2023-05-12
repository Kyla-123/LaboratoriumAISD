def Silnia(n):
    if n == 0:
        return 1
    elif n >= 1:
        return n * Silnia(n - 1)
n = int(input("Podaj liczbę aby uzyskać śilniet tej liczby: "))
if n < 0:
    print("Podana liczba musi być dodatnia aby móc otrzymać silnie tej liczby")
else:
    wynik = Silnia(n)
    print(f"Silnia {n}! wynośi {wynik}")
