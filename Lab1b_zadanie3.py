def lexicographic_sort(numbers):
    posortowane = sorted(map(str, numbers))
    posortowane.sort(key=lambda x: [int(d) for d in x])
    return posortowane
najmniejszailość = 4
Największailość = int(input("Podaj maksymalną ilość liczb do wprowadzenia minimalna ilość wynosi 4: "))
while Największailość < najmniejszailość:
    print("Maksymalna liczba musi być większa lub równa", najmniejszailość)
    Największailość = int(input("Podaj maksymalną ilość liczb do wprowadzenia minimalna ilość wynosi 4: "))
wpiszliczby = []
ilość = 0
while ilość < Największailość:
    number = input("Podaj liczbę naturalną: ")
    if number.isdigit():
        wpiszliczby.append(int(number))
        ilość += 1
    else:
        print("Ta liczba nie jest poprawna liczba naturalną Spróbuj jeszcze raz")
posortowane = lexicographic_sort(wpiszliczby)
print("Posortowane liczby leksykograficznie względem rozwinięć dziesiętnych wyglądają tak :")
print(" ".join(posortowane))
