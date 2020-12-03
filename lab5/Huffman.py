
alpha = {'a': 0.1, 'b': 0.2, 'c': 0.4, 'd': 0.1, 'e': 0.2}


def huffman():
    tree = alpha.values()
    length = len(tree) - 1

    for i in range(0, length):
        new_tree = []
        if len(tree) >= 2:
            # tree.sort()
            print(tree)
            sums = tree[0] + tree[1]
            new_tree.extend(tree[2:])
            new_tree.extend({sums})
            tree = new_tree

huffman()


