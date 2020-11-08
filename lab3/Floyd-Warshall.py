import math

def floydWarshall():

    graf = [[0,        math.inf, -2,        math.inf],
            [4,        0,         3,        math.inf],
            [math.inf, math.inf,  0,        2       ],
            [math.inf, -1,        math.inf, 0       ]]

    l = len(graf)

    dist = list(map(lambda i: list(map(lambda j: j, i)), graf))

    for k in range(l):

        for i in range(l):

            for j in range(l):

                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                # print(dist[i][j])

    for i in range(l):
        print(dist[i])


floydWarshall()

