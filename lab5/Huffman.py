alpha2 = ['c', 'b', 'e', 'a', 'd'], \
         [0.4, 0.2, 0.2, 0.1, 0.1]
code = ["", "", "", "", ""]
hist = []


def huffman(alpha):
    hist_index = 0
    hist.append(alpha[1])
    length = len(alpha[1]) - 2
    sort_min(alpha)

    for i in range(0, length):
        tree = hist[hist_index].copy()
        new_tree = []

        if len(tree) > 2:
            tree.sort()
            sums = tree[0] + tree[1]
            new_tree.extend({sums})
            new_tree.extend(tree[2:])
            # new_tree.sort()
            hist.append(new_tree)
            hist_index += 1


def sort_min(al):
    length = len(al[1])
    for i in range(0, length):
        for j in range(0, length):

            if al[1][j] > al[1][i]:
                for k in range(0, 2):
                    temp = al[k][j]
                    al[k][j] = al[k][i]
                    al[k][i] = temp


def count(left, right, level, value, i):
   level -= 1

   if level < 0:
       code[0] = value + "0"
       code[1] = value + "1"
   elif left <= right:
       count(hist[level][0], hist[level][1], level, value + "0", i-1)
       code[i] = value + "1"

   else:
       count(hist[level][0], hist[level][1], level, value + "1", i-1)
       code[i] = value + "0"


huffman(alpha2)
count(hist[3][0], hist[3][1], len(hist)-1, "", len(hist[0])-1)

print("Alfabet z częstotliwością:", alpha2)
print("historia/drzewo:", hist, "\n")
print("wynik:")
print(alpha2[0])
print(code)
