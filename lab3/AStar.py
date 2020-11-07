import math


def astar():
    v = [1, 2, 3, 4, 5, 6]
    graf = [[0, 1, 0, 0, 0, 10],
            [0, 0, 2, 1, 0, 0],
            [0, 0, 0, 0, 5, 0],
            [0, 0, 0, 0, 3, 4],
            [0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0]]
    l = len(graf)

    pred = [0] * l

    h = [5, 3, 4, 2, 6, 0]
    g = [math.inf] * l
    f = [math.inf] * l

    pq = [1, 2, 4, 6, 3, 5]
    while len(pq) != 0:

        u = pq.pop(0)

        min_num = math.inf
        for i in range(l):

            if min_num > graf[u-1][i] > 0:
                min_num = graf[u-1][i]
                min_index = i
        print(min_num , " ssssssssssssssssssss")
        g[u-1] = g[u-1] + min_num
        print("g:  ", g)
        for i in range(l):
            dist = h[u-1] + g[i]

            if dist > f[i] and graf[u-1][i] > 0:
                f[i] = dist
                pred[i] = u
        print(u)
        # pq.remove(u)

    print("v:  ", v)
    print("pred  ", pred)
    print("h:  ", h)
    print("g:  ", g)
    print("f:  ", f)


astar()