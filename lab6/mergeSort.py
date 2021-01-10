def merge_sort(l, r):
    if l < r:
        m = int((l+r)/2)

        merge_sort(l, m)
        merge_sort(m+1, r)

        counting_sort(l, r, m)


def counting_sort(l, r, m):
    lengthL = m - l + 1
    lengthR = r - m

    L = []
    R = []

    for i in range(0, lengthL):
        L.append(tab[l+i])

    for i in range(0, lengthR):
        R.append(tab[m+1+i])

    i = 0
    j = 0
    k = l

    while i < lengthL and j < lengthR:

        if L[i] <= R[j]:
            tab[k] = L[i]
            i += 1

        else:
            tab[k] = R[j]
            j += 1

        k +=1

    while i < lengthL:
        tab[k] = L[i]

        i += 1
        k += 1

    while j < lengthR:
        tab[k] = R[j]

        j += 1
        k += 1


tab = [2,45,76,3,5,7,34,67,67,234,2,57,6,856,8,356,34,542,3]
print(tab)
merge_sort(0, len(tab)-1)
print(tab)