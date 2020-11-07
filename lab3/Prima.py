import math

def prima():
    v = [1, 2, 3, 4, 5]
    graf = [[0, 3, 0, 3, 5],
            [3, 0, 5, 1, 0],
            [0, 5, 0, 2, 0],
            [3, 1, 2, 0, 1],
            [5, 0, 0, 1, 0]]
    l = len(graf)

    pred = [0] * l
    k = [math.inf] * l
    k[0] = 0

    pq = [1, 2, 3, 4, 5]
    while len(pq) != 0:

        min_el = math.inf
        for z in range(l):
            if k[z] < min_el and v[z] in pq:
                min_el = k[z]

        if v[k.index(min_el)] in pq:
            u = v[k.index(min_el)]
        else:
            break

        for i in range(l):
            el = graf[u-1][i]

            if k[i] > el > 0 and i+1 in pq:
                k[i] = el
                pred[i] = u

        pq.remove(u)

    print("Tablica k: ")
    print(k)
    print("Tablica pred: ")
    print(pred)


prima()