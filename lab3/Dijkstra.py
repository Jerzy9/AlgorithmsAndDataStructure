import math

def dijkstra():
    v = [1, 2, 3, 4, 5]
    graf = [[0, 3, 0, 3, 5],
            [3, 0, 5, 1, 0],
            [0, 5, 0, 2, 0],
            [3, 1, 2, 0, 1],
            [5, 0, 0, 1, 0]]
    l = len(graf)

    pred = [0] * l
    dist = [math.inf] * l
    dist[0] = 0

    pq = [1, 2, 4, 3, 5]
    while len(pq) != 0:

        min_el = math.inf
        for z in range(l):
            if dist[z] < min_el and v[z] in pq:
                min_el = dist[z]

        if v[min_el] in pq:
            u = v[min_el]
        else:
            break

        for i in range(l):
            el = graf[u-1][i] + dist[u-1]

            if dist[i] > el > 0:
                dist[i] = el
                pred[i] = u

        pq.remove(u)

    print("Tablica pred: ", pred)
    print("Tablica dist: ", dist)


dijkstra()