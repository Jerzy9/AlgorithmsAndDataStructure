def quick_sort(low, high):
    if low < high:
        pi = partition(low, high)
        quick_sort(low, pi -1)
        quick_sort(pi + 1, high)


def partition(low, high):
    pivot = tab[high]

    i = low -1
    index = 0

    for j in range(low, high):

        if tab[j] < pivot:
            i += 1

            temp = tab[j]
            tab[j] = tab[i]
            tab[i] = temp

            index = i

    temp = tab[i+1]
    tab[i+1] = tab[high]
    tab[high] = temp

    return i + 1


tab = [2,45,76,3,5,7,34,67,67,234,2,57,6,856,8,356,34,542,3]
print(tab)
quick_sort(0, len(tab)-1)
print(tab)