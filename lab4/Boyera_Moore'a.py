def booyer(input, pattern):
    tab = [0]*len(pattern), [0]*len(pattern)
    index = 0

    for k in range(0, len(pattern)):

        if pattern[k] in tab[0]:
            tab[1][tab[0].index(pattern[k])] = k
        else:
            tab[0][index] = pattern[k]
            tab[1][index] = k
            index += 1

    print(tab)

    n = len(input)
    m = len(pattern)
    i = m - 1

    while i < n:
        j = m - 1

        while j < m:
            if pattern[j] == input[i]:
                print("found patter:", pattern)
                print("i:", i, "j:", j, "  ", "T[i]:", input[i], "P[j]:", pattern[j])
                if i + m < n:
                    i += m
                else:
                    i = n
                break

            elif input[i] in pattern:
                id = tab[0].index(input[i])
                j = tab[1][id]

            else:
                if i + m < n:
                    i += m
                else:
                    i = n
                break


booyer("ACBADBABCABD", "ABCAB")

