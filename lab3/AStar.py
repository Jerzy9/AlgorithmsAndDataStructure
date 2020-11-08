import math
import mmap
graf = [[0, 1, 0, 0, 0, 10],
        [0, 0, 2, 1, 0, 0],
        [0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0]]
l = len(graf)

v = [1, 2, 3, 4, 5, 6]
pred = [0] * l
h = [5, 3, 4, 2, 6, 0]
g = [math.inf] * l
f = [math.inf] * l



pq = [1, 2, 3, 4, 5, 6]


def reconstruct_path(cameFrom, current):
    pass


def astar():

    cameFrom = v.copy()

    g[0] = 0
    f[0] = h[0]
    goal = v[l-1]

    while len(pq) != 0:
        minF = math.inf
        for i in f:
            if minF >= i:
                minF = i

        print("minF: ", minF)
        indexMinF = f.index(minF)

        print("pq:  ", pq)
        print(f.index(minF))
        # find proper index
        current = -1
        for f_el in f:
            indexMinF = f.index(minF)
            if  indexMinF+1 in pq:
                current = indexMinF + 1
        if current == -1:
            break


        # if indexMinF+1 in pq:
        #     current = indexMinF+1
        # else:
        #     print("NIE MA CURRENT:   ", current)
        #     break

        if current == goal:
            return reconstruct_path(cameFrom, current)

        # remove current
        print(current, "sss")
        pq.remove(current)

        print(g)
        print(f)
        for n in range(l):

            if graf[current-1][n] > 0:
                gScore = g[current-1] + graf[current-1][n]

                if gScore < g[n]:

                    cameFrom = current
                    g[n] = gScore
                    f[n] = g[n] + h[n]

                    if n not in pq:
                        pq.append(n)


astar()