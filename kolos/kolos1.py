def wczytaj_tabele_z_pliku():
    tab = []
    try:
        file = open("zadanie1.txt")
        tab = file.read().split(", ")

        for i in range(len(tab)):
            tab[i] = int(tab[i])

    except ValueError:
        print("błędna wartość")
    except FileNotFoundError:
        print("nieznaleziono pliku")

    A = list(set(tab.copy()))

    return tab, A


def sortowanie_przez_zliczanie(tab, A):
    indexy = [0] * len(A)
    res = []

    for i in tab:
        index = A.index(i)
        indexy[index] += 1

    for i in range(0, len(A)):
        for j in range(0, indexy[i]):
            res.append(A[i])
    return res


tab, A = wczytaj_tabele_z_pliku()

print(tab)
print(A)
print()
print(sortowanie_przez_zliczanie(tab, A))
