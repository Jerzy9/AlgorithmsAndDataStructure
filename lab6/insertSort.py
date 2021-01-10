tab = [2,45,76,3,5,7,34,67,67,234,2,57,6,856,8,356,34,542,3]


def insert_sort(tab):
    l = len(tab)

    for i in range(0, l):
        key = tab[i]
        j = i - 1

        while j >= 0 and tab[j] > key:
            tab[j+1] = tab[j]
            j -= 1

        tab[j+1] = key

    return tab


print(insert_sort(tab))