def odwróc(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    odwróc(arr, start + 1, end - 1)
def odwróc2():
    n = int(input("Podaj ilość liczb które zostaną umieszczone w tablicy: "))
    if n < 1:
        print("Nie można dokonać operacji ponieważ nie ma liczb w tablicy.")
        return
    array = []
    for i in range(n):
        num = int(input(f"Podaj liczbę {i+1}: "))
        array.append(num)
    print("Tablica przed odwróceniem wygląda tak:", array)
    odwróc(array, 0, len(array) - 1)
    print("Tablica po odwróceniu wygląda tak:", array)
odwróc2()
