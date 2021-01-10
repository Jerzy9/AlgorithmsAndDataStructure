def heap(n, i):
    L = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and tab[L] < tab[l]:
        L = l

    if r < n and tab[L] < tab[r]:
        L = r

    if L != i:
        temp = tab[L]
        tab[L] = tab[i]
        tab[i] = temp

        heap(n, L)


def heapSort():
    l = len(tab)

    for i in range(l // 2 - 1, -1, -1):
        heap(l, i)

    for i in range(l - 1, 0, -1):
        temp = tab[0]
        tab[0] = tab[i]
        tab[i] = temp

        heap(i, 0)


tab = [2, 45, 76, 3, 5, 7, 34, 67, 67, 234, 2, 57, 6, 856, 8, 356, 34, 542, 3]
print(tab)
heapSort()
print(tab)
