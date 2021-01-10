tab = [2,45,76,3,5,7,34,67,67,234,2,57,6,856,8,356,34,542,3]


def bubble_sort(tab):
    l = len(tab)

    for i in range(0, l):

        for j in range(0, l - i - 1):

            if tab[j] > tab[j+1]:
                temp = tab[j]
                tab[j] = tab[j+1]
                tab[j+1] = temp

    return tab

print(tab)
print(bubble_sort(tab))