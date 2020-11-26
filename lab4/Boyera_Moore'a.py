def booyer(input, pattern):
    # i = len(input)
    #
    # tab = [0]*len(pattern), [0]*len(pattern)
    # index = 0
    #
    # for k in range(0, len(pattern)):
    #     # print(tab)
    #     if pattern[k] in tab[0]:
    #         # print(tab[0].index(pattern[k]))
    #         tab[1][tab[0].index(pattern[k])] = k
    #     else:
    #         tab[0][index] = pattern[k]
    #         tab[1][index] = k
    #         index += 1
    #
    # print(tab)

    # while i < len(input):
    #     j = len(pattern) -1
    #
    #     if i == 0:
    #         i = j
    #
    #     pattern[j]
    #
    #     if input[i] == pattern[j]:
    #         print("Znaleziono wzorzec")

    n = len(input)
    m = len(pattern)
    i = m - 1

    while i <= n-1:
        print(2)
        j = m - 1

        while j >= m - 1:
            print("i:", i, "j:", j, "  ", "T[i]:", input[i], "P[j]:", pattern[j])
            if pattern[j] == input[i]:
                if j == 0:
                    print(pattern)
                else:
                    j -= 1
                    i -= 1
            else:
                print(last(input[i], pattern))
                print(input[i])

                j += m - min(j, 1 + last(input[i], pattern))
                j = m - 1


def last(czarek, pattern):
    index = 999999
    for i in range(0, len(pattern)):
        if i == czarek:
            index = i
    return index



# booyer("ABACADEFGABABGBMIABORIGAMI", "ORIGAMI")

last()