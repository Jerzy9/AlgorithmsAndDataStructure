import queue

def prima():
    v = [1, 2, 3, 4, 5]
    pred = [0, 0, 0, 0, 0]
    k = [0, 100, 100, 100, 100]

    graf = [[0, 3, 0, 3, 5],
            [3, 0, 5, 1, 0],
            [0, 5, 0, 2, 0],
            [3, 1, 2, 0, 1],
            [5, 0, 0, 1, 0]]

    pq = [1,2,4,3,5]



    current_v = pq[0]

    while len(pq) != 0:

        if v[k.index(min(k))] in pq:
            current_v = v[k.index(min(k))]

        print(current_v)
        print(pq)
        pq.remove(current_v)


        for i in range(0, len(v)):
            # print(i)
            el = graf[current_v-1][i]

            if k[i] > el > 0 and i+1 in pq:
                k[i] = el
                pred[i] = current_v

#                 Brakuje tutej
#         pq.remove(current_v)

prima()





